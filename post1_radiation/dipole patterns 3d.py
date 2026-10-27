"""
Two-panel 3D figure: radiation patterns of a linear and a circulating dipole.

Left : dipole oscillating along z       -> power ~ sin^2(theta)
Right: electron circulating about z     -> power ~ 1 + cos^2(theta)
Both panels use the same radial scale and the same color range.
"""
import numpy as np
import pyvista as pv
import os
os.chdir(os.path.dirname(__file__))
print(f"Current working directory: {os.getcwd()}")
OFF_SCREEN = True          # set False for an interactive window
OUTFILE = "dipole_patterns_3d.png"

pv.global_theme.background = "white"
pv.global_theme.font.color = "black"


def pattern_surface(power, n=150):
    """Surface whose distance from the origin is the radiated power in that direction."""
    theta = np.linspace(0, np.pi, n)
    phi = np.linspace(0, 2 * np.pi, n)
    T, P = np.meshgrid(theta, phi)
    R = power(T)
    X = R * np.sin(T) * np.cos(P)
    Y = R * np.sin(T) * np.sin(P)
    Z = R * np.cos(T)
    grid = pv.StructuredGrid(X, Y, Z)
    grid["power"] = R.ravel(order="F")
    return grid


linear = pattern_surface(lambda t: np.sin(t) ** 2)           # peak 1
circular = pattern_surface(lambda t: 1 + np.cos(t) ** 2)     # peak 2, equator 1

pl = pv.Plotter(shape=(1, 2), window_size=(1800, 900), off_screen=OFF_SCREEN, border=False)

# Camera shared by both panels
cam = [(6.4, -8.0, 4.0), (0, 0, 0.0), (0, 0, 1)]   # far enough to fit the tall right-hand pattern
AXIS_LEN = 2.3
RED = "#D85A30"
SURFACE = dict(scalars="power", cmap="YlGnBu", clim=(0, 3),
               smooth_shading=True, show_scalar_bar=False, opacity=0.55)


def add_axis(label):
    pl.add_mesh(pv.Line((0, 0, -AXIS_LEN), (0, 0, AXIS_LEN)), color="gray", line_width=2)
    pl.add_point_labels(
        [(0, 0, AXIS_LEN + 0.25)], [label],
        font_size=28, shape=None, show_points=False, text_color="black",
    )


# ---- Left panel: linear dipole -------------------------------------------
pl.subplot(0, 0)
pl.add_mesh(linear, **SURFACE)
add_axis("Dipole axis")
# oscillating charge: double-headed arrow along z with the electron on it
pl.add_mesh(pv.Arrow(start=(0, 0, -0.7), direction=(0, 0, 1), scale=1.4,
                     tip_length=0.25, tip_radius=0.09, shaft_radius=0.035), color=RED)
pl.add_mesh(pv.Arrow(start=(0, 0, 0.7), direction=(0, 0, -1), scale=1.4,
                     tip_length=0.25, tip_radius=0.09, shaft_radius=0.035), color=RED)
pl.add_mesh(pv.Sphere(radius=0.11, center=(0, 0, 0.35)), color="black")
pl.add_text("Oscillating electron", position="lower_edge", font_size=16, color="black")
pl.camera_position = cam

# ---- Right panel: circulating electron -----------------------------------
pl.subplot(0, 1)
pl.add_mesh(circular, **SURFACE)
add_axis("Rotation axis")
# orbit, electron, direction of motion, nucleus
r_orb = 0.45
a = np.linspace(0, 2 * np.pi, 200)
orbit = np.c_[r_orb * np.cos(a), r_orb * np.sin(a), np.zeros_like(a)]
pl.add_mesh(pv.lines_from_points(orbit), color=RED, line_width=5)
pl.add_mesh(pv.Sphere(radius=0.11, center=(r_orb, 0, 0)), color="black")
pl.add_mesh(pv.Arrow(start=(r_orb, 0, 0), direction=(0, 1, 0), scale=0.55,
                     tip_length=0.35, tip_radius=0.1, shaft_radius=0.035), color=RED)
pl.add_mesh(pv.Sphere(radius=0.06, center=(0, 0, 0)), color="gray")
pl.add_text("Circulating electron", position="lower_edge", font_size=16, color="black")
pl.camera_position = cam

if OFF_SCREEN:
    pl.screenshot(OUTFILE)
    print(f"saved {OUTFILE}")
else:
    pl.show()
