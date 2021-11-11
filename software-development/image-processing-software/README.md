# Image Processing

```{toctree}
:hidden:
advanced-normalization-tools-ants
anima
diffusion-simulator
freesurfer
fsl/README
itk-snap
nifti
openneuro-cli
osirix
```

## Smoothing

### Gaussian Filter

To smooth an image choosing the dimension\(s\) in which you want to apply the smoothing

```bash
c3d <input_image> -smooth <std_dim1>x<std_dim2>x<std_dim3>vox -o <output_image>
```

where &lt;std\_dim1&gt;, &lt;std\_dim2&gt; and &lt;std\_dim3&gt; are the standard deviation of the Gaussian kernel in each dimension.

#### Example:

```bash
c3d t2.nii.gz -smooth 0x0x5vox -o t2_z_smoothed.nii.gz
```

_Smooth the image t2.nii.gz only along the third dimension with a standard deviation of 5 voxels in this dimension._

```text
c3d t2.nii.gz -smooth 1vox -o t2_smoothed.nii.gz
```

_Smooth the image t2.nii.gz in every direction with a standard deviation of 1 voxels._

### Median Filter

The median filter, contrary to the gaussian filter, smooth an image by preserving the edges. It can be applied using fslmaths:

```text
fslmaths <input_image> -fmedian <output_image>
```

## Intensity Correction

It happens that an image has not a homogeneous intensity field. In MRI, the intensity is proportional to the antena proximity.

### N3 - Non-parametric Non-uniform Intensity Normalization

Information can be found on [http://en.wikibooks.org/wiki/MINC/Tools/N3](http://en.wikibooks.org/wiki/MINC/Tools/N3)

This filter can be applied using the following command \(MNI tools\): \(Problem –&gt; lost the image intensity dynamic\)

```bash
mri_nu_correct.mni --i <input_image> --o <output_image>
```

Or with c3d:

```bash
c3d <input_image> -biascorr -o <output_image>
```

### N4

The N4 algorithm is a variation of the original N3 algorithm with the additional benefits of an improved B-spline fitting routine which allows for multiple resolutions to be used during the correction process.

This algorithm is implemented on ITK \([http://www.itk.org/Doxygen/html/classitk\_1\_1N4BiasFieldCorrectionImageFilter.html](http://www.itk.org/Doxygen/html/classitk_1_1N4BiasFieldCorrectionImageFilter.html)\)

or in c3d:

```bash
c3d <input_image> -n4 -o <output_image>
```

Example \(before-after N4 correction\):

![](https://www.neuro.polymtl.ca/_media/tips_and_tricks/errsm_09_t2.png?w=200&tok=32fbae) ![](https://www.neuro.polymtl.ca/_media/tips_and_tricks/errsm_09_t2_n4.png?w=196&tok=ccc8f8)

## Manual Segmentations

[http://www.bmc.med.utoronto.ca/bmcwiki/doku.php/technologies:imaging\_processing\_software](http://www.bmc.med.utoronto.ca/bmcwiki/doku.php/technologies:imaging_processing_software)

