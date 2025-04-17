from typing import final

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@final
class UIGlobals:
    """
    Utility class to hold data for the entire UI test package.
    """
    browser: str
    host: str
    webdriver: webdriver
    webdriver_wait: WebDriverWait | None
