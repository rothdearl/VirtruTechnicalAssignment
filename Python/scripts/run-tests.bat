@echo off

:: Store variables locally.
setlocal

:: Set the test options file.
set TEST_OPTIONS_FILE=

:: Set the test path.
set TEST_PATH=test.ui

:: Run tests.
if "%~1"=="" (
    echo Test group required.
) else (
    set TEST_GROUPS=%*

    py -m unittest discover -t ..\ %TEST_PATH% -q
)
