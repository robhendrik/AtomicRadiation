"""
Animated GIFs of the coherent 1s + excited-state superpositions (2p, 3p, 2s): one full oscillation each.

    |Psi|^2 = (psi_g^2 + psi_e^2)/2 + psi_g psi_e cos(phi),   phi = (E_e - E_g) t / hbar

Same look and normalization as superposition_pair.py: magma, +-6 a0 window, dotted z = 0 line,
2 a0 scale bar, PowerNorm with display gamma GAMMA, and vmaxes adjusted across the three
states as in hydrogen_static_clouds.py:
    vmax_i = peak_i * (peak_i / max_peak)**(-GAMMA_NORM)
where peak_i is the largest density that state reaches during the oscillation.
GAMMA_NORM = 0 -> every GIF on its own scale, larger -> closer to one common scale.

Below each cloud: the dipole curve d_z(phi) = -e <z>, same vertical range in every GIF, with a
marker that follows the phase. The phase phi is printed in the top-left corner of every frame
(exactly "0", "pi/2", "pi", "3pi/2" on the four key frames used in the montage).

Usage: python superposition_gif.py
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import PowerNorm
from PIL import Image
import os
os.chdir(os.path.dirname(__file__))
print(f"Current working directory: {os.getcwd()}")

STATES = ["2p", "3p", "2s"]
HALF = 6.0           # half-width of the window, in Bohr radii (same for all GIFs)
BAR = 2.0            # scale bar length, a0
N = 700              # grid points per axis
FRAMES = 48          # frames per oscillation period
FRAME_MS = 50        # milliseconds per frame
GAMMAS = [0.6, 0.5, 0.35]          # display gamma of PowerNorm
GAMMA_NORM = 0.3     # exponent for adjusting vmaxes (same recipe and value as the other scripts)
MARKER_COLOR = "#4DD0E1"


def R10(r): return 2.0 * np.exp(-r)
def R20(r): return (1 / (2 * np.sqrt(2))) * (2 - r) * np.exp(-r / 2)
def R21(r): return (1 / (2 * np.sqrt(6))) * r * np.exp(-r / 2)
def R31(r): return (8 / (27 * np.sqrt(6))) * r * (1 - r / 6) * np.exp(-r / 3)
Y00 = 1 / np.sqrt(4 * np.pi)
def Y10(c): return np.sqrt(3 / (4 * np.pi)) * c

ORB = {"1s": lambda r, c: R10(r) * Y00, "2s": lambda r, c: R20(r) * Y00,
       "2p": lambda r, c: R21(r) * Y10(c), "3p": lambda r, c: R31(r) * Y10(c)}


def phase_label(k):
    """Label for frame k: exact text on the four key frames, decimals (in units of pi) otherwise."""
    exact = {0: "φ = 0", FRAMES // 4: "φ = π/2", FRAMES // 2: "φ = π", 3 * FRAMES // 4: "φ = 3π/2"}
    return exact.get(k, f"φ = {2 * k / FRAMES:.2f}π")


def transition_z(excited):
    """<1s| z |excited> in a0, by 3D quadrature."""
    r = np.linspace(0, 80, 8001)
    c = np.linspace(-1, 1, 2001)
    Rg, Cg = np.meshgrid(r, c, indexing="ij")
    f = ORB["1s"](Rg, Cg) * ORB[excited](Rg, Cg) * (Rg * Cg) * Rg ** 2
    return np.trapezoid(np.trapezoid(f, c, axis=1) * 2 * np.pi, r)


# --- grid (same for all states) ------------------------------------------------
x = np.linspace(-HALF, HALF, N)
X, Z = np.meshgrid(x, x)
r = np.hypot(X, Z)
c = np.divide(Z, r, out=np.zeros_like(r), where=r > 0)

# --- first pass: A and I for each state, and the peak density over the whole oscillation ---
prepared = {}
for excited in STATES:
    pg, pe = ORB["1s"](r, c), ORB[excited](r, c)
    A, I = 0.5 * (pg ** 2 + pe ** 2), pg * pe
    prepared[excited] = (A, I, (A + np.abs(I)).max())      # max over phi of A + I cos(phi)

peaks = [prepared[e][2] for e in STATES]
vmaxes = {e: p * (p / max(peaks)) ** (-GAMMA_NORM) for e, p in zip(STATES, peaks)}
for e, p in zip(STATES, peaks):
    print(f"1s-{e}: peak {p:.4f}  vmax {vmaxes[e]:.4f}")


def make_gif(excited):
    A, I, peak = prepared[excited]
    vmax = vmaxes[excited]
    z_te = transition_z(excited)
    norm = PowerNorm(GAMMAS[STATES.index(excited)], vmin=0, vmax=vmax)

    FIG_W, FIG_H = 6.0, 7.2
    fig = plt.figure(figsize=(FIG_W, FIG_H), dpi=80, facecolor="white")
    ax = fig.add_axes([0.2 / FIG_W, 1.0 / FIG_H, 5.6 / FIG_W, 5.6 / FIG_H])
    im = ax.imshow(A + I, origin="lower", extent=[-HALF, HALF, -HALF, HALF],
                   cmap="magma", norm=norm, interpolation="bilinear")
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    fig.text(0.5, 0.955, f"1s–{excited}", ha="center", va="center", fontsize=20)
    ax.axhline(0, color="white", lw=1, ls=(0, (1, 3)), alpha=0.7)            # the z = 0 line
    ax.plot([-HALF + 0.6, -HALF + 0.6 + BAR], [-HALF + 0.7] * 2, color="white", lw=3)
    ax.text(-HALF + 0.6 + BAR / 2, -HALF + 1.0, rf"{BAR:g} $a_0$", color="white",
            ha="center", va="bottom", fontsize=11)

    phase_txt = ax.text(-HALF + 0.4, HALF - 0.4, phase_label(0), color="white", ha="left", va="top",
                        fontsize=16)

    # dipole curve with moving marker (same y-range for every state: 0.8 e a0)
    strip = fig.add_axes([0.16, 0.025, 0.72, 0.085])
    ph = np.linspace(0, 2 * np.pi, 400)
    strip.plot(ph, -z_te * np.cos(ph), color="#444444", lw=1.5)
    strip.axhline(0, color="#999999", lw=0.8)
    strip.set_xlim(-0.25, 2 * np.pi + 0.25); strip.set_ylim(-0.8, 0.8)
    strip.set_xticks([]); strip.set_yticks([])
    for s in strip.spines.values():
        s.set_visible(False)
    strip.set_ylabel(r"$d_z$", rotation=0, labelpad=18, va="center", fontsize=15)
    dot, = strip.plot([0], [-z_te], "o", color=MARKER_COLOR, mec="black", ms=9, clip_on=False)

    frames = []
    for k in range(FRAMES):
        phi = 2 * np.pi * k / FRAMES
        im.set_data(A + I * np.cos(phi))
        dot.set_data([phi], [-z_te * np.cos(phi)])
        phase_txt.set_text(phase_label(k))
        fig.canvas.draw()
        frames.append(Image.fromarray(np.asarray(fig.canvas.buffer_rgba())[..., :3].copy()))
    plt.close(fig)

    out = f"superposition_1s_{excited}.gif"
    pal = [f.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
           for f in frames]
    pal[0].save(out, save_all=True, append_images=pal[1:], duration=FRAME_MS, loop=0, disposal=2)
    print(f"saved {out}: {FRAMES} frames, {FRAME_MS} ms each, <1s|z|{excited}> = {z_te:+.4f} a0")

    # montage of four key frames (phi = 0, pi/2, pi, 3pi/2) for a quick look
    w, h = frames[0].size
    sheet = Image.new("RGB", (w * 4, h), "white")
    for j, kf in enumerate([0, FRAMES // 4, FRAMES // 2, 3 * FRAMES // 4]):
        sheet.paste(frames[kf], (j * w, 0))
    sheet.save(f"superposition_1s_{excited}_montage.png")


for e in STATES:
    make_gif(e)
