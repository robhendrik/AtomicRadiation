"""Figure 4: a single atom exchanging excitation with an almost-empty cavity,
after Brune et al. (1996).

Panel A: Bohr-style CARTOON of a Rydberg atom: inner electrons in close orbits, one
         electron far out. Deliberately not physical (the real state is a probability
         cloud); the figure text says so. Radii are not to scale.
Panel B: ONE atom inside the cavity at a time; the next atom is far away.
Panel C: schematic theory curve (damped vacuum Rabi oscillation). NOT measured data;
         the time axis is in arbitrary units.

Run:     python figure4_brune.py
Output:  figure4_brune.png (PNG only)
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, Rectangle

OUT = Path(__file__).resolve().parent / "figure4_brune.png"

BG = "#081522"; PANEL = "#0b1c2d"; FG = "#e7edf5"; MUTED = "#9badbf"
BLUE = "#50b6fa"; AMBER = "#ffbb65"; RED = "#f47986"

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11, "savefig.facecolor": BG})
fig = plt.figure(figsize=(16, 5.9), facecolor=BG)
gs = fig.add_gridspec(1, 3, width_ratios=[1.05, 1.4, 1.45], left=.035, right=.975,
                      bottom=.10, top=.87, wspace=.095)
axs = [fig.add_subplot(gs[0, i]) for i in range(3)]
for ax in axs:
    ax.set_facecolor(PANEL)
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_color("#34506a"); sp.set_linewidth(1)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
fig.suptitle("A single atom exchanges excitation with an almost-empty cavity",
             color=FG, fontsize=19, fontweight="bold", y=.96)

# ---------------- A: cartoon of a Rydberg atom (core electrons close in, one far out) ----------------
ax = axs[0]
ax.text(.05, .94, "A   Rydberg atom", color=FG, fontsize=14, fontweight="bold", va="top")
ins = ax.inset_axes([.05, .20, .90, .66])
ins.set_xlim(-1, 1); ins.set_ylim(-1, 1); ins.set_aspect("equal"); ins.axis("off")
for radius in (.13, .21, .30, .40, .90):
    ins.add_patch(Circle((0, 0), radius, fill=False, ec=BLUE, lw=1.2 if radius < .5 else 1.8, alpha=.85))
for j, rad in enumerate((.13, .21, .30, .40)):
    cnt = (2, 8, 8, 18)[j]
    for k in range(cnt):
        th = 2 * np.pi * k / cnt + j * .2
        ins.add_patch(Circle((rad * np.cos(th), rad * np.sin(th)), .022, color=RED, zorder=5))
ins.add_patch(Circle((0, 0), .075, color=AMBER, zorder=6))
ins.text(0, 0, "Rb", color=BG, fontsize=9, ha="center", va="center", fontweight="bold", zorder=7)
ins.add_patch(Circle((.90 * np.cos(.7), .90 * np.sin(.7)), .045, color=RED, zorder=7))
ax.text(.5, .125, "Highly excited electron, far from the core", color=MUTED, ha="center", fontsize=10.5)
ax.text(.5, .075, "(cartoon, not to scale; the real state is a", color=MUTED, ha="center", fontsize=9)
ax.text(.5, .035, "probability cloud, not an orbit)", color=MUTED, ha="center", fontsize=9)

# ---------------- B: one atom at a time ----------------
ax = axs[1]
ax.text(.04, .94, "B   The experiment", color=FG, fontsize=14, fontweight="bold", va="top")
ax.text(.53, .825, "Superconducting microwave cavity", color=MUTED, ha="center", fontsize=10)
for cy in (.35, .69):
    ax.add_patch(Ellipse((.53, cy), .36, .08, fc="#728aa1", ec="#c4d6e6", lw=1.5, alpha=.85))
ax.add_patch(Rectangle((.35, .35), .36, .34, fc=BLUE, alpha=.07, ec=BLUE, lw=1.1))
for rr in (.11, .17, .24):
    ax.add_patch(Ellipse((.53, .52), rr, rr * 1.05, fill=False, ec=BLUE, lw=1, alpha=.45))
ax.plot([.04, .96], [.52, .52], color=FG, alpha=.35, lw=1)

# the one atom that is inside the cavity now
ax.add_patch(Circle((.53, .52), .026, fc=AMBER, ec="#ffdb9c", lw=1, zorder=9))
ax.add_patch(Circle((.53, .52), .045, fc=AMBER, alpha=.18, ec="none", zorder=8))
ax.annotate("one atom inside\nthe cavity", xy=(.56, .545), xytext=(.80, .75), color=AMBER, fontsize=9.5,
            ha="center", va="center", zorder=10,
            arrowprops=dict(arrowstyle="-", color=AMBER, lw=.9, alpha=.8))
# the next atom: far away, well outside the cavity
ax.add_patch(Circle((.065, .52), .014, fc=AMBER, ec="#ffdb9c", lw=.5, alpha=.45, zorder=8))
ax.text(.10, .575, "next atom,\nfar behind", color=MUTED, fontsize=8.5, ha="center", va="bottom")
# entrance and exit
ax.add_patch(FancyArrowPatch((.12, .43), (.31, .43), arrowstyle="-|>", mutation_scale=15, color=MUTED, lw=1.4))
ax.text(.215, .385, "prepared in |e⟩", color=AMBER, fontsize=10.5, ha="center", va="top")
ax.add_patch(Rectangle((.80, .47), .09, .10, fc=BLUE, alpha=.55, ec=FG, lw=1))
ax.text(.845, .60, "detector", color=BLUE, fontsize=10.5, ha="center")
ax.text(.845, .43, "finds |g⟩ or |e⟩", color=BLUE, fontsize=9.5, ha="center", va="top")
ax.add_patch(FancyArrowPatch((.72, .52), (.79, .52), arrowstyle="-|>", mutation_scale=12, color=MUTED, lw=1.2))
ax.text(.53, .265, "Interaction time  t", color=FG, fontsize=11, ha="center")
ax.add_patch(FancyArrowPatch((.35, .31), (.71, .31), arrowstyle="<->", mutation_scale=12, color=FG, lw=1))
ax.text(.5, .135, "Atoms arrive one at a time; t is set by the atom’s velocity", color=MUTED, ha="center", fontsize=10.5)
ax.text(.5, .085, "Each atom is measured once, after it has left the cavity", color=MUTED, ha="center", fontsize=10.5)

# ---------------- C: schematic theory curve ----------------
ax = axs[2]
ax.text(.04, .94, "C   Vacuum Rabi oscillations", color=FG, fontsize=14, fontweight="bold", va="top")
plot = ax.inset_axes([.18, .27, .76, .53]); plot.set_facecolor(PANEL)
T = 17.2
tau = np.linspace(0, 90, 900)
prob = .5 * (1 - np.exp(-tau / 40) * np.cos(2 * np.pi * tau / T))
plot.plot(tau, prob, color=AMBER, lw=2.6, zorder=3)
plot.axhline(.5, color=MUTED, lw=.8, ls=(0, (4, 4)), alpha=.5)
plot.set_xlim(0, 90); plot.set_ylim(-.05, 1.0)
plot.set_xticks([]); plot.set_yticks([0, .5, 1]); plot.set_yticklabels(["0", "0.5", "1"])
plot.tick_params(colors=FG, labelsize=9, length=4)
plot.spines["top"].set_visible(False); plot.spines["right"].set_visible(False)
plot.spines["left"].set_color(MUTED); plot.spines["bottom"].set_color(MUTED)
plot.set_xlabel("Interaction time  t  (arbitrary units)", color=FG, fontsize=10, labelpad=6)
plot.set_ylabel("Probability of detecting |g⟩", color=FG, fontsize=10)
ax.text(.56, .085, "Note: Curve is schematic - not the actual measured data.",
        color='grey', fontsize=8.5, fontweight="bold", ha="center",
        bbox=dict(boxstyle="round,pad=0.35", fc="#1a2433", ec='grey', lw=1))

fig.savefig(OUT, dpi=210, bbox_inches="tight")
plt.close(fig)
print(f"Saved {OUT}")
