# MetroApp
Web Application that displays Minneapolis Metro Transit bus line information.

# How to run

Currently, the code is developed and tested on localhost.
I recommend following the steps under the Docker section since Docker mitigates differences in environments.
## Docker (Recommended)

## Venv

# Developers Guide

## Setup

For the developers guide, I will assume the use of VSCode (for convenience).

**Code Development**

I recommend writing out the code in a python virtual environment.
This enables easy usage of flake8, black, and isort pre-commit hooks and minimal startup time (assumes Python 3.10 is already installed).

In cmd terminal or terminal of choice (syntax may vary):
1. `py -m venv venv`
2. `./ venv/Scripts/activate`
3. `pip install -r requirements-dev.txt`
4. `pre-commit install`

When it's time to execute code, use the defined launcher via F5: "Docker: Python - Flask". This will startup a Docker container and direct your browser to the Flask app.