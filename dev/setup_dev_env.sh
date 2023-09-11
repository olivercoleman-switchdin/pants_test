#!/bin/bash

# Sets up the development environment for this repo (in the docker container).

# Setup Pants venv (see https://www.pantsbuild.org/v2.16/docs/setting-up-an-ide#python-third-party-dependencies-and-tools)
rm -r $VENV_PATH || true
pants --no-pantsd export --py-resolve-format=symlinked_immutable_virtualenv --resolve=python-default
