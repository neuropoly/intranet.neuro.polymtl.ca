# Diffusion Simulator

Use `datasynth` command. Substrate can be one-diameter cylinders, `gamma-dist` cylinders, crossing cylinders, balls. Here you have a tutorial: [Monte Carlo Diffusion Simulator](http://cmic.cs.ucl.ac.uk/camino/index.php?n=Tutorials.MCSimulator).

Basic commands:

```bash
datasynth -walkers 50000 -tmax 2000 -voxels 1 -p 0.0 -schemefile /home/django/tanguy/data/simulations/bvecs/patient_1.scheme  -initial uniform -substrate cylinder -packing hex -cylinderrad 2E-6 -cylindersep 4.1 > Diffusion.img
analyzeheader -datadims 1 1 1 -nimages 16 -voxeldims 1 1 1 -datatype float -outputfile Diffusion.hdr
fslchfiletype NIFTI Diffusion.img
```

You can choose the permeability of the barriers via p but not the thickness.

However, you can also build any kind of shape using a PLY file \(3D object file\). Here is a tutorial for this option: [Monte-Carlo Mesh Simulation](http://cmic.cs.ucl.ac.uk/camino/index.php?n=Tutorials.MCMeshSimulation).

## Recommendations <a id="advices"></a>

* `cylindersep` must be at least twice as big as `cylinderrad` \(cylinders mustn't overlap\)
* Be very careful at high q-values \(&gt;0.14 um-1\). You need lots of walkers \(200 000\), and time steps \(-tmax 3000\)

![](https://www.neuro.polymtl.ca/_media/tips_and_tricks/screen_shot_2013-12-06_at_12.39.28_pm.png?w=200&tok=ef38e9)

