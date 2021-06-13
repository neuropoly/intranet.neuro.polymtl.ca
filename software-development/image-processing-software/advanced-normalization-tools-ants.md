# Advanced Normalization Tools \(ANTs\)

> [ANTs](http://stnava.github.io/ANTs/) extracts information from complex datasets that include imaging \([Word Cloud](http://brianavants.files.wordpress.com/2013/05/avants_wordcloud.jpg)\). Paired with [ANTsR](http://stnava.github.io/software/2014/01/08/antsr/) \(answer\), ANTs is useful for managing, interpreting and visualizing multidimensional data. ANTs is [popularly](https://sourceforge.net/projects/advants/files/ANTS/stats/timeline?dates=2010-07-19+to+2099-05-25) considered a state-of-the-art medical image registration and segmentation toolkit. ANTsR is an emerging tool supporting standardized multimodality image analysis. ANTs depends on the Insight ToolKit [\(ITK\)](http://www.itk.org/), a widely used medical image processing library to which ANTs developers contribute. A summary of some ANTs findings and tutorial material \(most of which is on this page\) is [here](http://rpubs.com/stnava/ANTsTut).
>
> ~ _Source:_ [_ANTs_](http://stnava.github.io/ANTs/) _webpage_

## Installation

[http://brianavants.wordpress.com/](http://brianavants.wordpress.com/)

Once you've compiled the binaries, you can copy the `bin` folder and the `lib` folder here: `/usr/local/ants/`.

In case you have previously installed ANTs binaries into `/usr/bin` and you would like to remove them without manually do each for each file, [here](https://www.neuro.polymtl.ca/_media/tips_and_tricks/remove_ants_files.py) is a python script that does it.

To copy ants binaries for SCT, go to your antsbin folder. Then, copy the `build_ants_sct.sh` script found in `SCT_DIR/bin/osx` or linux and then execute it.

## Parameters for antsRegistration

### transform

`-transform SyN[gradientStep, updateFieldVarianceInVoxelSpace, totalFieldVarianceInVoxelSpace]`

`gradientStep`: the higher, the more high frequency deformations \(and less stable\)

`updateFieldVarianceInVoxelSpace` \(default=3\) –&gt; the higher, the less high frequency deformations.

`totalFieldVarianceInVoxelSpace`: default=0.

```text
  Exponential[1,5,5]
```

* does not seem to move a lot

```text
  BSplineSyN[0.1,5,5,2]
```

`gradientStep`: 0.5 –&gt; the smaller, the smaller the distortion

`updateFieldMeshSizeAtBaseLevel`:

`totalFieldMeshSizeAtBaseLevel`: The larger, the larger the deform.

`splineOrder`=3

### metric

`-metric CC[x, x, weight, radius]`

`weight`: 1. This param has no influence if there is only one transform.

`radius`: 4

CC is much slower than MI on large images.

```text
  MI[x,x,weight,nbBins]
```

`nbBins`: 32

* fast! however, does not work if using small mask \(not enough values\).

### smoothing-sigmas

`-smoothing-sigmas`

* Can have a HUGE impact on the result. Don’t hesitate to try without smoothing, i.e., 0x0 \(if you have 2 iterations\).

### convergence

-convergence 20×3 –shrink-factors 2×1 –smoothing-sigmas 1x1mm –Restrict-Deformation 1x1x0 –output \[tmp\_reg,tmp.src\_pad\_reg.nii\] –collapse-output-transforms 1 –interpolation BSpline\[3\] –winsorize-image-intensities \[0.005,0.995\]

## Visualizing Warping Field

ANTs saves the warping field as a component image \(5D\), not in vector format \(4D\). Therefore, it cannot be interpreted by FSL. To convert the warping field in component, you can use c3d:

```bash
c3d -mcs warp_comp.nii -oo warp_vecx.nii warp_vecy.nii warp_vecz.nii
```

To convert vector-based warping field into component image readable by ANTS, use the following command

```bash
c3d warp_vecx.nii warp_vecy.nii warp_vecz.nii -omc 3 warp_comp.nii
```

## Translation

-t Translation\[GradientStep\]

**Example:**

```bash
antsRegistration -d $ImageDimension -r [${FILE_DEST}.${EXT},${FILE_SRC}.${EXT} ,1] -m ${MetricType}
${FILE_DEST}.${EXT},${FILE_SRC}.${EXT},1,4] -o $OutPrefix -t Translation -c [10000x10000x10000,1.e-8,20] -s 4x2x1vox -f 3x2x1
```

## Restrict Gradient Deformation

–Restrict-Deformation XxYxZ

**Example: restrict the gradient in two dimensions \(axial\)**

```bash
ants $ImageDimension -m ${MetricType}[${FILE_DEST}.${EXT_ANAT},${FILE_SRC}.${EXT},1,4] --Restrict-Deformation 1x1x0 -t SyN -r Gauss[6,3] -o ${PATH_OUTPUT}/ -i ${MaxIteration}
```

Note: this restriction **does not** apply to the affine transformation

## Point-Set Expectation \(PSE\)

From the [ANTs Manual PDF](https://github.com/stnava/ANTsDoc/raw/master/ants2.pdf):

`-m PSE [fixedImage, movingImage, fixedPoints, movingPoints, weight, pointSetPercentage, pointSetSigma, boundaryPointsOnly, kNeighborhood, PartialMatchingIterations=100000]`

– `fixedImage`: defines the space domain of the fixed point set.

– `movingImage`: defines the space domain of the moving point set.

– `fixedPoints/Image`: defines the coordinates of the fixed point set or label image. It can be an image with discrete positive labels, a VTK format point set file, or a text file. Details can be found in I/O section \(TODO\).

– `movingPoints/Image`: defines the coordinates of the moving point set or label image.

– `weight`: weight for this metric. 1 weights are relative to the weights on the N other metrics passed to ANTs — N is unlimited.

– `pointSetPercentage`: the percentage of points to be randomly sampled used in the registration.

– `pointSetSigma`: the standard deviation of the Parzen window used to estimate the expectation.

– `boundaryPointsOnly`: 1 \(or “true”\) means only the boundary points in the label image is used to drive registration.

– `kNeighborhood` is a positive discrete number. The first k neighbours are used to compute the deformation during the registration.

– `PartialMatchingIterations` controls the symmetry in the matching. This option assumes the complete labeling is in the first set of label parameters … more iterations leads to more symmetry in the matching - 0 iterations means full asymmetry

### **Example**

```bash
ants 3 -m PSE[destination.nii,source.nii,mask_destination.nii,mask_source.nii,0.8,100,1,0,1,100000] -o source_reg -i 0 --rigid-affine true --number-of-affine-iterations 100x10x5 -m MI[destination.nii,source.nii,0.2,4] --use-all-metrics-for-convergence 1
```

This line does an affine registration of the moving to the fixed image. There are 2 metrics used: PSE \(point-set expectation\) and MI \(mutual information\). The weight of each of them is the first “non-string” argument \(0.8 for PSE and 0.2 for MI here\). To do a diffeomorphic transformation, change the -i paramater to something like 50x50x50 \(number of iteration to do for the diffeomorphic transformation\). The MARKER files can be done with the ITK-snap labelling utility

```bash
 # apply the transformation
 WarpImageMultiTransform $DIM ${FILE_SRC}.${EXT} ${FILE_SRC}_reg_diffeo.${EXT} -R ${FILE_DEST}.${EXT} --use-BSpline
 ${FILE_SRC}Warp.nii.gz ${FILE_SRC}Affine.txt
```

This line applies the affine transformation to the moving image. For a diffeomorphic case, simply add ${FILE\_SRC}Warp.nii.gz in the transformation parameter \(end of the line\)

## Affine-only point-match transformation

Cannot be done with ANTs. Use the following command:

```bash
ANTSUseLandmarkImagesToGetAffineTransform fixed_image moving_image affine regAffine.txt
```

## Non-affine point-match transformation

Alternatively to ANTS, you can use the following command:

```bash
ANTSUseLandmarkImagesToGetBSplineDisplacementField
```

Note: Images should be in the same space! Otherwise you receive a Segmentation 11 error. Suggestion is to first run `ANTSUseLandmarkImagesToGetAffineTransform`, then this command.

## ITK Transform File

The `FixedCenterOfRotationAffineTransform` performs the following computation:

```bash
X′ = R·(S·X −C)+C+V
```

Where R is the rotation matrix, S is a scaling factor, C is the center of rotation and V is a translation vector or offset. Therefore the affine matrix M and the affine offset T are defined as:

```bash
M=R·S
T =C+V−R·C
```

NOTES ON ITK Transform Files:

```bash
T2d = [
a b o
c d p
0 0 1
]

T3d = [
a b c o
d e f p
g h i q
0 0 0 1
]
```

The “o p q” are the “offset”, which actually is not given in the file. The offset is computed from the 3×3 matrix \(the first 9 parameters\), from the translation “l m n” \(the last three parameters\), and from the center “x y z” \(the three fixed parameters\). To see how this is done, look at the code for ComputeOffset\(\) itkMatrixOffsetTransformBase.hxx.

How centered transforms work: p' = R \(p - C\) + C + T where p' = transformed point, p = original point, C = Center, T= Translation. R= Rotation matrix.

Format for 2d affine transfo:

```text
#Insight Transform File V1.0
#Transform 0
Transform: AffineTransform_double_2_2
Parameters: a b c d o p
FixedParameters: 0 0
```

Format for 3d affine transfo:

```text
#Insight Transform File V1.0
#Transform 0
Transform: AffineTransform_double_3_3
Parameters: a b c d e f g h i o p q
FixedParameters: 0 0
```

Documentation:

1. ITK Documentation \(700 pages\): [https://itk.org/ItkSoftwareGuide.pdf](https://itk.org/ItkSoftwareGuide.pdf)
2. [https://itk.org/Wiki/ITK/ImageRegistration](https://itk.org/Wiki/ITK/ImageRegistration)
3. [http://public.kitware.com/pipermail/insight-users/2014-January/049703.html](http://public.kitware.com/pipermail/insight-users/2014-January/049703.html)

Conversion world-image coordinate:

1. [http://www.vtk.org/Wiki/Proposals:Orientation](http://www.vtk.org/Wiki/Proposals:Orientation)

Discussions about ITK world coordinates:

1. [https://sourceforge.net/p/advants/discussion/840261/thread/2a1e9307/](https://sourceforge.net/p/advants/discussion/840261/thread/2a1e9307/)
2. [https://sourceforge.net/p/advants/discussion/840261/thread/ee4a6455/](https://sourceforge.net/p/advants/discussion/840261/thread/ee4a6455/)

