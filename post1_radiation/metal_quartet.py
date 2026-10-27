"""Four metallic surfaces, each enclosing 50% of the probability of the 1s+2p superposition, in a row at
phi = 0, pi/2, pi, 3pi/2 (one full period, left to right). Same faint plane z = 0 through all of them:
the cloud is above it at phi = 0, centred at pi/2, below it at pi, centred again at 3pi/2.
Usage: xvfb-run -a python metal_quartet.py"""
import numpy as np, pyvista as pv, os
from PIL import Image
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(f"Current working directory: {os.getcwd()}")
HALF, N, W, H = 7.0, 220, 1800, 520
LEVEL, BG = 0.5, "#04040c"
PLANE_OPACITY = 0.7
SEP = 5.2                                   # distance between neighbouring blobs (in a0)
PHASES = [0, np.pi/2, np.pi, 3*np.pi/2]
def R10(r): return 2*np.exp(-r)
def R21(r): return r*np.exp(-r/2)/(2*np.sqrt(6))
ax = np.linspace(-HALF, HALF, N)
X, Y, Z = np.meshgrid(ax, ax, ax, indexing="ij")
r = np.sqrt(X**2+Y**2+Z**2); c = np.divide(Z, r, out=np.zeros_like(r), where=r > 0)
pg, pe = R10(r)/np.sqrt(4*np.pi), R21(r)*np.sqrt(3/(4*np.pi))*c
grid = pv.ImageData(dimensions=(N,)*3, spacing=(ax[1]-ax[0],)*3, origin=(-HALF,)*3)

def surface(phi):
    """Surface enclosing LEVEL of the probability at phase phi."""
    D = 0.5*(pg**2+pe**2)+pg*pe*np.cos(phi)
    grid["D"] = D.ravel(order="F")
    flat = np.sort(D.ravel())[::-1]; cum = np.cumsum(flat)/flat.sum()
    level = flat[np.searchsorted(cum, LEVEL)]
    s = grid.contour([level], scalars="D").compute_normals(auto_orient_normals=True)
    print(f"phi = {phi/np.pi:.2f} pi: level/max = {level/D.max():.3f}, z-centre = {s.center[2]:+.2f}")
    return s

# procedural studio environment (soft gradient + two bright strip lights) for metallic reflections
def face(kind, n=256):
    u = np.linspace(-1, 1, n); U, V = np.meshgrid(u, u)
    base = 0.03+0.10*(V*0.5+0.5)
    img = np.stack([base*0.9, base*0.95, base*1.2], -1)
    if kind in ("left", "front"):
        s = np.exp(-((U+0.55)/0.10)**2)*np.exp(-(V/0.9)**4)
        img += s[..., None]*np.array([1.0, 0.85, 0.65])*2.5
    if kind in ("right", "back"):
        s = np.exp(-((U-0.5)/0.07)**2)*np.exp(-(V/0.9)**4)
        img += s[..., None]*np.array([0.45, 0.65, 1.0])*2.0
    if kind == "top":
        img += (np.exp(-(U**2+V**2)/0.1))[..., None]*0.8
    return (np.clip(img, 0, 1)*255).astype(np.uint8)
names = ["right", "left", "top", "bottom", "front", "back"]
tex = pv.Texture([pv.Texture(face(n)).to_image() for n in names])

pl = pv.Plotter(off_screen=True, window_size=(W, H), lighting="none")
pl.set_background(BG)
pl.set_environment_texture(tex)
xs = (np.arange(4)-1.5)*SEP
for phi, x0 in zip(PHASES, xs):
    s = surface(phi); s.points = s.points + np.array([x0, 0, 0])
    pl.add_mesh(s, color="#c9ced6", pbr=True, metallic=1.0, roughness=0.22, smooth_shading=True)
plane = pv.Plane(center=(0, 0, 0), direction=(0, 0, 1), i_size=4*SEP+1.5, j_size=8)
pl.add_mesh(plane, color="#ff8f98", opacity=PLANE_OPACITY, smooth_shading=True)
pl.add_light(pv.Light(position=(-20, -4, 3), focal_point=(0, 0, 0), color="#ffd9a8", intensity=1.2))
pl.add_light(pv.Light(position=(18, 6, 1), focal_point=(0, 0, 0), color="#9cc0ff", intensity=0.8))
pl.camera_position = [(1.0, -27.0, 8.0), (0, 0, 0.0), (0, 0, 1)]; pl.camera.zoom(1.3)
img = pl.screenshot(None, return_img=True, scale=2); pl.close()
Image.fromarray(img).resize((W, H), Image.LANCZOS).save("superposition_3d_metal_quartet_1s_2p.png")
print("saved superposition_3d_metal_quartet_1s_2p.png")
