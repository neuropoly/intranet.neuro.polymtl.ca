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
            "furo",
            "sphinx-panels",
            "sphinx-inline-tabs",
            # pinned because of this bug https://github.com/pydata/pydata-sphinx-theme/pull/509
            # and that the patched sphinx-book-theme isn't out yet: https://github.com/executablebooks/sphinx-book-theme/issues/428#issuecomment-966021270
            "sphinx~=4.2.0", # TODO: unpin when the next sphinx-book-theme is released
        ],
    },
)
