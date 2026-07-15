# Python

## Installation

* [Enthough Canopy](https://www.neuro.polymtl.ca/tips_and_tricks/python/canopy)
* [Miniconda (preferred)](https://www.neuro.polymtl.ca/tips_and_tricks/python/miniconda)

## IDEs

Below are popular IDE that are used at NeuroPoly:

* Visual Studio Code ([VSCode](https://code.visualstudio.com/))
    * Since VSCode is a "general" IDE, you will need to install extensions to work with specific languages. For Python, you will need to install the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python). 
* JetBrains [PyCharm](https://www.jetbrains.com/pycharm/)

Here are some useful tips/modules/extensions to get the most out of your IDE:

### 1. Run tests by changing the Python interpreter to an existing Virtual Environment

If you are working on a project that installs itself into a Python/Conda virtual environment, then it is a good idea to attach the virtual environment to your IDE. (This will let you run tests directly from IDE, using the packages installed in the project's virtual envrionment.)

First, make sure you have run the installation instructions for your project, and that you have opened the project folder in your IDE. Next, follow the instructions corresponding to your IDE:

<details>
<summary>VSCode</summary>

1. First, select the correct interpreter by first opening up the Command Palette (SHIFT+CMD+P or CTRL+SHIFT+P), typing "Python: Select Interpreter", then selecting the virtual environment corresponding to the project. (For SCT, this is `venv_sct`)
   ![image](https://github.com/neuropoly/intranet.neuro.polymtl.ca/assets/16181459/a2798fab-8dcc-499a-b979-c11f1c7927a2)
2. After selecting the correct interpreter, click on the flask icon in the sidebar, then click "Configure Python Tests", then "pytest". Then, select the directory containing the test files ("testing", "tests", etc.)
   ![image](https://github.com/neuropoly/intranet.neuro.polymtl.ca/assets/16181459/351e2f4b-9962-498a-9764-c981dced8d72)
3. Once tests are configured, you will now be able to Run and Debug tests directly from the Python test files by clicking (or right clicking) on the green arrow next to each test.

   ![image](https://github.com/neuropoly/intranet.neuro.polymtl.ca/assets/16181459/21e9d5b3-f2f9-44f4-a893-e0a99973e33d)
</details>

<details>
<summary>PyCharm</summary>

1. File > Settings > Project: spinalcordtoolbox > **Python interpreter**
2. Gear in top-right > **Show all**

   ![image](https://github.com/neuropoly/intranet.neuro.polymtl.ca/assets/16181459/f7e9cc00-d7cd-43be-9b87-c8ecbbbce389)

3. `+` in top-right > **Add Local Interpreter...**

   ![image](https://github.com/neuropoly/intranet.neuro.polymtl.ca/assets/16181459/cb74a403-4b1b-4f5e-9bc5-5baf986fbe10)

4. **"Conda environment"** in top-left > Check "Existing environment", then set **Interpreter:** to `${SCT_DIR}/python/envs/venv_sct/bin/python`. (NB: Replace ${SCT_DIR} with the location of the SCT installation directory.)

</details>

### 2. Opening lines of code on GitHub

If you are looking at code in your text editor and want to share a link to specific lines on GitHub, normally you would have to go to GitHub, find the same file, select the lines (by clicking with "shift" held down), right click, click "Copy permalink". ("Permalinks" are links that reference a specific commit, so that the links will not change even if the git branch is updated in the future.)

However, you can skip much of this work by going right from your IDE to GitHub using a single click:

<details>
<summary>VS Code</summary>

1. First, install the [Open In GitHub](https://marketplace.visualstudio.com/items?itemName=sysoev.vscode-open-in-github) extension.
2. Next, highlight a snippet, then right click and select "Open In GitHub: Copy File URL" and it will take you directly to a permalink to those lines on GitHub.

![image](https://github.com/neuropoly/intranet.neuro.polymtl.ca/assets/16181459/9aa6bd77-edcf-4ae0-940b-9ba6ff1c8ed7)

</details>
 
<details>
<summary>PyCharm</summary>

PyCharm has this feature baked directly into the IDE. Just highlight a snippet, then right click and select "Open In -> GitHub" and it will take you directly to a permalink to those lines on GitHub.

![image](https://github.com/neuropoly/intranet.neuro.polymtl.ca/assets/16181459/ee2c50cc-bbd8-42f4-b812-7d5dfa0daec7)

</details>

If you then paste the permalink in a GitHub comment on issues/PRs, GitHub will automatically render those lines in your comment. (This is super useful for when you're debugging an issue locally, and you want to communicate exactly which lines you're looking at locally.)

![image](https://github.com/neuropoly/intranet.neuro.polymtl.ca/assets/16181459/11225781-78dc-4972-8ab5-9dc403e05ebe)

## Virtual Environments

Virtual environments are the recommended way to manage your python environment. They allow the use of specific versions
in your project, which helps reproducibility and stability.

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
