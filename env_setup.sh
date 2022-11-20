#!/bin/bash

python3 -m pip install --user virtualenv
python3 -m venv ./venv
source ./venv/bin/activate
pip3 install -r requirments.txt
