import trimesh as tri
import numpy as np

def rasterize_stl(f, res=0.1):
    trimesh_obj = tri.load(f)

    cx, cy, cz = trimesh_obj.centroid
    mins,maxs= trimesh_obj.bounds
    zr = (maxs-mins)[2]
    stack = np.zeros(np.int16(((maxs - mins)/res).round()))

    for i, z in enumerate(np.arange(mins[2], maxs[2], res)):
        slice = trimesh_obj.section(plane_origin=(cx, cy,z), plane_normal=[0,0,1])
        path, _ = slice.to_planar()
        im = path.rasterize(pitch=res, 
                            resolution=((maxs - mins)/res).round()[:2])
        stack[:,:, i] = np.array(im).T

    return stacks