import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path
# ============================================================
# SETTINGS
# ============================================================

OUTPUT =  Path(__file__).with_name("figure3_balance_ground_state.png")

BG = "#050816"
FG = "#dfe7f5"
ZERO_COLOR = "#6c7a92"

VAC_COLOR = "#55c7ff"     # Vacuum fluctuations
RAD_COLOR = "#f3c74b"     # Radiation reaction
TOTAL_COLOR = "#ff9966"   # Optional total marker/text accent

FIGSIZE = (12, 5.6)
DPI = 220

# Values in units of (1/2) ħω0Γ
# Excited: vacuum fluctuations = -1, radiation reaction = -1, total = -2
# Ground:  vacuum fluctuations = +1, radiation reaction = -1, total = 0
excited_vals = {
    "Vacuum fluctuations": -1,
    "Radiation reaction": -1,
    "Total": -2,
}

ground_vals = {
    "Vacuum fluctuations": +1,
    "Radiation reaction": -1,
    "Total": 0,
}

# ============================================================
# HELPERS
# ============================================================

def setup_ax(ax, title):
    ax.set_facecolor(BG)
    ax.set_xlim(-2.35, 1.65)
    ax.set_ylim(-0.35, 2.15)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    # zero line
    ax.axvline(0, color=ZERO_COLOR, lw=1.4, alpha=0.85)

    # panel title
    ax.text(
        0.5, 1.05, title,
        transform=ax.transAxes,
        ha="center", va="bottom",
        color=FG, fontsize=18
    )

    # zero label
    ax.text(
        0, -0.22, "0",
        ha="center", va="top",
        color=FG, fontsize=11
    )

def draw_bar(ax, y, value, color, label, value_text):
    """
    Draw a single horizontal bar centered on zero line.
    Positive value extends right, negative value extends left.
    """
    h = 0.28
    if value >= 0:
        x0 = 0
        width = value
    else:
        x0 = value
        width = -value

    rect = Rectangle((x0, y - h/2), width, h, facecolor=color, edgecolor="none")
    ax.add_patch(rect)

    # label at left
    ax.text(
        -2.15, y, label,
        ha="right", va="center",
        color=FG, fontsize=12
    )

    # numeric annotation
    if value > 0:
        ax.text(
            value + 0.08, y, value_text,
            ha="left", va="center",
            color=FG, fontsize=12
        )
    elif value < 0:
        ax.text(
            value - 0.08, y, value_text,
            ha="right", va="center",
            color=FG, fontsize=12
        )
    else:
        ax.text(
            0.08, y, value_text,
            ha="left", va="center",
            color=FG, fontsize=12
        )

def draw_total_text(ax, total_value, explanation):
    """
    Add compact summary text near bottom of panel.
    """
    if total_value < 0:
        total_str = r"$-\hbar\omega_0\Gamma$"
    elif total_value > 0:
        total_str = r"$+\hbar\omega_0\Gamma$"
    else:
        total_str = r"$0$"

    ax.text(
        -2.15, 0.15,
        "Total:",
        ha="left", va="center",
        color=FG, fontsize=13, fontweight="bold"
    )
    ax.text(
        -1.25, 0.15,
        total_str,
        ha="left", va="center",
        color=TOTAL_COLOR, fontsize=13
    )
    ax.text(
        -2.15, -0.08,
        explanation,
        ha="left", va="top",
        color=FG, fontsize=11
    )

def draw_panel(ax, title, vals, explanation):
    setup_ax(ax, title)

    # y positions
    y_vac = 1.45
    y_rad = 0.95

    draw_bar(
        ax, y_vac,
        vals["Vacuum fluctuations"],
        VAC_COLOR,
        "Vacuum fluctuations",
        r"$+\frac{1}{2}\hbar\omega_0\Gamma$" if vals["Vacuum fluctuations"] > 0
        else r"$-\frac{1}{2}\hbar\omega_0\Gamma$"
    )

    draw_bar(
        ax, y_rad,
        vals["Radiation reaction"],
        RAD_COLOR,
        "Radiation reaction",
        r"$+\frac{1}{2}\hbar\omega_0\Gamma$" if vals["Radiation reaction"] > 0
        else r"$-\frac{1}{2}\hbar\omega_0\Gamma$"
    )

    draw_total_text(ax, vals["Total"], explanation)

# ============================================================
# MAIN
# ============================================================

fig, axes = plt.subplots(1, 2, figsize=FIGSIZE, dpi=DPI)
fig.patch.set_facecolor(BG)

draw_panel(
    axes[0],
    "Excited state $|e\\rangle$",
    excited_vals,
    "The two contributions reinforce each other."
)

draw_panel(
    axes[1],
    "Ground state $|g\\rangle$",
    ground_vals,
    "The two contributions cancel exactly."
)

plt.subplots_adjust(left=0.05, right=0.98, top=0.90, bottom=0.14, wspace=0.28)
plt.savefig(OUTPUT, dpi=DPI, facecolor=BG, bbox_inches="tight")
plt.show()