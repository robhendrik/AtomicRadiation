from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Post 4 — Figure 3
# Vacuum-fluctuation spectrum seen by inertial and accelerated atoms
#
# We plot the symmetric field spectrum in dimensionless form.
# Using the dimensionless frequency ratio
#
#   x = ω / ω0
#
# and the dimensionless acceleration parameter
#
#   α = a / (c ω0)
#
# the scalar-field spectra become
#
#   S_in(ω) = |ω| / (4π)
#   S_acc(ω) = |ω|/(4π) * coth(π c |ω| / a)
#
# so that, after dividing by ω0/(4π),
#
#   S̃_in(x) = x
#   S̃_acc(x; α) = x * coth(π x / α)
#
# We plot only positive frequencies.
# ============================================================

OUTPUT = Path(__file__).with_name("post4_figure3_spectrum.png")


def coth(z):
    """Numerically stable coth for positive numpy arrays."""
    return 1.0 + 2.0 / np.expm1(2.0 * z)



def spectrum_inertial(x):
    return x



def spectrum_accelerated(x, alpha):
    """Accelerated scalar-field spectrum in dimensionless form."""
    out = np.empty_like(x)
    small = np.isclose(x, 0.0, atol=1e-10)
    out[small] = alpha / np.pi  # x coth(pi x / alpha) -> alpha/pi as x -> 0
    z = np.pi * x[~small] / alpha
    out[~small] = x[~small] * coth(z)
    return out


# ------------------------------------------------------------
# Parameters
# ------------------------------------------------------------
x = np.linspace(0.0, 3.0, 1200)              # x = ω / ω0
alphas = [2.5, 2 * np.pi / np.log(3)]        # second gives a doubling at ω0

# ------------------------------------------------------------
# Plot
# ------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8.2, 5.4))

# Inertial reference
ax.plot(
    x,
    spectrum_inertial(x),
    linewidth=2.6,
    linestyle="--",
    label="Inertial"
)

# Accelerated curves
for alpha in alphas:
    y = spectrum_accelerated(x, alpha)
    ax.plot(
        x,
        y,
        linewidth=2.2,
        label=rf"$a/(c\omega_0) = {alpha:.1f}$"
    )

# Mark ω = ω0  ->  x = 1
ax.axvline(1.0, linewidth=1.4, linestyle=":", color="#6D7B8D")
ax.text(
    1.02, 0.04,
    r"Atomic frequency $\omega_0$",
    transform=ax.get_xaxis_transform(),
    fontsize=11,
    va="bottom"
)

# Labels
ax.set_xlabel(r"Frequency ratio  $\omega/\omega_0$")
ax.set_ylabel(r"Dimensionless fluctuation spectrum  $\tilde S_F(\omega)$")
ax.set_title("Vacuum Fluctuations Sampled by the Atom")

# Limits and cleanup
ax.set_xlim(0.0, 3.0)
ax.set_ylim(0.0, None)
ax.legend(frameon=False, loc="upper left")
ax.grid(False)

plt.tight_layout()
plt.savefig(OUTPUT, dpi=300, bbox_inches="tight")
plt.show()
