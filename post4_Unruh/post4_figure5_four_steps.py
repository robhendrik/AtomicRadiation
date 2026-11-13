"""Post 4, Figure 5: four steps from vacuum fluctuations to Unruh temperature.

Run: python post4_figure5_four_steps.py
Dependencies: numpy, matplotlib, scipy (scipy only for physical constants)
All four panels correspond to the SAME proper acceleration.

Panels 1-3 use the symmetric spectrum of a massless scalar field in 3+1D.
Panel 4 is the blackbody energy-density spectrum inferred from the SAME
Bose-Einstein occupation factor; it is not an emitted radiation spectrum.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle
from scipy.constants import c, h, k, hbar, pi

OUTPUT = Path(__file__).with_name("post4_figure5_four_steps.png")
ACCELERATION = 1.0e24  # m/s^2 (chosen for visibility of the optical band)
T_UNRUH = hbar * ACCELERATION / (2 * pi * c * k)

# Frequency ν, not angular frequency ω. x axes in THz; E=hν.
nu_THz = np.linspace(0, 950, 2400)
nu = nu_THz * 1e12
x = h * nu / (k * T_UNRUH)

# Bose occupation (avoid evaluating exactly at ν=0)
n = np.full_like(x, np.nan)
positive = x > 0
n[positive] = 1.0 / np.expm1(x[positive])

# Symmetric scalar vacuum fluctuation spectrum in arbitrary but COMMON units:
# S_in(ν) ∝ ν, S_acc(ν) ∝ ν(1+2n), ΔS(ν) ∝ 2νn.
# Put frequency on a THz scale for neat plotting.
s_in = nu_THz.copy()
s_delta = np.empty_like(nu_THz)
s_delta[positive] = 2 * nu_THz[positive] * n[positive]
# ν -> 0 gives 2 kT/h, expressed in THz.
s_delta[~positive] = 2 * k * T_UNRUH / h / 1e12
s_acc = s_in + s_delta

# Standard blackbody energy density PER UNIT FREQUENCY (spectral radiance
# differs only by a constant factor); normalized to its maximum for plotting.
u_nu = np.zeros_like(nu)
u_nu[positive] = (8 * pi * h / c**3) * nu[positive]**3 * n[positive]
u_norm = u_nu / np.max(u_nu)
nu_peak_THz = nu_THz[np.argmax(u_nu)]

# Optical visible band, 380–750 nm (violet at high frequency).
vis_low = c / (750e-9) / 1e12
vis_high = c / (380e-9) / 1e12

# Colors
INK = '#152235'
MUTED = '#566479'
BLUE = '#3798c6'
AMBER = '#e4a047'
PURPLE = '#8753b5'
TEAL = '#19a49c'
GRID = '#e8edf2'

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.titleweight': 'semibold',
    'axes.labelsize': 10.5,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'savefig.facecolor': 'white',
})
fig, axs = plt.subplots(2, 2, figsize=(12.0, 8.5))
fig.patch.set_facecolor('white')

for ax in axs.flat:
    ax.set_xlim(0, 950)
    ax.set_xticks([0, 200, 400, 600, 800])
    ax.tick_params(colors=MUTED, labelsize=10)
    for spine in ('left', 'bottom'):
        ax.spines[spine].set_color('#a8b3c0')
    ax.grid(axis='y', color=GRID, linewidth=.8)
    ax.set_axisbelow(True)
    ax.set_xlabel('Frequency  ν  (THz)', color=INK)

# 1: Two field spectra and shaded difference
ax = axs[0, 0]
ax.plot(nu_THz, s_in, color=BLUE, lw=2.5, ls='--', label='Inertial')
ax.plot(nu_THz, s_acc, color=AMBER, lw=2.9, label='Accelerated')
ax.fill_between(nu_THz, s_in, s_acc, color=AMBER, alpha=.23, linewidth=0)
ax.set_ylim(0, 1030)
ax.set_ylabel('Fluctuation spectrum (relative units)', color=INK)
ax.set_title('1. Acceleration Changes the Spectrum', loc='left', color=INK, pad=12)
ax.legend(loc='upper left', frameon=False, labelcolor=INK, fontsize=10)

# 2: Difference; this is NOT the integral of the area in panel 1.
ax = axs[0, 1]
ax.plot(nu_THz, s_delta, color=AMBER, lw=2.9)
ax.fill_between(nu_THz, s_delta, color=AMBER, alpha=.15)
ax.set_ylim(0, s_delta[0]*1.15)
ax.set_ylabel('Extra fluctuations  ΔS (relative units)', color=INK)
ax.set_title('2. Isolate the Extra Fluctuations', loc='left', color=INK, pad=12)
# Algebra belongs in the article text and caption, not on the plot.

# 3: Extract Bose occupation; divergent at zero, display a finite y-window
ax = axs[1, 0]
ax.plot(nu_THz[positive], n[positive], color=TEAL, lw=2.9)
ax.set_ylim(0, 3.0)
ax.set_ylabel(r'Occupation per mode  $n_U(\nu)$', color=INK)
ax.set_title('3. Extract the Thermal Occupation', loc='left', color=INK, pad=12)
# Thermal occupation is explained in the article prose.
# ax.text(.04, .07, 'Curve continues upward as ν → 0', transform=ax.transAxes,
#         fontsize=9.5, color=MUTED)

# 4: Actual BB energy density PER UNIT FREQUENCY at this T
ax = axs[1, 1]
# Physical visible band, lightly shaded. Rainbow strip follows frequency order:
# red at low ν (long wavelengths), violet at high ν.
ax.axvspan(vis_low, vis_high, color='#7e83bd', alpha=.075, zorder=0)
ax.plot(nu_THz, u_norm, color=PURPLE, lw=3)
ax.fill_between(nu_THz, u_norm, color=PURPLE, alpha=.09)
ax.set_ylim(0, 1.17)
ax.set_ylabel('Blackbody energy density (normalized)', color=INK)
ax.set_title('4. Equivalent Blackbody Spectrum', loc='left', color=INK, pad=12)
ax.plot([nu_peak_THz], [1], 'o', color=PURPLE, ms=5)
ax.annotate(f'Peak: {nu_peak_THz:.0f} THz', xy=(nu_peak_THz, 1),
            xytext=(nu_peak_THz+85, 1.075),
            arrowprops={'arrowstyle':'-', 'color':MUTED, 'lw':1},
            fontsize=10, color=INK)

# Rainbow band drawn near bottom of panel 4, true visible frequencies.
vis_cmap = LinearSegmentedColormap.from_list('visible',
                ['#d43a46', '#e98e35', '#ebcf55', '#69b66d', '#37a1d4', '#4d65bc', '#8051aa'])
rainbow = np.linspace(0, 1, 512)[None, :]
ax.imshow(rainbow, extent=[vis_low, vis_high, 0.035, 0.085],
          aspect='auto', origin='lower', cmap=vis_cmap, interpolation='bicubic', zorder=4)
ax.text((vis_low+vis_high)/2, 0.115, 'Visible light', color=INK,
        ha='center', fontsize=10)

fig.suptitle('From Accelerated Vacuum Fluctuations to a Thermal Spectrum',
             fontsize=16, fontweight='semibold', color=INK, y=.99)
fig.text(.5, .945,
         rf'One proper acceleration: $a=10^{{24}}\,\mathrm{{m/s^2}}$'
         rf'     |     Unruh temperature: $T_U={T_UNRUH:,.0f}\,\mathrm{{K}}$',
         ha='center', fontsize=11.5, color=MUTED)
fig.text(.5, .018,
         'Panels 1–3: scalar-field fluctuations seen by the accelerated atom. '
         'Panel 4: equivalent thermal energy distribution, not emitted radiation.',
         ha='center', color=MUTED, fontsize=9.4)
fig.subplots_adjust(left=.087, right=.975, bottom=.105, top=.875, wspace=.28, hspace=.44)
plt.savefig(OUTPUT, dpi=240, bbox_inches='tight', facecolor='white')
plt.close(fig)
print(f'Generated {OUTPUT}\nT={T_UNRUH:.2f} K, peak={nu_peak_THz:.1f} THz, visible={vis_low:.1f}-{vis_high:.1f} THz')
