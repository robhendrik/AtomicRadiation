"""50%-of-max density isosurface of 1s+2p (phi=0) with a metallic finish and side lighting.
Usage: xvfb-run -a python metal_surface.py"""
import numpy as np, pyvista as pv, os
from PIL import Image
os.chdir(os.path.dirname(os.path.abspath(__file__)))
HALF, N, W, H = 7.0, 220, 1200, 630
LEVEL, BG = 0.5, "#04040c"
PLANE_OPACITY = 0.7
def R10(r): return 2*np.exp(-r)
def R21(r): return r*np.exp(-r/2)/(2*np.sqrt(6))
ax = np.linspace(-HALF, HALF, N)
X, Y, Z = np.meshgrid(ax, ax, ax, indexing="ij")
r = np.sqrt(X**2+Y**2+Z**2); c = np.divide(Z, r, out=np.zeros_like(r), where=r > 0)
pg, pe = R10(r)/np.sqrt(4*np.pi), R21(r)*np.sqrt(3/(4*np.pi))*c
D = 0.5*(pg**2+pe**2)+pg*pe
grid = pv.ImageData(dimensions=(N,)*3, spacing=(ax[1]-ax[0],)*3, origin=(-HALF,)*3)
grid["D"] = D.ravel(order="F")
flat = np.sort(D.ravel())[::-1]; cum = np.cumsum(flat)/flat.sum()
level = flat[np.searchsorted(cum, LEVEL)]          # surface enclosing LEVEL of the probability
print("level / max =", level/D.max())
surf = grid.contour([level], scalars="D").compute_normals(auto_orient_normals=True)
print("surface:", surf.n_points, "points, bounds", np.round(surf.bounds, 2))

# procedural studio environment (soft gradient + two bright strip lights) for metallic reflections
def face(kind, n=256):
    u = np.linspace(-1, 1, n); U, V = np.meshgrid(u, u)
    base = 0.03+0.10*(V*0.5+0.5)                              # dark studio, slightly brighter on top
    img = np.stack([base*0.9, base*0.95, base*1.2], -1)
    if kind in ("left", "front"):                             # tall strip light on the left side
        s = np.exp(-((U+0.55)/0.10)**2)*np.exp(-(V/0.9)**4)
        img += s[..., None]*np.array([1.0, 0.85, 0.65])*2.5
    if kind in ("right", "back"):                             # cool rim light
        s = np.exp(-((U-0.5)/0.07)**2)*np.exp(-(V/0.9)**4)
        img += s[..., None]*np.array([0.45, 0.65, 1.0])*2.0
    if kind == "top":
        img += (np.exp(-(U**2+V**2)/0.1))[..., None]*0.8
    return (np.clip(img, 0, 1)*255).astype(np.uint8)
names = ["right", "left", "top", "bottom", "front", "back"]
cube = pv.Texture([pv.numpy_to_texture(face(n)).to_image() if False else pv.Texture(face(n)).to_image() for n in names]) if False else None
cube = pv.cubemap_from_filenames if False else None
tex = pv.Texture([pv.Texture(face(n)).to_image() for n in names]) 

pl = pv.Plotter(off_screen=True, window_size=(W, H), lighting="none")
pl.set_background(BG)
pl.set_environment_texture(tex)
SEP = 3.6
up = surf.copy(deep=True); up.points = up.points + np.array([-SEP, 0, 0])          # phi = 0: cloud above z = 0
dn = surf.copy(deep=True); p = dn.points.copy(); p[:, 2] *= -1; p[:, 0] += SEP     # phi = pi: mirror image, below z = 0
dn.points = p; dn = dn.flip_faces().compute_normals(auto_orient_normals=True)
plane = pv.Plane(center=(0, 0, 0), direction=(0, 0, 1), i_size=15, j_size=8)
pl.add_mesh(plane, color="#ff8f98", opacity=PLANE_OPACITY, smooth_shading=True)
#pl.add_mesh(plane.extract_feature_edges(), color="#8fb8ff", line_width=2, opacity=PLANE_OPACITY)
for m in (up, dn):
    pl.add_mesh(m, color="#c9ced6", pbr=True, metallic=1.0, roughness=0.22, smooth_shading=True)
pl.add_light(pv.Light(position=(-14, -4, 3), focal_point=(0, 0, 0), color="#ffd9a8", intensity=1.2))
pl.add_light(pv.Light(position=(12, 6, 1), focal_point=(0, 0, 0), color="#9cc0ff", intensity=0.8))
pl.camera_position = [(1.0, -19.0, 5.5), (0, 0, 0.0), (0, 0, 1)]; pl.camera.zoom(1.05)
img = pl.screenshot(None, return_img=True, scale=2); pl.close()
Image.fromarray(img).resize((W, H), Image.LANCZOS).save("superposition_3d_metal_pair_1s_2p.png"); print("saved")
