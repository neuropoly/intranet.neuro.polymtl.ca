"""
To build the docs:

    pip install .[sphinx]
    make html

They will end up in _build/html/

(this note is here and not in README.md because, in this case, README.md is the front-page)
"""

from setuptools import setup, find_packages

setup(
    name="intranet.neuro.polymtl.ca",
    python_requires=">=3.6",
    author="NeuroPoly",
    packages=[],
    extras_require={
        "sphinx": [
            "myst-parser",
            "sphinx-book-theme",
            "sphinx-design",
            "sphinx",
        ],
    },
)
