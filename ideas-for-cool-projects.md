---
description: "Do you have an idea for a cool research project? Awesome! Please write it down below \U0001F447"
---

# 💡 Ideas for Cool Projects

* Please indicate the author of the idea in brackets \(to get more info if necessary\)
* _Italic_: idea being investigated / work in progress
* **Bold**: Top priority

## Good Internship Projects

* [Projects GBM3100](https://drive.google.com/drive/folders/1_LuA1rKbHq6sgacGRvw3_Er7sCWND0wt)
* Look at ethnical background for normalizing spinal cord CSA using spine-generic database
* [SCT projects](https://github.com/neuropoly/spinalcordtoolbox/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+internship+project%22)
* [ivadomed projects](https://github.com/ivadomed/ivadomed/issues?q=is%3Aopen+is%3Aissue+label%3A%22Good+intership+project%22)
* [ADS projects](https://github.com/neuropoly/axondeepseg/labels/good%20internship%20project)
* [Shimming Toolbox projects](https://github.com/shimming-toolbox/shimming-toolbox/labels/good%20internship%20project)
* qMRLab

## Deep Learning

* [Data augmentation for one-shot image segmentation](https://arxiv.org/pdf/1902.09383v1.pdf)
* [Data augmentation, contrast agnostic segmentation with synthetic images](https://arxiv.org/abs/2003.01995) \(Marie-Helene\)
* [MS lesion segmentation](https://github.com/ivadomed/pipeline-ms-lesion)
* Compare SoftSeg outputs and PVE \(Andreanne, Charley\)
* AxonDeepSeg
  * Active learning \(Mélanie\)
  * 3D segmentation, looking at GoogleBrain method \(Oumayma\)
  * segment glia \(contact: Nikola/Roken/Jason\)
* MRI/Spinal cord
  * **detection of spinal cord compression point \(collab: Valosek\)**
  * **training multi-contrast models for MS lesion segmentation**
  * multi-modal training, MS lesion segmentation, without co-registration \(model would learn that\)
  * **neuroRx model training**
* Misc
  * [phase-unwrapping](https://github.com/neuropoly/ml-phase-unwrapping) \(project started by Olivier\)
  * Shimming project: real-time prediction of B0 shift based on resp. training period.

## Spinal Cord Toolbox

* SoftSeg for computing CSA. Using Paul's pipeline.
* Compute realistic model for cord atrophy by estimation a transformation between SC mask and eroded SC mask.
  * implement realistic model for scan-rescan, bias field, etc. 👉 [https://github.com/fepegar/torchio](https://github.com/fepegar/torchio)
* Develop a SIENAX based method for computing the cord size in comparison with PAM50 atlas. This will give us a scaling factor value that can be used to correct CSA-type of values.
  * Small healthy subjects \(i.e. children\) can get CSA values that are inside the range of atrophic cords whereas extremely tall patients can get values that might seem healthy.
  * Get normalized scaling factor per spinal cord vertebrae level in order to correct this
  * We need an invariant structure to compute it, however the bones are difficult to segment with SCT, hence we will use the outer CSF border as reference of the boundary between tissue and bones.
  * Potential problems - inflammation in this area, outer part of the CSF, cord compression???
  * Context: [https://forum.spinalcordmri.org/t/how-to-scale-spinal-cord-from-brain-data/403/5](https://forum.spinalcordmri.org/t/how-to-scale-spinal-cord-from-brain-data/403/5)
* CSA
  * Estimate partial volume effect with surrounding CSF in order to compute a CSF that is contrast-independent.
  * Comparison of CSA across T2, T1, T2\* –&gt; ways to normalize
  * Vérifier si relation entre CSA et sexe \(normalement oui car relation entre CSA et taille évidente \(à vérifier\) puis relation entre taille et sexe également \(à vérifier\)\)
  * correlation with several parameters \(ICV, neck length, BMI, spinal cord length\)
* Spinal levels \(Benjamin\)
  * compute difference between vertebral-spinal instead of displaying the mean distance from PMJ
  * use large FOV T2 data to segment spinal roots \(Zhuoqiong Ren\)
  * use data from Paris \(spinal levels already identified\)
* Calculate angle between mpMRI slice and cord, and estimate bias caused by partial volume effect \(see Allan's email from July 8th\)

## Myelin Imaging

* look into selective inversion recovery myelin mapping \(exchange effects\), see Smith et al.
* build a myelin phantom
  * oil emulsion? mayonnaise? milk?
* MTV
  * acquire data in phantom and check pipeline for B1- and B1+ correction, T1 and PD fitting
  * try non-linear fitting or weighted least square
* add features on the qMTLab software \(Nikola\)
* k-mean clustering of medic across echoes
* comparison AFI / double angle for B1 mapping \(data Boston\)
* estimate and correct T1 effect in short-TR diffusion imaging
  * estimate T1 \(e.g. using AFI\) and account for variation with pulse OX on diffusion scans
  * compare with long-TR diffusion scans

## Histology

* AxonDeepSeg: [http://neuroinformatics.be/modular-machine-learning-classification-toolbox-imagej-2/](http://neuroinformatics.be/modular-machine-learning-classification-toolbox-imagej-2/)
* **Framework for registering MRI and histology using 3d-printed frame:** [**https://www.slideshare.net/KlausSchmierer/neuropathological-correlates-imperialcollege4slsh2feb2018**](https://www.slideshare.net/KlausSchmierer/neuropathological-correlates-imperialcollege4slsh2feb2018)\*
* **CARS imaging of fixed vs. unfixed and see how shrinking affect each sub-region \(myelin, axon, etc.\)**
* phantom emulsion

## Acquisition

* **compensation of cardiac-related cord motion in spinal cord DTI \(julien\)**
  * acquire velocity encoding data and use to correct bvalue
  * acquire singles slice data at 50, 100, 150… ms after pulse ox peak. Weight diff along X, Y and Z. Acquire at C2, C4, C6.
  * data processing: show fig with cardiac cycle, and zoomed window of COV \(mean DWI/std\).
  * PulseOx vs. ECG and impact of timing on DW data \(julien\)

## Pulse Sequence Programming

* qMT on 7T scanner at ICM \(6 months\)

## RF Coil

* cushion for reducing inhomogeneities
  * [http://www.magmedix.com/mri-surgical/mri-sat-pads/sat-pad-mri-neck-imaging-kit.html](http://www.magmedix.com/mri-surgical/mri-sat-pads/sat-pad-mri-neck-imaging-kit.html)
* spine coil 3T with coupled coil anteriorly to combine with rFOV and pyrolitic foam \(Alexandru\)
* fieldprobes \(phosphore?\)
* Phantoms:
  * [http://martinos.org/~guerin/downloads.html](http://martinos.org/~guerin/downloads.html)
* metamaterial \(Caloz\)
  * for focusing in a region inside the body \(e.g. application for reduced field-of-view\)
  * for compensating B1+ inhomogeneity at 7T
  * for encoding? \(see spiraled phase\)
  * for moving excitation \(metamaterial can be controled with DC current, inducing movement of transmitted wave\)
* metasurface \(Nibardo\):
  * Receive array made with Surface-Circuit-Surface \(SCS\) metasurface \(receive element in inner Surface - low noise transistor stage, or complete preamp, integrated in Circuit layer - other antenna in outer Surface\)

## Shimming

* **Simulate susceptibility variation owing to O2 in lungs for real-time shimming**
  * model lungs and spine to estimate B0 variation and dynamics.
  * use Zumbal phantom
  * Apply realistic 3D warping field on the Zumbal phantom to deform the lungs, chest, etc.
  * See if the change in chest motion translates into linear shift in B0 \(currently our assumption\)
* Field mapping
  * Look at Poem phase combination from Bruce Pike's lab
  * Look at ROMEO
* Use MRD/Gadgetron to get data in real time for offline recon
  * look at IDEA forum: they have ICE functor to install, to be able to bypass ICE and send it on switch, on which client station is connected via ethernet \(1 GB/s\)
  * Info: ppl from NIH/Gadgetron: Rajiv, Adrienne Campbell [adrienne.campbell@nih.gov](mailto:adrienne.campbell@nih.gov)
  * After thoughts: maybe not the best idea for now \(use Siemens env instead\)
* Representing average B0 distortion in the spinal cord
  * inspiration from: [https://drive.google.com/drive/folders/1E3zcAkKiYAa9ewdUxihvaIF5FY2iif27](https://drive.google.com/drive/folders/1E3zcAkKiYAa9ewdUxihvaIF5FY2iif27)
* Get a better sense of field changes owing to respiration:
  * use machine learning to have a good estimate of lung volume based on one or more respiratory probes
  * explore use of field probes, e.g. loading coil
* Simulate ghosting by reconstructing synthetic k-space data \(with varying amount of phase errors, adding in a static and/or dynamic way\)
* Measure small-scale variation of B0 along spinal cord across subjects
* Applications
  * CEST with real-time shimming
* Masking
  * Implement BET to segment the brain

## Simulators

* qMTLab software for simulating and fitting magnetization transfer data \(Nikola\)
* dSim software for simulating diffusion sequences in realistic fibre/myelin arrangements \(Nikola\)

