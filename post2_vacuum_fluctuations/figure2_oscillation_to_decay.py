"""Figure 2: From oscillation to decay.

One atom, resonantly coupled (RWA, equal couplings g) to
  A: one mode,
  B: N = 11 equally spaced modes (spacing dw),
  C: a dense set of modes (continuum limit) with the same decay rate Gamma.

The excited-state probability is computed exactly by diagonalising the
single-excitation Hamiltonian (atom at 0, modes at detunings k*dw, atom-mode
coupling g). Time is dimensionless: x = Gamma * t, with Gamma = 2*pi*g^2/dw.

Run:      python figure2_oscillation_to_decay.py
Requires: numpy, matplotlib
Outputs:  figure2_oscillation_to_decay.png (and .svg)
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE / "figure2_oscillation_to_decay"
DPI = 220

# ---- colours (same palette as the other figures) ----
BG, PANEL, FG = "#0b1220", "#111e30", "#e3eaf4"
MUTED, GRAY = "#9daec5", "#8493a8"
GOLD, CYAN = "#ffc45b", "#58c8f4"

# ---- model parameters ----
N_B = 11            # modes in panel B
EPS = 0.4           # g / dw in panel B (weak coupling: Gamma ~ dw)
N_C = 801           # modes in panel C
DW_C = 0.05         # mode spacing in panel C, in units of Gamma
X_MAX = 15.0        # time axis, in units of 1/Gamma


def pe_of_t(t, detunings, g):
    """P_e(t) = |<e| exp(-iHt) |e>|^2 for atom + modes (single excitation)."""
    n = len(detunings)
    H = np.zeros((n + 1, n + 1))
    H[0, 1:] = g
    H[1:, 0] = g
    H[np.arange(1, n + 1), np.arange(1, n + 1)] = detunings
    w, V = np.linalg.eigh(H)
    weights = V[0, :] ** 2
    amp = np.exp(-1j * np.outer(t, w)) @ weights
    return np.abs(amp) ** 2


# ---- units: Gamma = 1 for the time axis ----
# Panel B: dw = 1 (own unit), g = EPS*dw, Gamma = 2 pi g^2 / dw.
dw_B = 1.0
g_B = EPS * dw_B
Gamma_B = 2 * np.pi * g_B**2 / dw_B
tr_B = 2 * np.pi / dw_B                      # revival time
x_rev = Gamma_B * tr_B                       # revival time in units of 1/Gamma

x = np.linspace(0, X_MAX, 1500)
t_B = x / Gamma_B
k = np.arange(N_B) - (N_B - 1) / 2
P_B = pe_of_t(t_B, k * dw_B, g_B)

# Panel A: one resonant mode, same g and same time axis
P_A = np.cos(g_B * t_B) ** 2

# Panel C: dense modes with the same Gamma (Gamma = 1)
g_C = np.sqrt(1.0 * DW_C / (2 * np.pi))
kc = np.arange(N_C) - (N_C - 1) / 2
P_C = pe_of_t(x, kc * DW_C, g_C)

# ---- diagnostics ----
i1 = np.argmin(abs(x - 1.0))
i_rev = np.argmin(abs(x - x_rev))
win = (x > x_rev - 1.0) & (x < x_rev + 1.0)
print(f"Gamma_B/dw = {Gamma_B:.3f},   Gamma*t_r = {x_rev:.3f}")
print(f"B: P_e(Gamma t=1) = {P_B[i1]:.3f}   (1/e = {np.exp(-1):.3f})")
print(f"B: revival peak in window = {P_B[win].max():.3f} at x = {x[win][np.argmax(P_B[win])]:.2f}")
print(f"C: P_e(Gamma t=1) = {P_C[i1]:.3f};  max |P_C - exp(-x)| = {np.max(abs(P_C - np.exp(-x))):.3f}")
print(f"C: revival time in x = {2*np.pi/DW_C:.0f}  (beyond the axis: {2*np.pi/DW_C > X_MAX})")

# ---- plotting ----
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 11,
    "text.color": FG, "axes.labelcolor": FG,
    "xtick.color": MUTED, "ytick.color": MUTED, "axes.edgecolor": GRAY,
    "savefig.facecolor": BG, "svg.fonttype": "none",
})

fig, axes = plt.subplots(3, 1, figsize=(11, 10.5), facecolor=BG, sharex=True)
fig.subplots_adjust(left=0.10, right=0.96, top=0.855, bottom=0.115, hspace=0.34)

for ax in axes:
    ax.set_facecolor(PANEL)
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color(GRAY)
    ax.tick_params(length=4, colors=MUTED)
    ax.grid(axis="y", color="white", alpha=0.08, lw=0.8)
    ax.set_axisbelow(True)
    ax.set(xlim=(0, X_MAX), ylim=(0, 1.05))
    ax.set_ylabel("Excited-state\nprobability")
    ax.set_yticks([0, 0.5, 1])

fig.text(0.10, 0.955, "FROM OSCILLATION TO DECAY",
         fontsize=18, weight="bold", color=FG)
fig.text(0.10, 0.924, "An excited atom coupled to one mode, to eleven modes, and to a continuum of modes",
         fontsize=11, color=MUTED)


def panel_title(ax, text):
    ax.set_title(text, loc="left", fontsize=13, color=FG, pad=10, weight="bold")


# A: one mode
axA, axB, axC = axes
panel_title(axA, "A   One mode: the excitation goes out and comes back")
axA.plot(x, P_A, color=GOLD, lw=3)
axA.fill_between(x, P_A, color=GOLD, alpha=0.07)
axA.text(0.985, 0.88, r"$P_e=\cos^2(gt)$", transform=axA.transAxes,
         ha="right", color=GOLD, fontsize=14)

# B: eleven equally spaced modes
panel_title(axB, "B   Eleven equally spaced modes: decay, then revival")
axB.plot(x, np.exp(-x), color=MUTED, lw=1.2, ls=(0, (5, 4)), alpha=0.8)
axB.plot(x, P_B, color=GOLD, lw=3)
axB.fill_between(x, P_B, color=GOLD, alpha=0.07)
axB.axvline(x_rev, color=CYAN, lw=1.2, ls=(0, (4, 4)), alpha=0.9)
axB.text(x_rev - 0.15, 0.80, "emitted amplitude returns\nat $t_r=2\\pi/\\delta\\omega$", color=CYAN, fontsize=11, ha="right", va="top")
axB.text(0.985, 0.88, "dashed: $e^{-\\Gamma t}$", transform=axB.transAxes,
         ha="right", color=MUTED, fontsize=11)

# C: continuum
panel_title(axC, "C   A continuum of modes: no revival, exponential decay")
axC.plot(x, np.exp(-x), color=MUTED, lw=1.2, ls=(0, (5, 4)), alpha=0.8)
axC.plot(x, P_C, color=GOLD, lw=3)
axC.fill_between(x, P_C, color=GOLD, alpha=0.07)
axC.axvline(1, color=MUTED, lw=1, ls=(0, (4, 4)), alpha=0.5)
axC.scatter([1], [np.exp(-1)], color=GOLD, s=36, zorder=5)
axC.annotate(r"$P_e(1/\Gamma)=1/e$", (1, np.exp(-1)), xytext=(2.0, 0.62),
             color=FG, fontsize=12,
             arrowprops=dict(arrowstyle="-", color=MUTED, lw=1))
axC.text(0.985, 0.88, r"$P_e=e^{-\Gamma t}$", transform=axC.transAxes,
         ha="right", color=GOLD, fontsize=14)
axC.set_xlabel(r"Time in units of the decay time,  $\Gamma t$   with   $\Gamma=2\pi g^{2}/\delta\omega$")

fig.text(0.10, 0.040,
         "Toy model: all modes have the same coupling g and are equally spaced by \u03b4\u03c9 (B: 11 modes, g = 0.4 \u03b4\u03c9; "
         "C: 801 modes, same \u0393).\n"
         "A uses the same g as B. Curves are computed, not measured.",
         color=MUTED, fontsize=9, linespacing=1.5)

fig.savefig(f"{OUT}.png", dpi=DPI, facecolor=BG)
#fig.savefig(f"{OUT}.svg", facecolor=BG)
print(f"Saved {OUT}.png")
