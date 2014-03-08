#!/bin/bash

rm docs/ansicolor.rst docs/modules.rst
sphinx-apidoc -o docs ansicolor
cd docs && \
    make html
