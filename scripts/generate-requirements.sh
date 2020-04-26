#!/usr/bin/env bash

pipenv lock -r > requirements.txt
pipenv lock -r -d > dev-requirements.txt