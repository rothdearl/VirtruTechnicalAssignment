#!/bin/bash

# Set the test options file.
export TEST_OPTIONS_FILE=

# Set the test path.
TEST_PATH="test.ui"

# Run tests.
if [ "$#" -eq 0 ]; then
    echo "Test group required."
else
    export TEST_GROUPS="$*"

    python3 -m unittest discover -t ../ ${TEST_PATH} -q
fi
