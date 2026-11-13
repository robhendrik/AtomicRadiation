import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path
# ============================================================
# Figure 2 — The Four Statistical Functions
# Explicit 2x2 graphic:
#
#                    Atom                          Field
# Correlation        C^A(tau,tau')                C^F(x,x')
# Susceptibility     chi^A(tau,tau')              chi^F(x,x')
#
# With short explanatory prose in each box.
# ============================================================

def add_box(ax, x, y, w, h, title, subtitle,
            facecolor="#f4f4f4", edgecolor="black",
            lw=1.5, title_size=22, subtitle_size=11):
    patch = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.018,rounding_size=0.03",
        linewidth=lw,
        edgecolor=edgecolor,
        facecolor=facecolor
    )
    ax.add_patch(patch)

    ax.text(
        x + w/2, y + 0.73*h,
        title,
        ha="center", va="center",
        fontsize=title_size
    )

    ax.text(
        x + w/2, y + 0.31*h,
        subtitle,
        ha="center", va="center",
        fontsize=subtitle_size,
        wrap=True
    )


# -----------------------------
# Figure and axes
# -----------------------------
fig, ax = plt.subplots(figsize=(11, 6.8))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

# -----------------------------
# Layout
# -----------------------------
left_margin = 0.17
box_w = 0.33
box_h = 0.23
gap_x = 0.08
gap_y = 0.11

x_atom  = left_margin
x_field = x_atom + box_w + gap_x

y_top = 0.54
y_bot = y_top - box_h - gap_y

# -----------------------------
# Title
# -----------------------------
ax.text(
    0.5, 0.95,
    "The Four Statistical Functions",
    ha="center", va="center", fontsize=20
)

# -----------------------------
# Column headers
# -----------------------------
ax.text(x_atom + box_w/2,  0.86, "Atom",
        ha="center", va="center", fontsize=17)
ax.text(x_field + box_w/2, 0.86, "Field",
        ha="center", va="center", fontsize=17)

# -----------------------------
# Row headers
# -----------------------------
ax.text(0.07, y_top + box_h/2, "Correlation",
        ha="center", va="center", rotation=90, fontsize=15)

ax.text(0.07, y_bot + box_h/2, "Susceptibility",
        ha="center", va="center", rotation=90, fontsize=15)

# -----------------------------
# Boxes
# -----------------------------
add_box(
    ax, x_atom, y_top, box_w, box_h,
    r"$C^{A}(\tau,\tau')$",
    "How are atomic fluctuations\n"
    "at two different proper times\n"
    r"$\tau$ and $\tau'$ related?",
    facecolor="#f2f2f2"
)

add_box(
    ax, x_field, y_top, box_w, box_h,
    r"$C^{F}(x,x')$",
    "How are field fluctuations\n"
    "at two spacetime points\n"
    r"$x$ and $x'$ related?",
    facecolor="#f2f2f2"   # neutral: reveal the changed function in the text
)

add_box(
    ax, x_atom, y_bot, box_w, box_h,
    r"$\chi^{A}(\tau,\tau')$",
    "How does the atom at proper time\n"
    r"$\tau$ respond to a disturbance" "\n"
    r"at proper time $\tau'$?",
    facecolor="#f2f2f2"
)

add_box(
    ax, x_field, y_bot, box_w, box_h,
    r"$\chi^{F}(x,x')$",
    "How does the field at spacetime point\n"
    r"$x$ respond to a disturbance" "\n"
    r"at spacetime point $x'$?",
    facecolor="#f2f2f2"
)

# -----------------------------
# Optional footnote
# -----------------------------
ax.text(
    0.5, 0.05,
    r"In the atom's evolution, the field functions are evaluated along the trajectory: "
    r"$x=x(\tau)$ and $x'=x(\tau')$.",
    ha="center", va="center", fontsize=11
)

plt.tight_layout()
OUTPUT = Path(__file__).with_name("post4_figure2_four_quantities_explicit.png")
plt.savefig(OUTPUT, dpi=300, bbox_inches="tight")
plt.show()