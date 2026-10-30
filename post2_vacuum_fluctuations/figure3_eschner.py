"""Figure 3: a single Ba+ ion in front of a mirror, after Eschner et al. (2001).

Panel C shows ILLUSTRATIVE sinusoids, NOT digitized experimental data.
The modulation sizes are the reported "visibilities", V = (Imax - Imin)/(Imax + Imin):
    493 nm (blue): 47 %   -> signal = 1 +/- 0.47 about its mean
    650 nm (red):  0.9 %  -> signal = 1 +/- 0.009 about its mean (1.8 % peak to peak)
Source for both numbers: Eschner et al., ICOLS'01 proceedings, Fig. 5 caption
("The visibility of the modulation is 47 % (top) and 0.9 % (bottom)").
The mirror reflects 493 nm and transmits 650 nm. Fringes repeat every
lambda/2 = 246.5 nm of mirror displacement.

Run:     python figure3_eschner.py
Output:  figure3_eschner.png (PNG only)
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle

OUT = Path(__file__).resolve().parent / "figure3_eschner.png"

BG = "#071321"
FG = "#e6edf5"
MUTED = "#a3b4c8"
BLUE = "#48b7ff"
RED = "#ff6879"
AMBER = "#ffbe65"
GRID = "#294057"

V_BLUE, V_RED = 0.47, 0.009          # reported visibilities
FRINGE = 246.5                        # nm, lambda/2 for 493 nm
PHASE0 = 0.3

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 11,
    "figure.facecolor": BG, "axes.facecolor": BG,
    "text.color": FG, "axes.labelcolor": FG,
    "xtick.color": MUTED, "ytick.color": MUTED,
    "axes.edgecolor": GRID, "savefig.facecolor": BG,
})

fig = plt.figure(figsize=(15, 6.4))
gs = GridSpec(1, 3, figure=fig, width_ratios=[0.95, 1.35, 1.4], wspace=0.24,
              left=0.045, right=0.985, top=0.86, bottom=0.20)
ax_a = fig.add_subplot(gs[0, 0])
ax_b = fig.add_subplot(gs[0, 1])
gsc = GridSpecFromSubplotSpec(2, 1, subplot_spec=gs[0, 2], hspace=0.20)
ax_c1 = fig.add_subplot(gsc[0])
ax_c2 = fig.add_subplot(gsc[1], sharex=ax_c1)

fig.suptitle("A mirror changes how a single atom emits", fontsize=22,
             fontweight="bold", y=0.97)


def arrow(ax, start, end, color, lw=2.7, style="-|>", mutation=17, alpha=1, z=4):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle=style,
                                 mutation_scale=mutation, linewidth=lw,
                                 color=color, alpha=alpha, zorder=z,
                                 shrinkA=0, shrinkB=0))


# ---------------- A: energy levels ----------------
ax_a.set_xlim(0, 10); ax_a.set_ylim(0, 10); ax_a.axis("off")
ax_a.set_title("A   Three-level atom", loc="left", fontsize=14, fontweight="bold", pad=15)
levels = {"P": (5.1, 8.0), "S": (2.2, 2.0), "D": (7.8, 3.15)}
for key, (x, y) in levels.items():
    ax_a.plot([x - 1.25, x + 1.25], [y, y], color=FG, lw=2.3, solid_capstyle="round")
    ax_a.add_patch(Circle((x, y), .13, color=AMBER if key == "P" else (BLUE if key == "S" else RED), zorder=5))
ax_a.text(7.0, 8.2, r"$P_{1/2}$", color=FG, fontsize=15)
ax_a.text(0.1, 1.25, r"$S_{1/2}$", color=FG, fontsize=15)
ax_a.text(8.0, 2.25, r"$D_{3/2}$", color=FG, fontsize=15)
arrow(ax_a, (4.55, 7.65), (2.35, 2.38), BLUE)
arrow(ax_a, (5.7, 7.65), (7.6, 3.48), RED)
ax_a.text(1.1, 5.3, "493 nm", color=BLUE, fontsize=13, fontweight="bold")
ax_a.text(7.0, 5.65, "650 nm", color=RED, fontsize=13, fontweight="bold")
ax_a.text(5.05, 0.45, "Continuous excitation", color=MUTED, fontsize=11, ha="center")

# ---------------- B: simplified optical setup ----------------
ax_b.set_xlim(0, 12); ax_b.set_ylim(0, 10); ax_b.axis("off")
ax_b.set_title("B   Single ion and movable mirror", loc="left", fontsize=14, fontweight="bold", pad=15)
ion = (4.1, 5.3)
Y_BLUE, Y_RED = 5.5, 5.1            # parallel horizontal beams (pumps and fluorescence)
mirror_x = 10.65
ax_b.add_patch(Circle(ion, 0.22, facecolor=AMBER, edgecolor="#ffe3ae", lw=1.3, zorder=8))
ax_b.text(ion[0] + 0.4, 4.55, r"Ba$^+$", ha="left", va="center", fontsize=13, fontweight="bold")
# Pump beams: horizontal and parallel
arrow(ax_b, (0.4, Y_BLUE), (3.85, Y_BLUE), BLUE, lw=2.3, alpha=.85)
arrow(ax_b, (0.4, Y_RED), (3.85, Y_RED), RED, lw=2.3, alpha=.85)
ax_b.text(0.3, Y_BLUE + 0.35, "493 nm pump", color=BLUE, fontsize=10)
ax_b.text(0.3, Y_RED - 0.5, "650 nm pump", color=RED, fontsize=10)
# Mirror (reflects blue, transmits red)
ax_b.add_patch(Rectangle((mirror_x - .11, 4.05), .22, 2.55,
                         facecolor="#b7c5d4", edgecolor=FG, linewidth=1.3, zorder=7))
ax_b.text(mirror_x, 7.18, "Movable mirror", ha="center", fontsize=11)
ax_b.text(mirror_x, 6.77, "reflects blue", color=BLUE, ha="center", fontsize=10)
ax_b.text(mirror_x, 3.56, "transmits red", color=RED, ha="center", fontsize=10)
# Blue light goes to the mirror and back: one double-headed arrow
arrow(ax_b, (4.4, Y_BLUE), (mirror_x - .14, Y_BLUE), BLUE, lw=2.5, style="<|-|>")
# Red light is parallel to the blue and passes straight through the mirror
arrow(ax_b, (4.4, Y_RED), (11.8, Y_RED), RED, lw=2.3, z=9)
# Detectors: one above, one below, both exactly vertically aligned with the ion
arrow(ax_b, (ion[0], Y_BLUE + 0.05), (ion[0], 7.2), BLUE, lw=2.5)
arrow(ax_b, (ion[0], Y_RED - 0.05), (ion[0], 1.8), RED, lw=2.5)
ax_b.add_patch(Rectangle((ion[0] - .35, 7.25), .7, .4, facecolor=BLUE,
                         edgecolor=FG, linewidth=1, alpha=.85))
ax_b.text(ion[0], 7.95, "493 nm", color=BLUE, ha="center", fontsize=11)
ax_b.add_patch(Rectangle((ion[0] - .35, 1.3), .7, .4, facecolor=RED,
                         edgecolor=FG, linewidth=1, alpha=.85))
ax_b.text(ion[0], .86, "650 nm", color=RED, ha="center", fontsize=11)
ax_b.text(ion[0], .28, "Fluorescence detectors", ha="center", color=MUTED, fontsize=10)
ax_b.annotate("", xy=(4.4, 8.5), xytext=(10.55, 8.5),
              arrowprops={"arrowstyle": "<->", "color": MUTED, "lw": 1.4})
ax_b.text(7.5, 8.72, "25 cm", ha="center", color=MUTED, fontsize=12)
arrow(ax_b, (10.2, 8.02), (11.2, 8.02), FG, lw=1.4, style="<->", mutation=11)
ax_b.text(10.7, 7.63, r"$\Delta z$", ha="center", fontsize=11)

# ---------------- C: illustrative anti-correlated signals ----------------
x = np.linspace(0, 600, 900)
phase = 2 * np.pi * x / FRINGE + PHASE0
blue = 1.0 + V_BLUE * np.cos(phase)
red = 1.0 - V_RED * np.cos(phase)           # same phase, opposite sign

for ax in (ax_c1, ax_c2):
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", color=GRID, alpha=.4, lw=.8)
    ax.set_xlim(0, 600)
    ax.tick_params(length=4)

ax_c1.plot(x, blue, color=BLUE, lw=2.8)
ax_c2.plot(x, red, color=RED, lw=2.8)
# Headroom above each curve, so the labels never touch the data.
ax_c1.set_ylim(.40, 1.80)
ax_c2.set_ylim(0.90, 1.10)
ax_c1.set_yticks([0.5, 1.0, 1.5])
ax_c2.set_yticks([0.9, 1.0, 1.1])
ax_c1.set_ylabel("Relative 493 nm signal", color=BLUE, fontsize=10)
ax_c2.set_ylabel("Relative 650 nm signal", color=RED, fontsize=10)
ax_c1.set_title("C   Fluorescence signals", loc="left", fontsize=14, fontweight="bold", pad=15)
ax_c2.set_xlabel("Mirror displacement (nm)", fontsize=11)
plt.setp(ax_c1.get_xticklabels(), visible=False)

# Dashed guide: a blue maximum coincides with a red minimum (anticorrelation).
peak_x = (2 * np.pi - PHASE0) * FRINGE / (2 * np.pi)        # first blue maximum after 0
for ax in (ax_c1, ax_c2):
    ax.axvline(peak_x, color=FG, ls="--", lw=1, alpha=.55)
ax_c1.text(peak_x - 8, 1.67, "blue maximum", color=FG, fontsize=9, alpha=.85, va="center", ha="right")
ax_c2.text(peak_x - 8, 1.085, "= red minimum", color=FG, fontsize=9, alpha=.85, va="center", ha="right")

ax_c1.text(0.988, 0.93, "493 nm: visibility 47 %", transform=ax_c1.transAxes,
           color=BLUE, ha="right", va="top", fontsize=10.5, fontweight="bold")
ax_c2.text(0.988, 0.93, "650 nm: visibility 0.9 %", transform=ax_c2.transAxes,
           color=RED, ha="right", va="top", fontsize=10.5, fontweight="bold")
ax_c2.text(0.988, 0.07, "\u00b10.9 % (1.8 % peak to peak)",
           transform=ax_c2.transAxes, color=MUTED, ha="right", va="bottom", fontsize=9)

# Prominent "not data" banner, well clear of every axis label.
fig.text(0.5, 0.045,
         "ILLUSTRATIVE  —  sinusoids drawn with the reported modulation depths; not experimental data",
         ha="center", va="center", color='grey', fontsize=10.5, fontweight="bold",
         bbox=dict(boxstyle="round,pad=0.5", fc="#1a2433", ec='grey', lw=1.2))

fig.savefig(OUT, dpi=220)
plt.close(fig)
print(f"Saved {OUT}")
