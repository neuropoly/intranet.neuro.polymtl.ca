# OsiriX

[OsiriX](https://www.osirix-viewer.com/) is a DICOM file viewer designed for MacOS and iOS.

## Usage

### Straighten Spinal Cord <a id="straighten_spinal_cord"></a>

1. Load image
2. select **3D curved MPR**
3. select the top left icon with the green curved line and red spots
4. select a couple of points along the spinal cord
5. select … view and select **export this image to a DICOM file** \(cmd+e\)
   1. select **a series with the following settings**
   2. select **transverse slices**

### Manual Segmentation of the Spinal Cord <a id="manual_segmentation_of_the_spinal_cord"></a>

1. Load image
2. Select axial orientation \(easier to have both views on screen\)
3. Disable interpolation for zoom. Menu Osirix → Preferences → Viewer → Miscellaneous → Check **No interpolation for zoom**
4. Select ROI tool \(icon… not ROI menu\) → Closed polygon
5. Create a 2D segmentation of the spinal cord at each vertebral level \(save ROIs to extract cross-sectional area\)
6. Select ROI → ROI Volume → Generate missing ROIs \(save ROIs\)
7. Select ROI → Set pixels values to :
   1. Apply to All ROIs
   2. Set pixels that are Inside ROIs
   3. If current value is larger than 0 and if current value is smaller than _10000_ \(check boxes\)
   4. To thus new value : 1
   5. Click “OK”
8. Apply same process to outside ROIs pixels and change value to 0
9. Set the image dynamic \(WL/WW –&gt; “Set WL/WW manually\) to 0 and 1
10. Right click and export to DICOM file\(s\)
    1. All images of the series
    2. Image format : as stored in memory in 16-bit BW \(important to keep dimensions!\)
    3. Change name and click “OK”

Use `dcm2nii` to transform DICOM files to a Nifti image.

## Troubleshooting

**!! IMPORTANT !!**

Sometimes, **OsiriX** changes dimensions and orientation. To repair this problem, you must use `c3d`. If it's just an orientation problem, you may use `sct_orientation`.

```bash
c3d <targetfilename> <inputfilename> -reslice-identity -o <outputfilename>
```

```bash
sct_orientation -i <inputfilename> -o <outputfilename> -orientation <three letter code of target orientation>
```

