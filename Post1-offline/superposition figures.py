"""
Coherent superpositions of hydrogen 1s with 2p_z, 3p_z and 2s, frozen at four
relative phases phi = (E_e - E_g) t / hbar = 0, pi/2, pi, 3pi/2.

    Psi = (psi_g + exp(-i phi) psi_e) / sqrt(2)        (real orbitals, equal weights)
    |Psi|^2 = 1/2 (psi_g^2 + psi_e^2) + psi_g psi_e cos(phi)
    <d_z>   = -e <z> = -e <g|z|e> cos(phi)

Common spatial window, common (gamma-compressed) color scale and common dipole-arrow
scale in all three figures, so they can be compared directly.
The arrow is the electric dipole moment d = -e<r>, NOT the electron cloud: it points
opposite to the displacement of the cloud's center of charge.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import PowerNorm

HALF = 16.0         # half-width of the window, in Bohr radii (same in every figure)
N = 900
GAMMA = 0.3
ARROW_MAG = 6.0     # arrow length = ARROW_MAG * |<z>| in a0 (same in every figure)
ARROW_COLOR = "#4DD0E1"
PHASES = [(0.0, r"$\phi = 0$"), (np.pi / 2, r"$\phi = \pi/2$"),
          (np.pi, r"$\phi = \pi$"), (3 * np.pi / 2, r"$\phi = 3\pi/2$")]


# --- hydrogen orbitals (a0 = 1), real angular parts ---------------------------
def R10(r): return 2.0 * np.exp(-r)
def R20(r): return (1 / (2 * np.sqrt(2))) * (2 - r) * np.exp(-r / 2)
def R21(r): return (1 / (2 * np.sqrt(6))) * r * np.exp(-r / 2)
def R31(r): return (8 / (27 * np.sqrt(6))) * r * (1 - r / 6) * np.exp(-r / 3)
Y00 = 1 / np.sqrt(4 * np.pi)
def Y10(c): return np.sqrt(3 / (4 * np.pi)) * c

ORB = {
    "1s": lambda r, c: R10(r) * Y00,
    "2s": lambda r, c: R20(r) * Y00,
    "2p": lambda r, c: R21(r) * Y10(c),
    "3p": lambda r, c: R31(r) * Y10(c),
}


def transition_z(excited):
    """<1s| z |excited> in units of a0, by 3D quadrature (r, cos t) -- independent check."""
    r = np.linspace(0, 80, 8001)
    c = np.linspace(-1, 1, 2001)
    Rg, Cg = np.meshgrid(r, c, indexing="ij")
    integrand = ORB["1s"](Rg, Cg) * ORB[excited](Rg, Cg) * (Rg * Cg) * Rg ** 2
    ang = np.trapezoid(integrand, c, axis=1) * 2 * np.pi
    return np.trapezoid(ang, r)


def grid():
    x = np.linspace(-HALF, HALF, N)
    X, Z = np.meshgrid(x, x)
    r = np.hypot(X, Z)
    c = np.divide(Z, r, out=np.zeros_like(r), where=r > 0)
    return r, c


def density(excited, phi, r, c):
    pg, pe = ORB["1s"](r, c), ORB[excited](r, c)
    return 0.5 * (pg ** 2 + pe ** 2) + pg * pe * np.cos(phi)


def make_figure(excited, outfile, vmax):
    r, c = grid()
    z_te = transition_z(excited)
    norm = PowerNorm(gamma=GAMMA, vmin=0, vmax=vmax)
    fig, axes = plt.subplots(1, 4, figsize=(16, 4.6), facecolor="white")
    for ax, (phi, label) in zip(axes, PHASES):
        ax.imshow(density(excited, phi, r, c), origin="lower",
                  extent=[-HALF, HALF, -HALF, HALF], cmap="magma", norm=norm,
                  interpolation="bilinear")
        ax.set_title(label, fontsize=18, pad=8)
        ax.set_xticks([]); ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(False)
        # dipole moment d = -e<z>: arrow from the nucleus, common magnification
        dz = -z_te * np.cos(phi) * ARROW_MAG      # in a0 units on the plot, sign from -e
        if abs(dz) > 0.05:
            ax.annotate("", xy=(0, dz), xytext=(0, 0),
                        arrowprops=dict(arrowstyle="-|>", color=ARROW_COLOR, lw=3,
                                        mutation_scale=22, shrinkA=0, shrinkB=0))
        ax.plot(0, 0, "o", ms=4, mfc="none", mec="white", mew=1)     # nucleus
        ax.plot([-HALF + 2, -HALF + 12], [-HALF + 2.5, -HALF + 2.5], color="white", lw=3)
        ax.text(-HALF + 7, -HALF + 3.8, r"10 $a_0$", color="white",
                ha="center", va="bottom", fontsize=11)
    plt.tight_layout()
    fig.savefig(outfile, dpi=200, facecolor="white")
    plt.close(fig)
    print(f"saved {outfile}   <1s|z|{excited}> = {z_te:+.4f} a0")


if __name__ == "__main__":
    # one common brightness scale for all three figures (largest density in any frame)
    r, c = grid()
    vmax = max(density(e, p, r, c).max() for e in ("2p", "3p", "2s") for p, _ in PHASES)
    print(f"common vmax = {vmax:.4f}")

    make_figure("2p", "superposition_1s_2p.png", vmax)
    make_figure("3p", "superposition_1s_3p.png", vmax)
    make_figure("2s", "superposition_1s_2s.png", vmax)

    # check: time-averaged density is just the mean of the two stationary densities
    avg = np.mean([density("2p", p, r, c) for p in np.linspace(0, 2 * np.pi, 8, endpoint=False)], axis=0)
    ref = 0.5 * (ORB["1s"](r, c) ** 2 + ORB["2p"](r, c) ** 2)
    print(f"max |time-average - mean of stationary densities| = {np.abs(avg - ref).max():.2e}")
