from configparser import ConfigParser
from typing import final


@final
class TestGlobals:
    """
    Utility class to hold data for the entire test project.
    """
    options: ConfigParser  # The options provided by a configuration file.
