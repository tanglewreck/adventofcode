#!/usr/bin/env bash
# shellcheck shell=bash
# Start ipython using a local .ipython
PROJDIR="$HOME/Proj/adventofcode"
export IPYTHONDIR="$PROJDIR/.ipython"
export PYLINTRC="$PROJDIR/pylintrc"
if [ -d "$IPYTHONDIR" ]; then
    ipython --profile="$(hostname -s)" --pylab
else
    echo "No .ipython dir found ($IPYTHONDIR): FAIL"
    exit 1
fi
exit 0
