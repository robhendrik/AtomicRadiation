"""Post 4 Figure 4 — vacuum fluctuations and radiation reaction.

White-background version to match the other explanatory figures.
Ground / excited energy-change contributions for an inertial atom and an
accelerated atom (illustrative Unruh occupation n_U=0.5).

All bars are normalized by hbar * omega_0 * Gamma, where Gamma is the
inertial spontaneous-emission rate. This is Audretsch's scalar-field
model (long-time, uniformly accelerated detector).
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

OUTPUT = Path(__file__).with_name("post4_figure4_balance.png")

# Light theme matching Figures 1–3 and 5
BG = "white"
FG = "#1E2E46"
MUTED = "#52637A"
ZERO = "#8E9AAD"
DIV = "#D4DCE8"
CYAN = "#55C4F3"
YELLOW = "#F4C94E"
ORANGE = "#D9723F"

N_U = 0.5  # internal parameter: gives a twofold vacuum-fluctuation contribution

# Normalized energy-change rate in units of hbar * omega_0 * Gamma.
# Each tuple: vacuum fluctuations, radiation reaction, total.
PANELS = [
    [(-0.5, -0.5, -1.0), (-(0.5 + N_U), -0.5, -(1.0 + N_U))],
    [(+0.5, -0.5, 0.0), (+(0.5 + N_U), -0.5, +N_U)],
]


def fmt(x):
    if abs(x) < 1e-10:
        return "0"
    return f"{x:+.1f}"


def draw(ax, vf, rr, total):
    ax.set_facecolor(BG)
    ax.set_xlim(-1.88, 1.88)
    ax.set_ylim(-0.42, 1.90)
    ax.axis("off")

    # Same zero line and scale in every panel.
    ax.plot([0, 0], [0.00, 1.72], color=ZERO, lw=1.6, alpha=0.95)
    ax.text(0, -0.09, "0", ha="center", va="top", color=MUTED, fontsize=10)

    # Each bar starts at zero; negative values extend left.
    for y, val, color in [(1.32, vf, CYAN), (0.57, rr, YELLOW)]:
        ax.barh(y, abs(val), left=min(0, val), height=0.27,
                color=color, edgecolor="none", zorder=3)
        if val < 0:
            ax.text(val - 0.09, y, fmt(val), ha="right", va="center",
                    color=FG, fontsize=12)
        else:
            ax.text(val + 0.09, y, fmt(val), ha="left", va="center",
                    color=FG, fontsize=12)

    ax.text(-1.74, -0.22, "Total", ha="left", va="center",
            color=FG, fontsize=14, fontweight="bold")
    ax.text(-0.54, -0.22, fmt(total), ha="left", va="center",
            color=ORANGE, fontsize=17, fontweight="bold")


def main():
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "savefig.facecolor": BG,
        "figure.facecolor": BG,
        "axes.facecolor": BG,
    })

    fig, axes = plt.subplots(2, 2, figsize=(14.8, 8.8), facecolor=BG)
    fig.subplots_adjust(left=0.105, right=0.975, top=0.77, bottom=0.075,
                        wspace=0.14, hspace=0.30)

    # Column and row headings.
    fig.text(0.31, 0.902, "Inertial atom", color=FG, ha="center",
             va="center", fontsize=22)
    fig.text(0.76, 0.902, "Accelerated atom", color=FG, ha="center",
             va="center", fontsize=22)
    fig.text(0.76, 0.860, "Illustrative acceleration", color=MUTED,
             ha="center", va="center", fontsize=12)
    fig.text(0.050, 0.616, r"Excited $|e\rangle$", color=FG,
             ha="center", va="center", rotation=90, fontsize=17)
    fig.text(0.050, 0.253, r"Ground $|g\rangle$", color=FG,
             ha="center", va="center", rotation=90, fontsize=17)

    fig.legend(handles=[Patch(facecolor=CYAN, label="Vacuum fluctuations"),
                        Patch(facecolor=YELLOW, label="Radiation reaction")],
                loc="upper center", bbox_to_anchor=(0.53, 0.826), ncol=2,
                frameon=False, labelcolor=FG, fontsize=13,
                handlelength=1.7, columnspacing=2.5)

    for row in range(2):
        for col in range(2):
            draw(axes[row, col], *PANELS[row][col])

    # Subtle dividing lines separate the four scenarios.
    fig.add_artist(plt.Line2D([0.52, 0.52], [0.072, 0.780],
                              transform=fig.transFigure, lw=1,
                              color=DIV, alpha=1.0))
    fig.add_artist(plt.Line2D([0.100, 0.977], [0.441, 0.441],
                              transform=fig.transFigure, lw=1,
                              color=DIV, alpha=1.0))
    fig.text(0.53, 0.026,
             r"Energy-change rate in units of $\hbar\omega_0\Gamma$",
             color=MUTED, ha="center", va="center", fontsize=12)

    fig.savefig(OUTPUT, dpi=240, facecolor=BG, bbox_inches="tight", pad_inches=0.12)
    print(f"Saved {OUTPUT}")
    plt.show()


if __name__ == "__main__":
    main()
