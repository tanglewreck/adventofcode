#!/usr/bin/env bash
# shellcheck shell=bash
# Start ipython using a local .ipython
PROJDIR="$HOME/Proj/adventofcode"
IPYTHONDIR_="$PROJDIR/.ipython"
if [ -d "$IPYTHONDIR_" ]; then
    IPYTHONDIR="$IPYTHONDIR_" ipython --profile=default --pylab
else
    echo "No .ipython dir found ($IPYTHONDIR_): FAIL"
    exit 1
fi
exit 0
