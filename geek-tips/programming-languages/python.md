# Python

## Installation

* [Individual package installation](https://www.neuro.polymtl.ca/tips_and_tricks/python/installation)
* [Enthough Canopy](https://www.neuro.polymtl.ca/tips_and_tricks/python/canopy)
* [Miniconda (preferred)](https://www.neuro.polymtl.ca/tips_and_tricks/python/miniconda)

## IDE

* [Pycharm](https://www.neuro.polymtl.ca/tips_and_tricks/python/pycharm)
* Interactive debugging using iPython: [http://www.scipy-lectures.org/advanced/debugging/#using-the-python-debugger](http://www.scipy-lectures.org/advanced/debugging/#using-the-python-debugger)
* [iPython](http://ipython.org)

## Virtual Environments

1\. Create a virtual environment for a project:

```
$ cd my_project_folder
$ virtualenv venv
```

Or to specify a Python version:
```
$ virtualenv venv -p <PATH_TO_PYTHON>
```

2\. To begin using the virtual environment, it needs to be activated:

```
 
 $ source my_project/bin/activate
```

3\. If you are done working in the virtual environment for the moment, you can deactivate it:

```
 $ deactivate
```

## Packaging Code

Suggest workflow via Github Actions:

* on Pypi, create a Token for the “organization” with “global” scope
* on Github > Settings > Secrets > Add a secrets.
  * Warning: if you created the token at the organization level, you should create a secrets for the organization (not the repos)
* Create a Github action template for “publishing”
* Github uses `twine` to publish the package, everytime a release is created (does not work for draft releases)
* Edit the `.yml` file with the credentials for connecting to Pypi
  * Example: [https://github.com/neuropoly/gifmaker/blob/master/.github/workflows/python-publish.yml](https://github.com/neuropoly/gifmaker/blob/master/.github/workflows/python-publish.yml)
* To debug, you can create the package locally and verify its integrity:
  * Install twine: `pip install twine`
  * Build the distribution: `python setup.py sdist bdist_wheel`
  * Check integrity: `twine check dist/*`

## Useful Packages

### NeuroImaging

* [Nipype](http://nipy.sourceforge.net/nipype/0.6/index.html)
* [Dipy - Diffusion imaging in Python](http://nipy.org/dipy/index.html)
* [NiLearn](http://nilearn.github.io)

### Visualization

* [PySurfer](https://pysurfer.github.io)
* [NiLearn](http://nilearn.github.io/index.html)
* [The Connectome Viewer Toolkit](http://www.cmtk.org)
* [Mayavi - 3D data visualization](https://pypi.python.org/pypi/mayavi)
* [PyMVPA](http://dev.pymvpa.org)
* [BrainVisa](http://brainvisa.info)

## Courses and Tutorials

* [Learn Python with Socratica](https://www.youtube.com/playlist?list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-)
* [Excellent book on Python, git and Unix Shell, addressed to researchers](https://merely-useful.github.io/py-rse/index.html)
* [Excellent notes on Python](http://matthew-brett.github.io/pydagogue/index.html#)
* [Matlab to Python(Numpy) cheat sheet](http://mathesaurus.sourceforge.net/matlab-numpy.html)
* [Scipy lectures](http://scipy-lectures.github.io)
* [Presentation by Martin Luessi](http://nmr.mgh.harvard.edu/whynhow/scientific_python\_2012.html)
* [Commands](https://www.neuro.polymtl.ca/tips_and_tricks/python/commands)
* [2D and 3D plotting using matlplotlib](http://nbviewer.ipython.org/urls/raw.github.com/jrjohansson/scientific-python-lectures/master/Lecture-4-Matplotlib.ipynb)

## Resources

* [https://www.geeksforgeeks.org/command-line-scripts-python-packaging/](https://www.geeksforgeeks.org/command-line-scripts-python-packaging/)
* [Problem Solving with Algorithms and Data Structures using Python](https://runestone.academy/ns/books/published//pythonds/index.html)

## Tips and Tricks

### Nice Packages

\- [pytest-sugar](https://github.com/Teemu/pytest-sugar): Nice visualization for pytestEdit

### Matplotlib

Display 2d array:

```python
from matplotlib.pylab import *
matshow(data2d, fignum=1, cmap=cm.gray), plt.colorbar(), show()
```

Interactive mode (can display several figures without freezing the process)

```python
import matplotlib.pyplot as plt
plt.ion()
plt.plot([1.6, 2.7])
plt.draw()
# Turn interactive mode off
plt.ioff()
```

Using oriented-object approach (force backend)

```python
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
fig = Figure()
FigureCanvas(fig)
ax = fig.add_subplot(111)
ax.matshow(data2d, cmap='gray')
fig.savefig('myfig.png')
```
