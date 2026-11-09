"""Atomic Radiation, Post 4 — accelerated atom and 3D light cones.

Run in your Codespace with:
    pip install pyvista numpy
    python atomic_post4_feature.py

If PyVista is unavailable, the script uses the same VTK geometry directly.
Outputs atomic_post4_feature.png beside the script.

Axes: X=longitudinal space z, Y=one transverse spatial coordinate, Z=ct.
Units: c=1 and proper acceleration a=0.65. This is a 2+1D slice
of Minkowski spacetime, not a depiction of 3D physical space.
"""
from pathlib import Path
import numpy as np
import pyvista as pv
OUT = Path(__file__).with_suffix('.png')
W,H=1600,900
A=0.65
CYAN='#55e3ec'; BLUE='#258fae'; AMBER='#f8bc79'; WHITE='#d7f6fa'; GRID='#23374e'

def worldline(tau):
    return np.stack([np.cosh(A*tau)/A, np.zeros_like(np.asarray(tau)), np.sinh(A*tau)/A],axis=-1)

def cone_arrays(point,height,nr=30,nphi=100):
    """Surface of future cone of given event, excluding tip degeneracy."""
    hs=np.linspace(0.003,height,nr)
    ps=np.linspace(0,2*np.pi,nphi,endpoint=False)
    verts=np.array([[point[0]+h*np.cos(p),point[1]+h*np.sin(p),point[2]+h] for h in hs for p in ps],float)
    faces=[]
    for i in range(nr-1):
        for j in range(nphi):
            k=i*nphi+j;l=i*nphi+(j+1)%nphi
            faces.append([k,l,l+nphi]); faces.append([k,l+nphi,k+nphi])
    return verts,np.array(faces)

def tube_points_curve(arr,r=.012):
    return np.asarray(arr,float)

def create_pyvista():

    pv.global_theme.background='#07101e'
    pl=pv.Plotter(off_screen=True,window_size=(W,H),lighting='none')
    pl.set_background('#07101e')
    pl.enable_anti_aliasing('ssaa')
    def add_line(pts,color,width=0.013,opacity=1):
        path=pv.lines_from_points(pts,close=False)
        pipe=path.tube(radius=width,n_sides=10)
        pl.add_mesh(pipe,color=color,opacity=opacity,ambient=.40,diffuse=.55,specular=.55,specular_power=35)
    def add_cone(event,height,color,opacity):
        pts,tri=cone_arrays(event,height)
        cells=np.column_stack([np.full(len(tri),3),tri]).astype(np.int64).ravel()
        mesh=pv.PolyData(pts,cells)
        pl.add_mesh(mesh,color=color,opacity=opacity,ambient=.55,diffuse=.45,smooth_shading=True,show_edges=False)
        for h in (height*.47,height):
            theta=np.linspace(0,2*np.pi,201)
            ring=np.column_stack([event[0]+h*np.cos(theta),event[1]+h*np.sin(theta),np.full_like(theta,event[2]+h)])
            add_line(ring,color,.008,.95)
    # subdued coordinate scaffold
    for y in np.linspace(-1.75,1.75,9):
        add_line(np.array([[-.45,y,-1.83],[3.6,y,-1.83]]),GRID,.0035,.45)
    for x in np.linspace(-.4,3.6,10):
        add_line(np.array([[x,-1.75,-1.83],[x,1.75,-1.83]]),GRID,.0035,.45)
    add_line([[-.5,0,-1.83],[3.75,0,-1.83]],'#3c5c77',.007,.6)
    add_line([[0,0,-1.9],[0,0,2.7]],'#3c5c77',.008,.7)
    # Rindler horizon in the worldline plane
    for sign in (-1,1):
        t=np.linspace(-1.7,2.5,100)
        add_line(np.column_stack([sign*t,np.zeros_like(t),t]),'#b27d53',.004,.26)
    # cones first so trajectory remains foreground
    events=[(-1.26,1.48,'#54a6ca',.40),(-.48,1.34,'#65dce4',.36),(.35,1.18,'#f1b673',.43)]
    for tau,height,col,opacity in events:
        ev=worldline(np.array(tau))
        add_cone(ev,height,col,opacity)
        pl.add_mesh(pv.Sphere(radius=.045,center=ev,theta_resolution=24,phi_resolution=24),color=col,emissive=True)
    tau=np.linspace(-1.67,1.63,320)
    path=worldline(tau)
    add_line(path,'#135a72',.042,.42)
    add_line(path,CYAN,.018,1)
    # stylized atom at one event
    pos=worldline(np.array(.88))
    pl.add_mesh(pv.Sphere(radius=.093,center=pos,theta_resolution=40,phi_resolution=40),color='#fee1af',ambient=.55,diffuse=.3,specular=.9,specular_power=60)
    pl.add_mesh(pv.Sphere(radius=.155,center=pos,theta_resolution=32,phi_resolution=32),color='#ffc57a',opacity=.13,ambient=.7)
    for rot in (0,60,120):
        theta=np.linspace(0,2*np.pi,180)
        pts=np.column_stack([.2*np.cos(theta),.2*np.sin(theta),np.zeros_like(theta)])
        r=np.deg2rad(rot)
        m=np.array([[np.cos(r),0,np.sin(r)],[0,1,0],[-np.sin(r),0,np.cos(r)]])
        add_line(pts@m.T+pos,'#d8f6ff',.004,.55)
    pl.camera.position=(6.8,-9.8,5.4)
    pl.camera.focal_point=(1.45,0,.40)
    pl.camera.view_up=(0,0,1)
    pl.camera.zoom(1.07)
    pl.screenshot(str(OUT),transparent_background=False)
    pl.close()

def create_vtk():
    import vtk
    from vtk.util.numpy_support import numpy_to_vtk
    def rgb(s):
        s=s.lstrip('#');return tuple(int(s[i:i+2],16)/255 for i in (0,2,4))
    ren=vtk.vtkRenderer();ren.SetBackground(*rgb('#07101e'))
    win=vtk.vtkRenderWindow();win.SetOffScreenRendering(1);win.AddRenderer(ren);win.SetSize(W,H)
    win.SetMultiSamples(8)
    def actor_for_poly(poly,color,opacity,ambient=.43):
        mapper=vtk.vtkPolyDataMapper();mapper.SetInputData(poly)
        actor=vtk.vtkActor();actor.SetMapper(mapper)
        p=actor.GetProperty();p.SetColor(*rgb(color));p.SetOpacity(opacity);p.SetAmbient(ambient);p.SetDiffuse(.55);p.SetSpecular(.35);p.SetSpecularPower(25)
        ren.AddActor(actor);return actor
    def add_line(arr,color,radius=.012,opacity=1):
        pts=vtk.vtkPoints(); lines=vtk.vtkCellArray()
        for i,p in enumerate(arr):pts.InsertNextPoint(*p)
        for i in range(len(arr)-1):
            l=vtk.vtkLine();l.GetPointIds().SetId(0,i);l.GetPointIds().SetId(1,i+1);lines.InsertNextCell(l)
        poly=vtk.vtkPolyData();poly.SetPoints(pts);poly.SetLines(lines)
        tub=vtk.vtkTubeFilter();tub.SetInputData(poly);tub.SetRadius(radius);tub.SetNumberOfSides(8);tub.CappingOn();tub.Update()
        return actor_for_poly(tub.GetOutput(),color,opacity)
    def add_sphere(pos,r,color,opacity=1):
        sph=vtk.vtkSphereSource();sph.SetCenter(*pos);sph.SetRadius(r);sph.SetThetaResolution(32);sph.SetPhiResolution(32);sph.Update()
        return actor_for_poly(sph.GetOutput(),color,opacity,.6)
    def add_cone(ev,height,color,opacity):
        v,tri=cone_arrays(ev,height)
        points=vtk.vtkPoints(); points.SetData(numpy_to_vtk(v,deep=True))
        cells=vtk.vtkCellArray()
        for face in tri:
            c=vtk.vtkTriangle()
            for j,k in enumerate(face):c.GetPointIds().SetId(j,int(k))
            cells.InsertNextCell(c)
        p=vtk.vtkPolyData();p.SetPoints(points);p.SetPolys(cells)
        ac=actor_for_poly(p,color,opacity,.62)
        ac.GetProperty().SetBackfaceCulling(False)
        for h in (height*.47,height):
            theta=np.linspace(0,2*np.pi,160)
            ring=np.column_stack([ev[0]+h*np.cos(theta),ev[1]+h*np.sin(theta),np.full_like(theta,ev[2]+h)])
            add_line(ring,color,.008,.95)
    for y in np.linspace(-1.75,1.75,9):add_line([[-.45,y,-1.83],[3.6,y,-1.83]],GRID,.0035,.5)
    for x in np.linspace(-.4,3.6,10):add_line([[x,-1.75,-1.83],[x,1.75,-1.83]],GRID,.0035,.5)
    add_line([[-.5,0,-1.83],[3.75,0,-1.83]],'#3c5c77',.007,.7)
    add_line([[0,0,-1.9],[0,0,2.7]],'#3c5c77',.008,.7)
    for sign in (-1,1):
        t=np.linspace(-1.7,2.5,100)
        add_line(np.column_stack([sign*t,np.zeros_like(t),t]),'#b27d53',.004,.26)
    for tau,height,col,opacity in [(-1.26,1.48,'#54a6ca',.40),(-.48,1.34,'#65dce4',.36),(.35,1.18,'#f1b673',.43)]:
        ev=worldline(np.array(tau))
        add_cone(ev,height,col,opacity)
        add_sphere(ev,.045,col)
    path=worldline(np.linspace(-1.67,1.63,320))
    add_line(path,'#135a72',.041,.55)
    add_line(path,CYAN,.018,1)
    pos=worldline(np.array(.88))
    add_sphere(pos,.095,'#fee1af')
    add_sphere(pos,.158,'#ffc57a',.12)
    for rot in (0,60,120):
        theta=np.linspace(0,2*np.pi,180)
        pts=np.column_stack([.2*np.cos(theta),.2*np.sin(theta),np.zeros_like(theta)])
        r=np.deg2rad(rot)
        m=np.array([[np.cos(r),0,np.sin(r)],[0,1,0],[-np.sin(r),0,np.cos(r)]])
        add_line(pts@m.T+pos,'#d8f6ff',.004,.55)
    cam=ren.GetActiveCamera();cam.SetPosition(6.8,-9.8,5.4);cam.SetFocalPoint(1.45,0,.40);cam.SetViewUp(0,0,1)
    cam.Zoom(1.07)
    ren.UseDepthPeelingOff()
    win.SetAlphaBitPlanes(1)
    win.Render()
    filt=vtk.vtkWindowToImageFilter();filt.SetInput(win);filt.SetInputBufferTypeToRGB();filt.ReadFrontBufferOff();filt.Update()
    writer=vtk.vtkPNGWriter();writer.SetFileName(str(OUT));writer.SetInputConnection(filt.GetOutputPort());writer.Write()
    win.Finalize()

if __name__=='__main__':
    try:
        import pyvista
    except ImportError:
        print('PyVista unavailable: rendering with VTK directly')
        create_vtk()
    else:
        create_pyvista()
    print(f'Created {OUT}')
