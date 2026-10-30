"""Dense hydrogen 2p_z point cloud with configurable sphere finish and mirror.

Install: pip install numpy pyvista vtk
Examples:
  python atomic_2p_dense_spheres.py
  python atomic_2p_dense_spheres.py --mass 90 --points 16000 --size-cv 0.25
  python atomic_2p_dense_spheres.py --show-boundary --save

The boundary is an isodensity surface enclosing the chosen fraction of
the *full* 2p_z probability mass. The cloud is then resampled CONDITIONAL
on being inside it, so no spheres are drawn outside the boundary.
"""
import argparse
import numpy as np
import pyvista as pv
import os
os.chdir(os.path.dirname(__file__))
print(f"Current working directory: {os.getcwd()}")

def density(xyz):
    r = np.linalg.norm(xyz, axis=-1)
    return xyz[..., 2]**2 * np.exp(-r)  # |psi_2pz|², constants cancel

def find_cutoff(mass, resolution=160, extent=24.0):
    """Integrate the analytic density on a uniform grid; find HPD threshold."""
    axis = np.linspace(-extent, extent, resolution)
    step = axis[1]-axis[0]
    x, y, z = np.meshgrid(axis, axis, axis, indexing="ij")
    d = z*z * np.exp(-np.sqrt(x*x+y*y+z*z))
    sorted_d = np.sort(d.ravel())[::-1]
    cdf = np.cumsum(sorted_d, dtype=np.float64)
    cutoff = float(sorted_d[min(np.searchsorted(cdf, mass/100*cdf[-1]), len(sorted_d)-1)])
    grid = pv.ImageData(dimensions=(resolution,)*3,
                        spacing=(step,)*3, origin=(axis[0],)*3)
    grid.point_data["density"] = d.ravel(order="F")
    return cutoff, grid

def sample_inside(n, cutoff, rng):
    """Exact independent samples from 2p_z density, rejection-filtered by cutoff."""
    pieces = []
    remaining = n
    while remaining:
        batch = max(3000, int(remaining*3))
        r = rng.gamma(shape=5.0, scale=1.0, size=batch)
        # angular PDF is 3/2 cos²(theta); signed cube root of uniform
        u = np.cbrt(rng.uniform(-1, 1, size=batch))
        phi = rng.uniform(0, 2*np.pi, size=batch)
        radial = r*np.sqrt(1-u*u)
        xyz = np.column_stack((radial*np.cos(phi), radial*np.sin(phi), r*u))
        xyz = xyz[density(xyz) >= cutoff]
        take = min(remaining, len(xyz))
        if take:
            pieces.append(xyz[:take])
            remaining -= take
    return np.vstack(pieces)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--points", type=int, default=2000,
                    help="Number of spheres INSIDE the boundary")
    ap.add_argument("--mass", type=float, default=85,
                    help="Probability mass enclosed by boundary, e.g. 80 or 90")
    ap.add_argument("--radius", type=float, default=0.185,
                    help="Median sphere radius in Bohr radii")
    ap.add_argument("--size-cv", type=float, default=0.22,
                    help="Coefficient of variation of sphere radii (0=equal size)")
    ap.add_argument("--show-boundary", action="store_true",
                    help="Draw faint wireframe boundary; invisible by default")
    ap.add_argument("--boundary-opacity", type=float, default=0.17)
    ap.add_argument("--boundary-resolution", type=int, default=160)
    ap.add_argument("--seed", type=int, default=23)
    ap.add_argument("--mirror", action=argparse.BooleanOptionalAction, default=True,
                    help="Add an artistic virtual reflection and mirror plane")
    ap.add_argument("--mirror-x", type=float, default=14.0,
                    help="Mirror plane x position, in Bohr radii")
    ap.add_argument("--reflection-brightness", type=float, default=0.48,
                    help="Reflection brightness multiplier, 0 to 1")
    ap.add_argument("--mirror-opacity", type=float, default=0.05,
                    help="Translucency of mirror plane (0 to 1)")
    ap.add_argument("--finish", choices=["matte", "satin", "metallic", "glossy"],
                    default="metallic", help="Sphere material preset")
    ap.add_argument("--specular", type=float, default=None,
                    help="Override material specular strength, 0 to 1")
    ap.add_argument("--roughness", type=float, default=None,
                    help="PBR roughness override, 0 to 1")
    ap.add_argument("--save", action="store_true", default=True,
                    help="Save the output to a file instead of showing it interactively")
    ap.add_argument("--output", default="atomic_2p_dense_spheres.png")
    args = ap.parse_args()
    if not (0 < args.mass < 100): ap.error("--mass must be between 0 and 100")
    if not (0 <= args.reflection_brightness <= 1 and 0 <= args.mirror_opacity <= 1):
        ap.error("reflection brightness and mirror opacity must be between 0 and 1")
    if args.roughness is not None and not 0 <= args.roughness <= 1:
        ap.error("--roughness must be between 0 and 1")
    if args.specular is not None and not 0 <= args.specular <= 1:
        ap.error("--specular must be between 0 and 1")
    if args.points < 1 or args.radius <= 0 or args.size_cv < 0:
        ap.error("--points > 0, --radius > 0, --size-cv >= 0 required")
    rng = np.random.default_rng(args.seed)
    cutoff, grid = find_cutoff(args.mass, args.boundary_resolution)
    xyz = sample_inside(args.points, cutoff, rng)
    # Lognormal radii with requested coefficient of variation; median fixed.
    sigma = np.sqrt(np.log1p(args.size_cv**2))
    radii = args.radius*np.exp(sigma*rng.normal(size=len(xyz)))
    pl = pv.Plotter(off_screen=args.save, window_size=(1600, 900))
    pl.set_background("#03050b")
    pl.enable_anti_aliasing("ssaa")
    pl.add_light(pv.Light(position=(15,-20,25), focal_point=(0,0,0),
                          color="white", intensity=2.2))
    pl.add_light(pv.Light(position=(-18,12,5), focal_point=(0,0,0),
                          color="#6688ff", intensity=0.45))
    # PBR sphere materials, with optional manual specular override.
    presets = {
        "matte": (0.0, 0.90, 0.10),
        "satin": (0.15, 0.55, 0.30),
        "metallic": (0.80, 0.28, 0.70),
        "glossy": (0.15, 0.12, 0.95),
    }
    metallic, roughness, specular = presets[args.finish]
    if args.roughness is not None:
        roughness = args.roughness
    if args.specular is not None:
        specular = args.specular
    unit_sphere = pv.Sphere(radius=1, theta_resolution=12, phi_resolution=12)

    def add_cloud(coords, sizes, brightness=1.0):
        for mask, rgb in ((coords[:, 2] >= 0, (0.5, 1.00, 0.19)),
                          (coords[:, 2] < 0, (0.04, 0.65, 1.0))):
            cloud = pv.PolyData(coords[mask])
            cloud["radius"] = sizes[mask]
            spheres = cloud.glyph(scale="radius", geom=unit_sphere,
                                  orient=False, factor=1.0)
            color = tuple(min(1.0, channel*brightness) for channel in rgb)
            pl.add_mesh(spheres, color=color, smooth_shading=True,
                        pbr=True, metallic=metallic, roughness=roughness,
                        ambient=0.15, diffuse=0.8,
                        specular=specular, specular_power=32,
                        show_scalar_bar=False)

    add_cloud(xyz, radii)

    if args.mirror:
        # Reflection is a geometrically mirrored copy, not optical ray tracing.
        # It sits behind a translucent mirror plane so it remains visible.
        reflected = xyz.copy()
        reflected[:, 0] = 2*args.mirror_x - reflected[:, 0]
        add_cloud(reflected, radii, args.reflection_brightness)

        # Mirror in the yz plane. Subtle dark glass rather than a plastic shell.
        mirror = pv.Plane(center=(args.mirror_x, 0, 0),
                          direction=(1, 0, 0), i_size=37, j_size=37)
        pl.add_mesh(mirror, color="#6d7c92",
                    opacity=args.mirror_opacity, lighting=False)
        # Thin frame, slightly wider than the reflective panel.
        frame = pv.Plane(center=(args.mirror_x+0.02, 0, 0),
                         direction=(1, 0, 0), i_size=38, j_size=38)
        pl.add_mesh(frame, style="wireframe", color="#8b95a6",
                    opacity=0.65, line_width=2, lighting=False)

    if args.show_boundary:
        boundary = grid.contour([cutoff], scalars="density")
        pl.add_mesh(boundary, style="wireframe", color="#9daab8",
                    opacity=args.boundary_opacity, line_width=0.6,
                    lighting=False, show_scalar_bar=False)
    pl.camera_position = (
        [(-25.504035357169172, -35.26011937346284, -0.8458479500578157),
        (12.007484452786336, 1.9285294820415322, -0.8302589921571384),
        (0.007393983993900297, -0.007877339837629702, 0.9999416365557445)]
    )
    # pl.camera.zoom(1.1 if args.mirror else 1.2)
    if args.save:
        pl.screenshot(args.output)
        print(f"Saved {args.output}")
        pl.close()
    else:
        pl.show()
        print("Camera position:")
        print(pl.camera_position)

if __name__ == "__main__":
    main()
