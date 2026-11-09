
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
"""Atomic Radiation — Post 4, Figure 1.

Inertial and uniformly accelerated worldlines in the (z, ct) plane.
The past and future Rindler horizons of an eternally uniformly
accelerated observer are ct = -z and ct = z (z >= 0).

Run: python post4_figure1_spacetime.py
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# Units are chosen such that c=1. a is proper acceleration.
a = 1.0
TAU_LIMIT = 2.6
TIME_LIMIT = 3.35
Z_LIMIT = 4.55
OUTPUT = Path(__file__).with_name("post4_figure1_spacetime.png")

# Restrict the accelerated trajectory to the visible interval.
tau = np.linspace(-TAU_LIMIT, TAU_LIMIT, 1200)
ct = np.sinh(a * tau) / a
z = np.cosh(a * tau) / a
visible = np.abs(ct) <= TIME_LIMIT

# Figure style
plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'savefig.facecolor': 'white',})
fig, ax = plt.subplots(figsize=(8.1, 7.3), dpi=160)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# Right Rindler wedge: z > |ct|.
y = np.linspace(-TIME_LIMIT, TIME_LIMIT, 500)
ax.fill_betweenx(y, np.abs(y), Z_LIMIT, facecolor='#dceeee', alpha=0.60, zorder=0)

# Only the rightgoing null boundaries form the accelerated observer's horizons.
# Negative ct branch is the past horizon; positive ct branch is the future horizon.
z_h = np.linspace(0, TIME_LIMIT, 500)
ax.plot(z_h, z_h, color='#b07c4b', lw=2.0, ls=(0, (5, 4)), zorder=2)
ax.plot(z_h, -z_h, color='#b07c4b', lw=2.0, ls=(0, (5, 4)), zorder=2)

# Inertial atom, at z=0.
ax.plot([0, 0], [-TIME_LIMIT, TIME_LIMIT], color='#5679a6', lw=3.0, zorder=3)

# Accelerated atom, z^2 - (ct)^2 = 1/a^2.
ax.plot(z[visible], ct[visible], color='#c75e4b', lw=3.8, zorder=4)

# Mark the event of instantaneous rest at t=0.
z0 = 1 / a
ax.scatter([z0], [0], s=58, color='#c75e4b', edgecolor='white', linewidth=1.0, zorder=6)
ax.annotate(r'$z=c^2/a$ at $t=0$', xy=(z0, 0), xytext=(1.35, -0.47),
            fontsize=10, color='#7a3f35',
            arrowprops=dict(arrowstyle='-', color='#7a3f35', lw=0.8))

# Clear, separate labels within the plotting area.
ax.annotate('Inertial atom', xy=(0, 1.55), xytext=(-1.38, 2.03),
            fontsize=11, color='#315780',
            arrowprops=dict(arrowstyle='->', color='#315780', lw=1.0))
ax.annotate('Accelerated atom', xy=(np.sqrt(1+1.35**2), 1.35), xytext=(2.35, 1.12),
            fontsize=11, color='#9b4435',
            arrowprops=dict(arrowstyle='->', color='#9b4435', lw=1.0))
ax.annotate('Future horizon', xy=(2.65, 2.65), xytext=(1.28, 3.13),
            fontsize=11, color='#8b643c',
            arrowprops=dict(arrowstyle='->', color='#8b643c', lw=1.0))
ax.annotate('Past horizon', xy=(2.75, -2.75), xytext=(1.46, -3.15),
            fontsize=11, color='#8b643c',
            arrowprops=dict(arrowstyle='->', color='#8b643c', lw=1.0))
ax.text(3.62, 0.10, 'Right Rindler\nwedge', ha='center', va='center',
        color='#447b7a', fontsize=10)

ax.axhline(0, color='#6f7880', lw=0.9, alpha=0.55, zorder=1)
ax.set_xlim(-1.65, Z_LIMIT)
ax.set_ylim(-TIME_LIMIT, TIME_LIMIT)
ax.set_aspect('equal', adjustable='box')
ax.set_xlabel(r'Position $z$  (units of $c^2/a$)', labelpad=10)
ax.set_ylabel(r'Time $ct$  (units of $c^2/a$)', labelpad=10)
ax.set_title('Straight and Hyperbolic Worldlines', fontsize=17, pad=21)
ax.tick_params(colors='#4b5563')
fig.tight_layout(pad=1.8)
fig.savefig(OUTPUT, dpi=240, bbox_inches='tight')
print(f'Saved {OUTPUT}')
plt.show()