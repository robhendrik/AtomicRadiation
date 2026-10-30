"""Figure 1: Vacuum Rabi oscillations with aligned atom/field snapshots.

Requires numpy, matplotlib. Run: python figure1_vacuum_rabi.py
Outputs PNG and SVG. All main styling is configurable below.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import os
os.chdir(os.path.dirname(__file__))
print(f"Current working directory: {os.getcwd()}")
# -------------------- CONFIG --------------------
OUTPUT = 'figure1_vacuum_rabi'
DARK = True
FIGSIZE = (12, 7.3)
DPI = 240
G = 1.0  # Coupling in arbitrary inverse-time units
N_PERIODS = 2  # Probability period T = pi / G
ATOM_COLOR = '#ffc35c'
FIELD_COLOR = '#55c8f4'
BG = '#0b1220' if DARK else '#ffffff'
FG = '#e1e9f5' if DARK else '#182437'
MUTED = '#95a7bd' if DARK else '#607086'
GRID = '#304259' if DARK else '#dae1e9'
SHOW_STATE_LABELS = True
SHOW_VERTICAL_GUIDES = True
# ------------------------------------------------

plt.rcParams.update({
    'font.family': 'DejaVu Sans', 'font.size': 11,
    'text.color': FG, 'axes.labelcolor': FG,
    'xtick.color': MUTED, 'ytick.color': MUTED,
    'axes.edgecolor': MUTED, 'savefig.facecolor': BG,
})

T = np.pi / G  # period of the populations, not of the state amplitudes
# Five extrema over two complete probability oscillations.
t_snap = np.arange(5) * T / 2
t = np.linspace(0, N_PERIODS * T, 1400)
p_atom = np.cos(G * t)**2
p_field = np.sin(G * t)**2

fig = plt.figure(figsize=FIGSIZE, facecolor=BG)
gs = GridSpec(2, 1, figure=fig, height_ratios=[1.25, 1.35],
              left=.09, right=.965, top=.88, bottom=.115, hspace=.19)
ax_top = fig.add_subplot(gs[0])
ax = fig.add_subplot(gs[1], sharex=ax_top)
for a in (ax_top, ax):
    a.set_facecolor(BG)

# Top row: five snapshots with atomic two-level diagrams and a field symbol.
ax_top.set_xlim(-.08*T, 2.08*T)
ax_top.set_ylim(0, 1)
ax_top.axis('off')
for i, ti in enumerate(t_snap):
    excited = (i % 2 == 0)
    # Energy levels, dot on occupied level.
    halfwidth = .105*T
    y_e, y_g = .78, .57
    ax_top.plot([ti-halfwidth, ti+halfwidth], [y_e, y_e],
                color=MUTED, lw=2.5, solid_capstyle='round')
    ax_top.plot([ti-halfwidth, ti+halfwidth], [y_g, y_g],
                color=MUTED, lw=2.5, solid_capstyle='round')
    ax_top.scatter([ti], [y_e if excited else y_g], s=110,
                   color=ATOM_COLOR, edgecolors=BG, linewidths=.8, zorder=5)
    if i == 0:
        ax_top.text(ti-halfwidth-.035*T, y_e, 'e', va='center', ha='right',
                    fontsize=10, color=MUTED)
        ax_top.text(ti-halfwidth-.035*T, y_g, 'g', va='center', ha='right',
                    fontsize=10, color=MUTED)

    # Field: flat baseline for vacuum; wave packet icon for one photon.
    xw = np.linspace(ti-.12*T, ti+.12*T, 160)
    y_base = .34
    if excited:
        yw = np.full_like(xw, y_base)
    else:
        u = (xw-ti)/(.12*T)
        yw = y_base + .07*np.exp(-3*u*u)*np.sin(5*np.pi*u)
    ax_top.plot(xw, yw, color=FIELD_COLOR, lw=2.1)
    if SHOW_STATE_LABELS:
        state = r'$|e,0\rangle$' if excited else r'$|g,1\rangle$'
        ax_top.text(ti, .13, state, color=FG, fontsize=12,
                    ha='center', va='center')

ax_top.text(0, .99, 'ATOM', color=ATOM_COLOR, weight='bold', fontsize=10, va='top')
ax_top.text(0, .45, 'FIELD MODE', color=FIELD_COLOR, weight='bold', fontsize=10, va='top')

# Bottom: complementary probability oscillations.
ax.plot(t, p_atom, color=ATOM_COLOR, lw=2.8, label=r'Atom excited   $P_e=\cos^2(gt)$')
ax.plot(t, p_field, color=FIELD_COLOR, lw=2.8, label=r'One photon   $P_{g,1}=\sin^2(gt)$')
if SHOW_VERTICAL_GUIDES:
    for ti in t_snap:
        ax.axvline(ti, color=GRID, lw=.9, linestyle=(0, (3, 5)), zorder=0)
ax.set_ylim(-.07, 1.08)
ax.set_xlim(-.08*T, 2.08*T)
ax.set_yticks([0, .5, 1])
ax.set_ylabel('Probability', labelpad=10)
ax.set_xlabel('Time', labelpad=9)
ax.set_xticks(t_snap)
ax.set_xticklabels(['0', r'$T/2$', r'$T$', r'$3T/2$', r'$2T$'])
ax.spines[['top', 'right']].set_visible(False)
ax.spines[['left', 'bottom']].set_color(GRID)
ax.tick_params(length=0, pad=8)
ax.legend(loc='upper center', bbox_to_anchor=(.5, 1.16),
          ncol=2, frameon=False, fontsize=10, labelcolor=FG)

fig.text(.09, .957, 'VACUUM RABI OSCILLATIONS', fontsize=17,
         color=FG, weight='bold', va='top')
fig.text(.09, .914, 'A single resonant mode allows the excitation to return',
         fontsize=11, color=MUTED, va='top')
fig.text(.965, .035, r'$T=\pi/g$   ·   Wave icon represents mode occupation, not a photon trajectory',
         ha='right', color=MUTED, fontsize=9)


path = f'{OUTPUT}.{'png'}'
fig.savefig(path, dpi=DPI, facecolor=BG)
print('Saved:', path)
plt.show()
