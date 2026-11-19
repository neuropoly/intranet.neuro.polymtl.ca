# ITK-SNAP

[ITK-SNAP](http://www.itksnap.org/pmwiki/pmwiki.php) is a software package used to segment structures in 3D medical images.

## Create a mesh out of a binary file <a id="create_a_mesh_out_of_a_binary_file"></a>

ITK-SNAP allows you to construct a mesh \(`.vtk`\) with a binary mask.

1. Change the anatomic image: `File -> Open grayscale image` 
2. Load the mask: `Segmentation -> Load from image` 
3. Click `update mesh` in the bottom of the window
4. Record the mesh: `Segmentation -> Export as surface mesh` and indicate the format as `VTK PolyData File`

