"""
Static hydrogen electron clouds: |psi|^2 in a plane through the nucleus.

Panels: 1s, 2s, 2p_z, 3p_z  (the states used in the later superposition figures).
All panels share one spatial window (in Bohr radii) and one color scale, so the
relative sizes and brightnesses are honest. A gamma < 1 compresses the color
scale so the diffuse n = 3 cloud stays visible next to the compact 1s cloud.
The z axis is vertical, matching the dipole-axis convention of Figure 1.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import PowerNorm

OUTFILE = "hydrogen_static_clouds.png"
HALF = 24.0        # half-width of the window, in Bohr radii (same for all panels)
N = 1200           # grid points per axis
GAMMA = 0.3        # <1 brightens faint regions; same for all panels


# Hydrogen radial functions R_nl(r), atomic units (a0 = 1), normalized so that
# integral R^2 r^2 dr = 1
def R10(r): return 2.0 * np.exp(-r)
def R20(r): return (1 / (2 * np.sqrt(2))) * (2 - r) * np.exp(-r / 2)
def R21(r): return (1 / (2 * np.sqrt(6))) * r * np.exp(-r / 2)
def R31(r): return (8 / (27 * np.sqrt(6))) * r * (1 - r / 6) * np.exp(-r / 3)

# Real angular parts, normalized over the sphere
Y00 = 1 / np.sqrt(4 * np.pi)
def Y10(cos_t): return np.sqrt(3 / (4 * np.pi)) * cos_t

STATES = [
    ("1s",   lambda r, c: R10(r) * Y00),
    ("2s",   lambda r, c: R20(r) * Y00),
    ("2p",   lambda r, c: R21(r) * Y10(c)),
    ("3p",   lambda r, c: R31(r) * Y10(c)),
]


def check_normalization():
    """Radial integrals of R^2 r^2 must be 1 (angular parts are normalized by construction)."""
    r = np.linspace(0, 200, 400001)
    for name, R in [("1s", R10), ("2s", R20), ("2p", R21), ("3p", R31)]:
        val = np.trapezoid(R(r) ** 2 * r ** 2, r)
        print(f"normalization {name}: {val:.6f}")


def density_slice(psi):
    x = np.linspace(-HALF, HALF, N)
    z = np.linspace(-HALF, HALF, N)
    X, Z = np.meshgrid(x, z)
    r = np.sqrt(X ** 2 + Z ** 2)
    cos_t = np.divide(Z, r, out=np.zeros_like(r), where=r > 0)
    return psi(r, cos_t) ** 2


if __name__ == "__main__":
    check_normalization()

    dens = [density_slice(psi) for _, psi in STATES]
    vmax = max(d.max() for d in dens)           # one common scale (1s peak, 1/pi)
    norm = PowerNorm(gamma=GAMMA, vmin=0, vmax=vmax)

    fig, axes = plt.subplots(1, 4, figsize=(16, 4.6), facecolor="white")
    for ax, (name, _), d in zip(axes, STATES, dens):
        ax.imshow(d, origin="lower", extent=[-HALF, HALF, -HALF, HALF],
                  cmap="magma", norm=norm, interpolation="bilinear")
        ax.set_title(name, fontsize=18, pad=8)
        ax.set_xticks([])
        ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(False)
        # scale bar: 10 a0, same in every panel
        ax.plot([-HALF + 2, -HALF + 12], [-HALF + 2.5, -HALF + 2.5], color="white", lw=3)
        ax.text(-HALF + 7, -HALF + 4.0, r"10 $a_0$", color="white",
                ha="center", va="bottom", fontsize=11)

    plt.tight_layout()
    fig.savefig(OUTFILE, dpi=200, facecolor="white")
    print(f"saved {OUTFILE}")
