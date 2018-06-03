#!/usr/bin/env python3
'''
Basic tests for layouts repo

Used to validate whether the JSON files can be read and processed.
'''

## Imports

import os

import layouts


## Test

# Determine this scripts directory
script_dir = os.path.dirname(os.path.realpath(__file__))

# Load layouts of this repository
mgr = layouts.Layouts(layout_path=os.path.join(script_dir, ".."))

# Print out a list of layouts
# Doing this requires loading all of the JSON files, and reading the name field
for layout, path in sorted(mgr.layout_names.items()):
    print(layout, path)

