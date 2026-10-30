"""Experimental PyVista feature image: a hydrogen 2p_z cloud and its reflection.

Install: pip install pyvista numpy vtk
Run: python atomic_orbital_mirror.py
Use --save to export a PNG (requires a working VTK rendering backend).
"""
import argparse
import numpy as np
import pyvista as pv

def make_orbital(n=110, extent=12.0, mirror_x=8.0, distance=5.5):
    """Real 2p_z wavefunction (arbitrary normalized units), shifted in front of mirror."""
    axis = np.linspace(-extent, extent, n)
    x, y, z = np.meshgrid(axis, axis, axis, indexing="ij")
    # 2p_z amplitude proportional to z exp(-r/2a0), with a0=1.
    r = np.sqrt(x*x + y*y + z*z)
    psi = z * np.exp(-r / 2.0)
    psi /= np.max(np.abs(psi))
    grid = pv.ImageData(dimensions=(n,n,n),
                        spacing=(axis[1]-axis[0],)*3,
                        origin=(axis[0],)*3)
    grid.point_data["psi"] = psi.ravel(order="F")
    # Original orbital centered at x = mirror_x-distance.
    front = grid.copy()
    front.translate((mirror_x-distance, 0, 0), inplace=True)
    # Reflection: mirror x -> 2*mirror_x-x; also reverse the x direction
    # of the density, so it is geometrically mirrored rather than duplicated.
    back = grid.copy()
    back.point_data["psi"] = psi[::-1, :, :].ravel(order="F")
    back.translate((mirror_x+distance, 0, 0), inplace=True)
    return front, back

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--save", action="store_true", help="Save PNG without opening a window")
    ap.add_argument("--output", default="atomic_orbital_mirror.png")
    ap.add_argument("--resolution", type=int, default=110)
    args = ap.parse_args()

    pv.global_theme.allow_empty_mesh = True
    plotter = pv.Plotter(off_screen=args.save, window_size=(1600, 900))
    plotter.set_background("#070b15")
    front, back = make_orbital(n=args.resolution)

    # Volume opacity transfer function: nearly invisible around psi=0,
    # visible at positive/negative amplitude. Experiment with these numbers.
    opacity = [0.45, 0.22, 0.07, 0.0, 0.07, 0.22, 0.45]
    plotter.add_volume(front, scalars="psi", clim=(-1,1),
                       cmap="coolwarm", opacity=opacity,
                       shade=False, show_scalar_bar=False)
    plotter.add_volume(back, scalars="psi", clim=(-1,1),
                       cmap="coolwarm", opacity=[v*0.25 for v in opacity],
                       shade=False, show_scalar_bar=False)

    # The 'mirror' is a translucent plane, deliberately stylized.
    mirror_x = 8.0
    plane = pv.Plane(center=(mirror_x, 0, 0), direction=(1, 0, 0),
                     i_size=27, j_size=27)
    plotter.add_mesh(plane, color="#8da4c0", opacity=0.12,
                     show_edges=False, lighting=False)
    plotter.camera_position = [(32, -35, 17), (8, 0, 0), (0, 0, 1)]
    plotter.camera.zoom(1.1)
    if args.save:
        plotter.screenshot(args.output)
        print(f"Saved {args.output}")
        plotter.close()
    else:
        plotter.show()

if __name__ == "__main__":
    main()
