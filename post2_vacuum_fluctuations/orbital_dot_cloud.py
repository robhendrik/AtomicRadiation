"""Cinematic hydrogen 2p_z orbital as a sampled 3D probability cloud.

Install: pip install numpy pyvista vtk
Run:     python atomic_2p_pointcloud.py
Save:    python atomic_2p_pointcloud.py --save

The dots sample |psi_2p_z|^2. Gold and cyan represent opposite signs
(relative phase 0/pi) of the *wavefunction*, not electric charges.
All distances are in Bohr radii a0. This first study has NO mirror.
"""
import argparse
import numpy as np
import pyvista as pv


def sample_2pz(count: int, seed: int) -> np.ndarray:
    """Exactly sample the angular/radial distribution of hydrogen 2p_z.

    Probability volume element: r^4 exp(-r/a0) dr * cos²(theta) dOmega.
    Thus r/a0 ~ Gamma(shape=5,scale=1), cos(theta) has density 3u²/2.
    """
    rng = np.random.default_rng(seed)
    r = rng.gamma(shape=100.0, scale=1.0, size=count)
    u = np.cbrt(rng.uniform(-1.0, 1.0, size=count))
    phi = rng.uniform(0, 2 * np.pi, size=count)
    rho = r * np.sqrt(1 - u*u)
    return np.column_stack((rho * np.cos(phi), rho * np.sin(phi), r * u))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--points', type=int, default=11000)
    parser.add_argument('--seed', type=int, default=23)
    parser.add_argument('--point-size', type=float, default=4.1)
    parser.add_argument('--save', action='store_true')
    parser.add_argument('--output', default='atomic_2p_pointcloud.png')
    args = parser.parse_args()

    xyz = sample_2pz(args.points, args.seed)
    plotter = pv.Plotter(off_screen=args.save, window_size=(1600, 900))
    plotter.set_background('#03050b')

    # Phase sign: the real 2p_z wavefunction is proportional to z exp(-r/2).
    for selector, color in [(xyz[:, 2] >= 0, '#ffd05c'),
                            (xyz[:, 2] < 0, '#22c9ff')]:
        cloud = pv.PolyData(xyz[selector])
        plotter.add_mesh(cloud, color=color, style='points',
                         point_size=args.point_size,
                         render_points_as_spheres=True,
                         lighting=False, show_scalar_bar=False)

    # Tilted camera makes the two lobes read as a 3D object.
    plotter.camera_position = [(26, -38, 21), (0, 0, 0), (0, 0, 1)]
    plotter.camera.zoom(1.15)
    if args.save:
        plotter.screenshot(args.output)
        print(f'Saved {args.output}')
        plotter.close()
    else:
        plotter.show()


if __name__ == '__main__':
    main()