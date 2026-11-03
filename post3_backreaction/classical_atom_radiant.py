"""
classical_atom_radiant.py

Stylized Python rendering of a classical atom spiraling inward:
- glowing orange spiral
- bright metallic-looking nucleus
- bright glowing electron
- soft fading blue comet tail
- high-resolution rendering + downsampling for smooth spheres

Install:
    pip install numpy pillow scipy

Run:
    python classical_atom_radiant.py
"""

from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw
from scipy.ndimage import gaussian_filter

# ============================================================
# SETTINGS
# ============================================================

OUTPUT = Path(__file__).with_name("classical_atom_radiant.png")

# Final output size
W, H = 1600, 900

# Internal supersampled render size
SUPERSAMPLE = 3
W2, H2 = W * SUPERSAMPLE, H * SUPERSAMPLE

# Background
BG = np.array([4, 2, 18], dtype=np.float32) / 255.0

# Spiral geometry
TURNS = 2.7
R_OUTER = 1.0
R_INNER = 0.12
PHASE = 0.25
CENTER = np.array([0.53 * W2, 0.53 * H2], dtype=np.float32)
SPIRAL_SCALE = 0.37 * min(W2, H2)

# Electron position along spiral
ELECTRON_FRACTION = 0.17  # 0 = outer end, 1 = near nucleus

# Tail
TAIL_FRACTION = 0.17      # fraction of whole spiral used as tail
TAIL_COLOR = np.array([40, 185, 255], dtype=np.float32) / 255.0
TAIL_GLOW_COLOR = np.array([20, 110, 255], dtype=np.float32) / 255.0

# Colors
ORBIT_CORE = np.array([1.00, 0.72, 0.42], dtype=np.float32)
ORBIT_GLOW = np.array([1.00, 0.52, 0.28], dtype=np.float32)

NUCLEUS_BASE = (205, 188, 160)
ELECTRON_BASE = (155, 220, 255)

# Sphere sizes (internal render pixels)
NUCLEUS_R = 19 * SUPERSAMPLE
ELECTRON_R = 13 * SUPERSAMPLE

# Optional global bloom
ENABLE_GLOBAL_BLOOM = True
GLOBAL_BLOOM_SIGMA = 11.0
GLOBAL_BLOOM_STRENGTH = 0.42

# ============================================================
# UTILS
# ============================================================

def clamp01(x):
    return np.clip(x, 0.0, 1.0)

def alpha_blend_patch(base_patch, color_rgb, alpha):
    """
    Alpha-blend a solid color onto an RGB patch.
    base_patch: (h,w,3) float in [0,1]
    color_rgb: (3,) float in [0,1]
    alpha: (h,w) float in [0,1]
    """
    a = alpha[..., None]
    base_patch[:] = color_rgb[None, None, :] * a + base_patch * (1.0 - a)

def add_glow_patch(base_patch, color_rgb, intensity):
    """
    Additively add glow to an RGB patch.
    intensity: (h,w) float
    """
    base_patch[:] = clamp01(base_patch + color_rgb[None, None, :] * intensity[..., None])

def draw_soft_glow(img, cx, cy, radius, color, alpha=0.25):
    """
    Add a soft gaussian-like glow centered at (cx,cy).
    """
    h, w = img.shape[:2]
    r = int(max(2, radius * 3.2))
    x0 = max(0, int(cx - r))
    x1 = min(w, int(cx + r + 1))
    y0 = max(0, int(cy - r))
    y1 = min(h, int(cy + r + 1))

    yy, xx = np.mgrid[y0:y1, x0:x1]
    dx = xx - cx
    dy = yy - cy
    rr2 = dx * dx + dy * dy

    sigma2 = radius * radius
    glow = np.exp(-rr2 / (2.0 * sigma2))
    intensity = alpha * glow

    add_glow_patch(img[y0:y1, x0:x1], np.array(color, dtype=np.float32) / 255.0, intensity)

def draw_lit_sphere(
    img,
    cx,
    cy,
    radius,
    base_color=(220, 190, 120),
    light_dir=(-0.65, -0.75, 1.0),
    ambient=0.23,
    diffuse_strength=0.95,
    specular_strength=1.0,
    shininess=55,
    rim_strength=0.18,
):
    """
    Draw a lit sphere into an RGB float image.
    """
    h, w = img.shape[:2]
    r = int(np.ceil(radius))
    x0 = max(0, int(cx - r - 2))
    x1 = min(w, int(cx + r + 3))
    y0 = max(0, int(cy - r - 2))
    y1 = min(h, int(cy + r + 3))

    yy, xx = np.mgrid[y0:y1, x0:x1]
    x = (xx - cx) / radius
    y = (yy - cy) / radius
    rsq = x * x + y * y

    mask = rsq <= 1.0
    z = np.zeros_like(x, dtype=np.float32)
    z[mask] = np.sqrt(1.0 - rsq[mask])

    nx, ny, nz = x, y, z

    L = np.array(light_dir, dtype=np.float32)
    L /= np.linalg.norm(L)

    V = np.array([0.0, 0.0, 1.0], dtype=np.float32)
    Hvec = L + V
    Hvec /= np.linalg.norm(Hvec)

    ndotl = np.clip(nx * L[0] + ny * L[1] + nz * L[2], 0.0, 1.0)
    ndoth = np.clip(nx * Hvec[0] + ny * Hvec[1] + nz * Hvec[2], 0.0, 1.0)
    spec = np.power(ndoth, shininess)
    rim = np.power(1.0 - np.clip(nz, 0.0, 1.0), 2.2)

    base = np.array(base_color, dtype=np.float32) / 255.0

    color = (
        ambient * base
        + diffuse_strength * ndotl[..., None] * base
        + specular_strength * spec[..., None] * np.array([1.0, 1.0, 1.0], dtype=np.float32)
        + rim_strength * rim[..., None] * np.array([1.0, 0.97, 0.90], dtype=np.float32)
    )

    # Slight warm/cool center boost for richer appearance
    center_boost = np.exp(-rsq / 0.16)
    color += 0.10 * center_boost[..., None] * base
    color = clamp01(color)

    # Slight antialiasing near edge
    alpha = np.zeros_like(x, dtype=np.float32)
    edge_softness = 0.04
    alpha[mask] = 1.0
    near_edge = (rsq > (1.0 - edge_softness)) & (rsq <= 1.0)
    alpha[near_edge] = (1.0 - rsq[near_edge]) / edge_softness
    alpha = clamp01(alpha)

    patch = img[y0:y1, x0:x1]
    # per-pixel alpha blend using precomputed colors
    a = alpha[..., None]
    patch[:] = color * a + patch * (1.0 - a)

def draw_masked_glow(img, mask, color, sigma, strength):
    """
    Blur a mask and add it as colored glow.
    """
    glow = gaussian_filter(mask.astype(np.float32), sigma=sigma)
    mx = glow.max()
    if mx > 1e-8:
        glow /= mx
    add_glow_patch(img, color, glow * strength)

def draw_masked_core(img, mask, color, alpha=1.0):
    """
    Blend a sharp colored mask.
    """
    alpha_mask = np.clip(mask.astype(np.float32) * alpha, 0.0, 1.0)
    alpha_blend_patch(img, color, alpha_mask)

def add_gaussian_blob(field, cx, cy, sigma, amplitude):
    """
    Add a gaussian blob into a single-channel field.
    """
    h, w = field.shape
    r = int(max(2, sigma * 3.2))
    x0 = max(0, int(cx - r))
    x1 = min(w, int(cx + r + 1))
    y0 = max(0, int(cy - r))
    y1 = min(h, int(cy + r + 1))

    yy, xx = np.mgrid[y0:y1, x0:x1]
    dx = xx - cx
    dy = yy - cy
    g = np.exp(-(dx * dx + dy * dy) / (2.0 * sigma * sigma))
    field[y0:y1, x0:x1] += amplitude * g

# ============================================================
# SPIRAL PATH
# ============================================================

n = 1800
theta = np.linspace(0.0, 2.0 * np.pi * TURNS, n)

# Radius decreases inward
radius = R_OUTER + (R_INNER - R_OUTER) * (theta / theta[-1])

# Spiral in image coordinates
x = CENTER[0] + SPIRAL_SCALE * radius * np.cos(theta + PHASE)
y = CENTER[1] + SPIRAL_SCALE * radius * np.sin(theta + PHASE)

points = np.column_stack([x, y])

# electron near outer region
e_idx = int(np.clip(ELECTRON_FRACTION, 0.0, 1.0) * (n - 1))
ex, ey = points[e_idx]

# tail extends backward from electron toward older orbit points
tail_len = max(12, int(TAIL_FRACTION * n))
tail_start = max(0, e_idx - tail_len)
tail_points = points[tail_start : e_idx + 1]

# nucleus at center
nx, ny = CENTER

# ============================================================
# CANVAS
# ============================================================

img = np.ones((H2, W2, 3), dtype=np.float32)
img[:] = BG[None, None, :]

# ============================================================
# ORBIT: core + glow
# ============================================================

# Draw core orbit mask with PIL
orbit_mask_img = Image.new("L", (W2, H2), 0)
draw = ImageDraw.Draw(orbit_mask_img)

orbit_pts = [tuple(p) for p in points]
draw.line(orbit_pts, fill=255, width=3 * SUPERSAMPLE)

orbit_mask = np.array(orbit_mask_img, dtype=np.float32) / 255.0

# Warm orbit glow
draw_masked_glow(img, orbit_mask, ORBIT_GLOW, sigma=10.0 * SUPERSAMPLE / 3.0, strength=0.18)
draw_masked_glow(img, orbit_mask, ORBIT_GLOW, sigma=4.0 * SUPERSAMPLE / 3.0, strength=0.12)

# Orbit core
#draw_masked_core(img, orbit_mask, ORBIT_CORE, alpha=0.95)

# Slight bright inner line
orbit_inner = gaussian_filter(orbit_mask, sigma=1.0)
orbit_inner /= max(orbit_inner.max(), 1e-8)
#draw_masked_core(img, orbit_inner, np.array([1.0, 0.83, 0.57], dtype=np.float32), alpha=0.22)

# ============================================================
# TAIL: fading blue comet
# ============================================================

tail_glow = np.zeros((H2, W2), dtype=np.float32)
tail_core = np.zeros((H2, W2), dtype=np.float32)

m = len(tail_points)
for i, (tx, ty) in enumerate(tail_points):
    # 0 = oldest tail point, 1 = near electron
    s = i / max(1, m - 1)

    # strong near electron, fades toward far end
    amp = 0.08 + 0.85 * (s ** 1.6)
    sigma_glow = (10 + 22 * s) * SUPERSAMPLE / 3.0
    sigma_core = (3 + 7 * s) * SUPERSAMPLE / 3.0

    add_gaussian_blob(tail_glow, tx, ty, sigma_glow, amp)
    add_gaussian_blob(tail_core, tx, ty, sigma_core, 0.22 + 0.95 * (s ** 1.7))

# normalize and softly taper
if tail_glow.max() > 1e-8:
    tail_glow /= tail_glow.max()
if tail_core.max() > 1e-8:
    tail_core /= tail_core.max()

tail_glow = gaussian_filter(tail_glow, sigma=1.2)
tail_core = gaussian_filter(tail_core, sigma=0.7)

add_glow_patch(img, TAIL_GLOW_COLOR, 0.30 * tail_glow)
add_glow_patch(img, TAIL_COLOR, 0.40 * tail_glow)
alpha_blend_patch(img, np.array([0.32, 0.84, 1.0], dtype=np.float32), 0.68 * tail_core)

# ============================================================
# NUCLEUS: soft halos + lit sphere
# ============================================================

draw_soft_glow(img, nx, ny, radius=58 * SUPERSAMPLE / 3.0, color=(255, 115, 45), alpha=0.14)
draw_soft_glow(img, nx, ny, radius=30 * SUPERSAMPLE / 3.0, color=(255, 185, 95), alpha=0.18)
draw_soft_glow(img, nx, ny, radius=16 * SUPERSAMPLE / 3.0, color=(255, 230, 170), alpha=0.16)

draw_lit_sphere(
    img,
    nx,
    ny,
    radius=NUCLEUS_R,
    base_color=NUCLEUS_BASE,
    light_dir=(-0.72, -0.80, 1.0),
    ambient=0.24,
    diffuse_strength=0.95,
    specular_strength=1.15,
    shininess=68,
    rim_strength=0.20,
)

# extra hot highlight
draw_soft_glow(img, nx - 0.26 * NUCLEUS_R, ny - 0.28 * NUCLEUS_R, radius=3.3 * SUPERSAMPLE, color=(255, 255, 245), alpha=0.12)

# ============================================================
# ELECTRON: glow + lit sphere
# ============================================================

draw_soft_glow(img, ex, ey, radius=42 * SUPERSAMPLE / 3.0, color=(20, 115, 255), alpha=0.16)
draw_soft_glow(img, ex, ey, radius=21 * SUPERSAMPLE / 3.0, color=(90, 220, 255), alpha=0.22)
draw_soft_glow(img, ex, ey, radius=10 * SUPERSAMPLE / 3.0, color=(225, 250, 255), alpha=0.10)

draw_lit_sphere(
    img,
    ex,
    ey,
    radius=ELECTRON_R,
    base_color=ELECTRON_BASE,
    light_dir=(-0.72, -0.80, 1.0),
    ambient=0.24,
    diffuse_strength=0.90,
    specular_strength=1.18,
    shininess=72,
    rim_strength=0.14,
)

# extra bright highlight
draw_soft_glow(img, ex - 0.24 * ELECTRON_R, ey - 0.26 * ELECTRON_R, radius=2.8 * SUPERSAMPLE, color=(255, 255, 255), alpha=0.14)

# ============================================================
# GLOBAL BLOOM
# ============================================================

if ENABLE_GLOBAL_BLOOM:
    # Only bloom bright regions
    bright = np.maximum(img - 0.55, 0.0)
    bloom = gaussian_filter(bright, sigma=(GLOBAL_BLOOM_SIGMA, GLOBAL_BLOOM_SIGMA, 0.0))
    img = clamp01(img + GLOBAL_BLOOM_STRENGTH * bloom)

# ============================================================
# SAVE (downsampled)
# ============================================================

img8 = (clamp01(img) * 255).astype(np.uint8)
im = Image.fromarray(img8, mode="RGB")
im = im.resize((W, H), resample=Image.Resampling.LANCZOS)
im.save(OUTPUT)

print(f"Saved: {OUTPUT.resolve()}")
