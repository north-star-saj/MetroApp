# MetroApp
Web Application that displays Minneapolis Metro Transit bus line information.

# How to run

Currently, the code is developed and tested on localhost.
I recommend using Docker. However, it *should* work to run from a Python venv (follow the Developer's Guide if this is desired).

The following was ran on Windows 10; however, it is expected to work on Linux or MacOS. It assumes the current working directory is this project (MetroApp).

1. `docker build --rm --pull -f "Dockerfile" --label "metrobuild" -t "metroapp:latest" .`
2. `docker run -dt -P --name "metroapp-dev" -e "FLASK_APP=metro" --label "metrobuild" "metroapp:latest"`
3. `docker port metroapp-dev`

Use the port identified in step three when opening in browser.
E.g. `http://localhost:49162/`.

# API

Three endpoints exist (left). These generally map to the corresponding NexTrip API endpoints (right) (see [Swagger NexTripAPI](https://svc.metrotransit.org/swagger/index.html) for more info on their API):
* `/` -> `/nextripv2/routes`
* `/direction/<id>` -> `/nextripv2/directions/{route_id}`
* `/stops/<route_id>/<direction_id>` -> `/nextripv2/stops/{route_id}/{direction_id}`

# Developers Guide

## Setup

For the developers guide, I will assume the use of VSCode (for convenience).

**Code Development**

I recommend developing the code in a python virtual environment.
This enables easy usage of flake8, black, and isort pre-commit hooks and minimal startup time (assumes Python 3.10 is already installed).
I've done a development Docker container with pre-commit hooks installed in the past, but have found it to be sometimes more expensive than needed.

In cmd terminal or terminal of choice (syntax may vary):
1. `py -m venv venv`
2. `./ venv/Scripts/activate`
3. `pip install -r requirements-dev.txt`
4. `pre-commit install`

Debugging code options:

* (Auto Opens Browser) Use VSCode's defined launcher via F5: "Docker: Python - Flask". 
  This will startup a Docker container and direct your browser to the Flask app.
* (http://127.0.0.1:5000/) Run the following commands in Windows CMD or equivalent commands in terminal of choice:
  * `set FLASK_APP=metro`
  * `flask run`

Unit Testing:

Currently, only pytests via the Python venv are supported.
To run the pytests, activate the virtual env and then execute the following in terminal from the MetroApp directory:

`pytest tests`

**Note:** The third-party APIs are mocked to ensure unit test autonomy.
  
# TODO:

Quite a bit of items belong in this category. Much of which is likely required prior to production.

* Beautify the user interface.
* Update testing to occur on the Docker container (currently tests were only performed via venv).
* Peer reviews (pull requests).
* Stored builds for rollbacks.
* Include in pipeline (repo, build, testing, staging, production)
* Implement further testing including expanded unit tests, performance, and system tests.
* Expand on features.

# Assumptions

* Sticking to requirements, we can assume that there's no need to check times.
* Assumed no default value requirements.
* That it's sufficient to only update the Routes by refreshing the page.
* Data is assumed valid; e.g. no checking for bad responses from Metro's API.
* This is a standalone application.
* Minimum performance requirements.
* No need to maintain a database or user information.
* No HTTPS requirements nor any security requirements.