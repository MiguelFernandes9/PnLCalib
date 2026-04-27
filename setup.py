"""Minimal setup.py shim so this repo is pip-installable.

Forked from mguti97/PnLCalib (GPL-2.0). This shim is added solely to enable
`pip install git+https://github.com/MiguelFernandes9/PnLCalib@<sha>` for
downstream consumption by the futPuzzle video pipeline. No upstream source
files are modified.
"""
from setuptools import setup, find_packages


setup(
    name="pnlcalib",
    version="0.0.0+fork.1",
    description="Pip-installable shim over mguti97/PnLCalib (GPL-2.0).",
    long_description=__doc__,
    long_description_content_type="text/plain",
    url="https://github.com/MiguelFernandes9/PnLCalib",
    license="GPL-2.0",
    py_modules=["inference", "train", "train_l", "eval_wp"],
    packages=find_packages(include=["model", "model.*", "utils", "utils.*", "config", "config.*"]),
    python_requires=">=3.10",
    install_requires=[
        "torch",
        "torchvision",
        "numpy",
        "opencv-python-headless",
        "matplotlib",
        "tqdm",
        "lsq-ellipse",
        "scikit-learn",
    ],
)
