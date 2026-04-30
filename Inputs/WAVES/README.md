# WAVES: Wind Asset Value Estimation System
[![PyPI version](https://badge.fury.io/py/waves.svg)](https://badge.fury.io/py/waves)
[![PyPI downloads](https://img.shields.io/pypi/dm/waves?link=https%3A%2F%2Fpypi.org%2Fproject%2FWAVES%2F)](https://pypi.org/project/WAVES/)
[![Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![image](https://img.shields.io/pypi/pyversions/waves.svg)](https://pypi.python.org/pypi/waves)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/NREL/WAVES/main?filepath=examples)
[![Jupyter Book](https://jupyterbook.org/badge.svg)](https://nrel.github.io/WAVES)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## Overview

Runs analyses for offshore wind projects by utilizing ORBIT (CapEx), WOMBAT (OpEx), and FLORIS (AEP)
to estimate the lifecycle costs using NREL's flagship technoeconomic models.

This instance of WAVES is configured for the **IEA Wind Task 49 Deep Semi-Submersible Reference Array**
design study. Please visit the [documentation site](https://nrel.github.io/WAVES/) for general API
documentation, a reference guide, and examples.

## Requirements

Python 3.10+, preferably 3.12

## Environment Setup

Download the latest version of [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
for the appropriate OS. Follow the remaining [steps](https://conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation)
for the appropriate OS version.

Using conda, create a new virtual environment:

```console
conda create -n <environment_name> python=3.12
conda activate <environment_name>
conda install -c anaconda pip
conda config --set pip_interop_enabled true
# to deactivate
conda deactivate
```

## Installation

Requires Python 3.10+.

Clone the IEA Task 49 Reference Array repository, navigate to the WAVES sub-directory, and install
from source:

```bash
git clone https://github.com/IEAWindTask49/Reference_Array_Deep_Semi
cd Reference_Array_Deep_Semi/Inputs/WAVES
pip install .
```

For an editable installation (recommended if you plan to modify the underlying code):

```bash
pip install -e .
```

## Project Inputs

All WAVES input files for the IEA Task 49 Deep Semi-Submersible design case are located under:

```
Inputs/WAVES/library/iea-task-49-deep-design/
```

Browse the full input library on GitHub:
[`Inputs/WAVES/library/iea-task-49-deep-design`](https://github.com/IEAWindTask49/Reference_Array_Deep_Semi/tree/main/Inputs/WAVES/library/iea-task-49-deep-design)

## Running the Example

A Jupyter Notebook that runs the full IEA Task 49 Deep Semi-Submersible case end-to-end is
provided at:

```
Inputs/WAVES/examples/iea-task-49-deep-design-notebook.ipynb
```

Open it directly on GitHub:
[`iea-task-49-deep-design-notebook.ipynb`](https://github.com/IEAWindTask49/Reference_Array_Deep_Semi/blob/main/Inputs/WAVES/examples/iea-task-49-deep-design-notebook.ipynb)

To run the notebook locally, install the examples dependencies first:

```bash
pip install ".[examples]"
jupyter notebook Inputs/WAVES/examples/iea-task-49-deep-design-notebook.ipynb
```

## Usage

After installation, the package can be imported:

```console
python
import waves
waves.__version__
```

### CLI

```console
waves library-path configuration1.yaml configuration2.yaml
```