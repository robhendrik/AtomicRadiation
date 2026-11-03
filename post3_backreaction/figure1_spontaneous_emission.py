from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

OUTPUT = Path(__file__).with_name('figure1_spontaneous_emission.png')
BG = '#050816'
FG = '#e8eefc'
LEVEL_COLOR = '#f4c542'
ATOM_COLOR = '#8bd3ff'
PHOTON_COLOR = '#ff9966'
FIGSIZE = (12, 5)
DPI = 220
Y_G, Y_E = 0.28, 0.74


def setup_ax(ax):
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.set_facecolor(BG)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)


def draw_level(ax, y, label, state_label):
    ax.plot([0.28, 0.72], [y, y], lw=4, color=LEVEL_COLOR,
            solid_capstyle='round')
    ax.text(0.18, y, label, color=FG, fontsize=14, va='center', ha='right')
    ax.text(0.76, y, state_label, color=ATOM_COLOR,
            fontsize=16, va='center', ha='left')


def draw_wiggly_arrow(ax, x0, y0, x1, y1,
                       amplitude=0.014, waves=5, color=PHOTON_COLOR, lw=3,
                       head_length=0.024, head_width=0.025):
    """Sine wave smoothly entering a straight, custom triangular arrowhead.

    Coordinates (including arrowhead size) use axes data units.
    """
    delta = np.array([x1 - x0, y1 - y0], dtype=float)
    length = np.linalg.norm(delta)
    if length <= head_length:
        raise ValueError('Arrow too short for chosen arrowhead')
    tangent = delta / length
    normal = np.array([-tangent[1], tangent[0]])
    tail = np.array([x0, y0])

    # Sine reaches exactly zero at arrowhead base; cosine derivative is
    # reduced smoothly near endpoint to avoid a visible angled junction.
    wave_length = length - head_length
    u = np.linspace(0, 1, 500)
    envelope = np.minimum(1.0, (1.0 - u) / 0.13)
    ripple = amplitude * np.sin(2 * np.pi * waves * u) * envelope
    coords = tail + (u * wave_length)[:, None] * tangent + ripple[:, None] * normal
    ax.plot(coords[:, 0], coords[:, 1], lw=lw, color=color,
            solid_capstyle='round', zorder=5)

    base = tail + wave_length * tangent
    tip = np.array([x1, y1])
    triangle = np.vstack([tip,
                          base + 0.5 * head_width * normal,
                          base - 0.5 * head_width * normal])
    ax.add_patch(Polygon(triangle, closed=True, facecolor=color,
                         edgecolor=color, zorder=6))


def draw_transition(ax, upward):
    start, end = ((Y_G + 0.01, Y_E - 0.01) if upward
                  else (Y_E - 0.01, Y_G + 0.01))
    ax.annotate('', xy=(0.50, end), xytext=(0.50, start),
                arrowprops=dict(arrowstyle='-|>', color=ATOM_COLOR,
                                lw=2.8, mutation_scale=16))


def draw_panel_absorption(ax):
    setup_ax(ax)
    draw_level(ax, Y_E, 'Excited state', r'$|e\rangle$')
    draw_level(ax, Y_G, 'Ground state', r'$|g\rangle$')
    draw_transition(ax, upward=True)
    draw_wiggly_arrow(ax, 0.18, 0.49, 0.46, 0.49)
    ax.text(0.50, 0.93, 'Photon absorption', color=FG,
            fontsize=16, ha='center', va='center')


def draw_panel_emission(ax):
    setup_ax(ax)
    draw_level(ax, Y_E, 'Excited state', r'$|e\rangle$')
    draw_level(ax, Y_G, 'Ground state', r'$|g\rangle$')
    draw_transition(ax, upward=False)
    draw_wiggly_arrow(ax, 0.54, 0.49, 0.84, 0.49)
    ax.text(0.50, 0.93, 'Photon emission', color=FG,
            fontsize=16, ha='center', va='center')


if __name__ == '__main__':
    fig, axes = plt.subplots(1, 2, figsize=FIGSIZE, dpi=DPI)
    fig.patch.set_facecolor(BG)
    draw_panel_absorption(axes[0])
    draw_panel_emission(axes[1])
    fig.subplots_adjust(left=0.03, right=0.97, top=0.92,
                        bottom=0.08, wspace=0.18)
    fig.savefig(OUTPUT, dpi=DPI, facecolor=BG, bbox_inches='tight')
    print(f'Saved: {OUTPUT.resolve()}')
    plt.show()
