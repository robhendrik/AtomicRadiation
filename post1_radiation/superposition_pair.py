"""
Two-panel (phi = 0 and phi = pi) figures of 1s + excited-state superpositions.

|Psi|^2 = (psi_g^2 + psi_e^2)/2 + psi_g psi_e cos(phi)

Brightness: gamma-compressed PowerNorm per figure, with the vmaxes adjusted as in
hydrogen_static_clouds.py: vmax_i = peak_i * (peak_i / max_peak)**(-GAMMA_NORM), where peak_i is the
largest density in the two frames of figure i. GAMMA_NORM = 0 -> every figure on its own scale,
larger -> closer to one common scale. Dotted line = z = 0.

Usage: python superposition_pair.py
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import PowerNorm
import os
os.chdir(os.path.dirname(__file__))
print(f"Current working directory: {os.getcwd()}")
N = 900


def R10(r): return 2.0 * np.exp(-r)
def R20(r): return (1 / (2 * np.sqrt(2))) * (2 - r) * np.exp(-r / 2)
def R21(r): return (1 / (2 * np.sqrt(6))) * r * np.exp(-r / 2)
def R31(r): return (8 / (27 * np.sqrt(6))) * r * (1 - r / 6) * np.exp(-r / 3)
Y00 = 1 / np.sqrt(4 * np.pi)
def Y10(c): return np.sqrt(3 / (4 * np.pi)) * c

ORB = {"1s": lambda r, c: R10(r) * Y00, "2s": lambda r, c: R20(r) * Y00,
       "2p": lambda r, c: R21(r) * Y10(c), "3p": lambda r, c: R31(r) * Y10(c)}

GAMMA_NORM = 0.3   # exponent for adjusting vmaxes to enhance visibility of diffuse clouds
                   # (same recipe and value as hydrogen_static_clouds.py)

# (excited state, title, half-width a0, gamma, scale-bar length a0)
CASES = [("2p", "1s–2p", 6.0, 0.6, 2.0),
         ("3p", "1s–3p", 6.0, 0.6, 2.0),
         ("2s", "1s–2s", 6.0, 0.6, 2.0)]

# First pass: density function of every case and its peak over the two frames shown
prepared = []
for excited, title, HALF, gamma, bar in CASES:
    x = np.linspace(-HALF, HALF, N)
    X, Z = np.meshgrid(x, x)
    r = np.hypot(X, Z)
    c = np.divide(Z, r, out=np.zeros_like(r), where=r > 0)
    pg, pe = ORB["1s"](r, c), ORB[excited](r, c)
    D = lambda phi, pg=pg, pe=pe: 0.5 * (pg ** 2 + pe ** 2) + pg * pe * np.cos(phi)
    prepared.append((D, max(D(0).max(), D(np.pi).max())))

# Same normalization as the static figure: the brightest figure keeps vmax = its peak,
# fainter figures get vmax = peak * (peak / max_peak)**(-GAMMA_NORM), i.e. a partly shared scale
peaks = [p for _, p in prepared]
vmaxes = [v * (v / max(peaks)) ** (-GAMMA_NORM) for v in peaks]

# Second pass: draw
for (excited, title, HALF, gamma, bar), (D, peak), vmax in zip(CASES, prepared, vmaxes):
    norm = PowerNorm(gamma, vmin=0, vmax=vmax)

    fig, axes = plt.subplots(1, 2, figsize=(10, 5.9), facecolor="white")
    for ax, (phi, label) in zip(axes, [(0, r"$\phi=0$"), (np.pi, r"$\phi=\pi$")]):
        ax.imshow(D(phi), origin="lower", extent=[-HALF, HALF, -HALF, HALF],
                  cmap="magma", norm=norm, interpolation="bilinear")
        ax.set_title(label, fontsize=18, pad=8)
        ax.set_xticks([]); ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(False)
        ax.axhline(0, color="white", lw=1, ls=(0, (1, 3)), alpha=0.7)
        #ax.plot([0], [0], "+", color="white", ms=10)
        k = HALF / 6.0
        ax.plot([-HALF + 0.6 * k, -HALF + 0.6 * k + bar], [-HALF + 0.7 * k] * 2, color="white", lw=3)
        ax.text(-HALF + 0.6 * k + bar / 2, -HALF + 1.0 * k, rf"{bar:g} $a_0$", color="white",
                ha="center", va="bottom", fontsize=11)
    fig.suptitle(title, fontsize=20, y=0.985)
    plt.tight_layout(rect=(0, 0, 1, 0.95))
    out = f"superposition_pair_1s_{excited}.png"
    fig.savefig(out, dpi=160, facecolor="white")
    plt.close(fig)
    print(f"saved {out}   window ±{HALF:g} a0, gamma {gamma}, peak {peak:.4f}, vmax {vmax:.4f}")
