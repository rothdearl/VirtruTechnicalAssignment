from enum import Enum
from typing import final


@final
class WebBrowsers(int, Enum):
    """
    Enum constants for the supported web browsers.
    """
    CHROME = 0
    EDGE = 1
    FIREFOX = 2
