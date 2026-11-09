"""Atomic Radiation Post 4 — cinematic Rindler horizons and accelerated atom.

Run: pip install numpy pyvista vtk
     python atomic_post4_rindler.py

Coordinates (X,Y,Z) = (longitudinal space z, transverse space y, ct).
The plot is a 2+1 dimensional SLICE of Minkowski spacetime. An atom with
constant proper acceleration a follows z^2-(ct)^2=(c^2/a)^2, y=0.
Its past and future Rindler horizons are the null PLANES ct=+z and ct=-z
(extended along y); they are not ordinary conical surfaces. Units c=1.
"""
from pathlib import Path
import numpy as np

OUT = Path(__file__).with_suffix('.png')
WIDTH, HEIGHT = 1600, 900
A = 0.67
BACKGROUND='#060e1b'
CYAN='#54e4f2'; GOLD='#f2b46b'; MIDBLUE='#438bb1'; GRID='#34465d'

def worldline(tau):
    tau=np.asarray(tau)
    return np.column_stack((np.cosh(A*tau)/A, np.zeros_like(tau), np.sinh(A*tau)/A))

def quad_mesh(corners, nu=30, nv=30):
    """Corners (00,10,11,01); returns triangle mesh."""
    a,b,c,d=np.asarray(corners,float)
    v=np.array([(1-u)*(1-w)*a+u*(1-w)*b+u*w*c+(1-u)*w*d
                for u in np.linspace(0,1,nu) for w in np.linspace(0,1,nv)])
    faces=[]
    for i in range(nu-1):
        for j in range(nv-1):
            k=i*nv+j
            faces.extend(([k,k+nv,k+nv+1],[k,k+nv+1,k+1]))
    return v,np.asarray(faces,dtype=int)

# Each horizon is a ruled null sheet extending transverse to acceleration.
ZMAX=3.55; YMAX=1.80
FUTURE=[(0,-YMAX,0),(ZMAX,-YMAX,ZMAX),(ZMAX,YMAX,ZMAX),(0,YMAX,0)]
PAST=[(0,-YMAX,0),(ZMAX,-YMAX,-ZMAX),(ZMAX,YMAX,-ZMAX),(0,YMAX,0)]

def draw_scene(add_surface,add_tube,add_ball,save):
    # Subdued reference lattice in y=0 (the atom's spacetime plane)
    for zz in np.linspace(0,3.6,9):
        add_tube([[zz,0,-2.7],[zz,0,2.7]],GRID,.003,.19)
    for tt in np.linspace(-2.5,2.5,11):
        add_tube([[0,0,tt],[3.65,0,tt]],GRID,.003,.19)
    # Planes are actually 3-D sheets, not a collection of local event cones.
    add_surface(PAST,'#317baf',.24)
    add_surface(FUTURE,'#d69750',.24)
    # Ruling lines make the full geometric extent legible.
    for t in np.linspace(.52,3.35,7):
        add_tube([[t,-YMAX,t],[t,YMAX,t]],'#f5ba79',.004,.23)
        add_tube([[t,-YMAX,-t],[t,YMAX,-t]],'#62b7d7',.004,.19)
    for side in (-YMAX,YMAX):
        add_tube([[0,side,0],[ZMAX,side,ZMAX]],'#f6c58b',.008,.55)
        add_tube([[0,side,0],[ZMAX,side,-ZMAX]],'#6acbe7',.008,.50)
    add_tube([[0,-YMAX,0],[0,YMAX,0]],'#d1e6f5',.007,.58)
    # Lines along central y=0 plane to read the asymptotic approach.
    add_tube([[0,0,0],[3.50,0,3.50]],'#ffbd79',.012,.70)
    add_tube([[0,0,0],[3.50,0,-3.50]],'#6dc9ec',.012,.65)
    # Worldline: proper acceleration stays constant, the curve approaches both horizons.
    tau=np.linspace(-2.16,2.16,400)
    curve=worldline(tau)
    add_tube(curve,'#115473',.050,.32)
    add_tube(curve,CYAN,.021,1.0)
    for tm in (-1.58, -.65, .12, 1.15, 1.88):
        add_ball(worldline([tm])[0],.033,'#c7faff',.90)
    # Atom, highlighted on its worldline; schematic, not electron-cloud literalism.
    centre=worldline([.53])[0]
    add_ball(centre,.123,'#ffddaa',1)
    add_ball(centre,.21,'#f8b96d',.10)
    for angle in (0,60,120):
        theta=np.linspace(0,2*np.pi,160)
        circle=np.stack([.23*np.cos(theta),.23*np.sin(theta),np.zeros_like(theta)],axis=-1)
        rot=np.deg2rad(angle)
        mat=np.array([[np.cos(rot),0,np.sin(rot)],[0,1,0],[-np.sin(rot),0,np.cos(rot)]])
        add_tube(circle@mat.T+centre,'#baf2ff',.004,.67)
    # tiny directional axis tick, unobtrusive
    add_tube([[0,0,-3.0],[0,0,3.0]],'#8eaac0',.006,.30)
    save()

def render_pyvista():
    import pyvista as pv
    pl=pv.Plotter(off_screen=True,window_size=(WIDTH,HEIGHT),lighting='none')
    pl.set_background(BACKGROUND)
    try: pl.enable_anti_aliasing('ssaa')
    except Exception: pass
    def add_surface(corners,color,alpha):
        verts,faces=quad_mesh(corners)
        cells=np.column_stack([np.full(len(faces),3),faces]).ravel()
        mesh=pv.PolyData(verts,cells)
        pl.add_mesh(mesh,color=color,opacity=alpha,ambient=.60,diffuse=.35,specular=.25,show_edges=False,culling=False)
    def add_tube(points,color,r,alpha):
        mesh=pv.lines_from_points(np.asarray(points,float)).tube(radius=r,n_sides=9)
        pl.add_mesh(mesh,color=color,opacity=alpha,ambient=.48,diffuse=.50,specular=.5)
    def add_ball(pos,r,color,alpha):
        pl.add_mesh(pv.Sphere(radius=r,center=pos,theta_resolution=32,phi_resolution=32),color=color,opacity=alpha,ambient=.65,diffuse=.25,specular=.6)
    def save():
        pl.camera.position=(7.4,-9.8,5.45)
        pl.camera.focal_point=(1.71,0,0)
        pl.camera.view_up=(0,0,1)
        pl.camera.zoom(.79)
        pl.screenshot(str(OUT))
        pl.close()
    draw_scene(add_surface,add_tube,add_ball,save)

def render_vtk():
    import vtk
    from vtk.util.numpy_support import numpy_to_vtk
    def rgb(h):
        h=h.lstrip('#');return tuple(int(h[i:i+2],16)/255 for i in (0,2,4))
    ren=vtk.vtkRenderer();ren.SetBackground(*rgb(BACKGROUND))
    win=vtk.vtkRenderWindow();win.SetOffScreenRendering(1);win.AddRenderer(ren);win.SetSize(WIDTH,HEIGHT)
    win.SetMultiSamples(8)
    def actor(poly,color,alpha):
        mapper=vtk.vtkPolyDataMapper();mapper.SetInputData(poly)
        a=vtk.vtkActor();a.SetMapper(mapper);p=a.GetProperty()
        p.SetColor(*rgb(color));p.SetOpacity(alpha);p.SetAmbient(.62);p.SetDiffuse(.35);p.SetSpecular(.3)
        p.SetBackfaceCulling(False)
        ren.AddActor(a)
    def add_surface(corners,color,alpha):
        v,f=quad_mesh(corners)
        pts=vtk.vtkPoints();pts.SetData(numpy_to_vtk(v,deep=True))
        cells=vtk.vtkCellArray()
        for face in f:
            tri=vtk.vtkTriangle()
            for j,k in enumerate(face):tri.GetPointIds().SetId(j,int(k))
            cells.InsertNextCell(tri)
        poly=vtk.vtkPolyData();poly.SetPoints(pts);poly.SetPolys(cells)
        actor(poly,color,alpha)
    def add_tube(points,color,r,alpha):
        p=np.asarray(points,float);pts=vtk.vtkPoints();pts.SetData(numpy_to_vtk(p,deep=True))
        lines=vtk.vtkCellArray()
        for i in range(len(p)-1):
            l=vtk.vtkLine();l.GetPointIds().SetId(0,i);l.GetPointIds().SetId(1,i+1);lines.InsertNextCell(l)
        poly=vtk.vtkPolyData();poly.SetPoints(pts);poly.SetLines(lines)
        tub=vtk.vtkTubeFilter();tub.SetInputData(poly);tub.SetRadius(r);tub.SetNumberOfSides(9);tub.CappingOn();tub.Update()
        actor(tub.GetOutput(),color,alpha)
    def add_ball(pos,r,color,alpha):
        s=vtk.vtkSphereSource();s.SetCenter(*pos);s.SetRadius(r);s.SetPhiResolution(28);s.SetThetaResolution(28);s.Update()
        actor(s.GetOutput(),color,alpha)
    def save():
        cam=ren.GetActiveCamera();cam.SetPosition(7.4,-9.8,5.45);cam.SetFocalPoint(1.71,0,0);cam.SetViewUp(0,0,1);cam.Zoom(.79)
        win.Render()
        filt=vtk.vtkWindowToImageFilter();filt.SetInput(win);filt.SetInputBufferTypeToRGB();filt.ReadFrontBufferOff();filt.Update()
        wr=vtk.vtkPNGWriter();wr.SetFileName(str(OUT));wr.SetInputConnection(filt.GetOutputPort());wr.Write();win.Finalize()
    draw_scene(add_surface,add_tube,add_ball,save)

if __name__=='__main__':
    try:
        import pyvista
    except ImportError:
        print('PyVista not installed; rendering using its VTK backend directly.')
        render_vtk()
    else:
        render_pyvista()
    print('Wrote',OUT)
