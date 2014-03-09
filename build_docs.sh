#!/bin/bash

rm docs/ansicolor.rst docs/modules.rst
sphinx-apidoc --separate --output-dir docs ansicolor
cd docs && \
    make html
