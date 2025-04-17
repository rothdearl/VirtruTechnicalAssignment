import os
from typing import Final

# Define directory paths.
_CURRENT_DIR: Final[str] = os.path.dirname(__file__)
OPTIONS_DIR: Final[str] = os.path.join(_CURRENT_DIR, "ini")
PROJECT_ROOT_DIR: Final[str] = _CURRENT_DIR
TEST_ROOT_DIR: Final[str] = os.path.join(_CURRENT_DIR, "test")

# Define OS constants.
OS_IS_POSIX: Final[bool] = os.name == "posix"
OS_IS_WINDOWS: Final[bool] = os.name == "nt"
