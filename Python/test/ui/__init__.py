# __init__.py

"""
Initialization file for the UI tests package.
"""

import os
import unittest
from typing import Final, final

from selenium.webdriver.support.wait import WebDriverWait

from test import TestGroups
from test.ui.util import UIGlobals as Test, WebDriverFactory, WebElementUtils
from test.util import Logger, TestOptions
from .web_page import WebPage

# The default options file.
_DEFAULT_OPTIONS_FILE: Final[str] = "ui-default.ini"


@final
class TestInitializer(object):
    """
    A class to start and stop the UI tests.
    """

    @staticmethod
    def _close_browser() -> None:
        """
        Closes the browser.
        :return: None
        """
        Logger.info("Closing browser...")
        Test.webdriver.quit()
        Test.webdriver = None
        Test.webdriver_wait = None
        Logger.info("Browser closed.")

    @staticmethod
    def _init_test_globals(options_file: str) -> None:
        """
        Initializes the global variables used by the tests.
        :param options_file: The options file.
        :return: None
        """
        try:
            TestOptions.load_options(options_file)
            Test.browser = TestOptions.get_option("driver", "browser")
            Test.host = TestOptions.get_option("test", "host")
            Test.webdriver = WebDriverFactory.get_webdriver_instance(Test.browser)
            Test.webdriver_wait = WebDriverWait(Test.webdriver, TestOptions.get_int_option("driver", "wait.timeout"))
        except ValueError:
            Logger.error("Force stopping tests due to an initialization error.")
            raise SystemExit()

    @classmethod
    def start_test_run(cls) -> None:
        """
        Sets up the tests.
        :return: None
        """
        # Get the test options file.
        options_file = os.getenv("TEST_OPTIONS_FILE")

        if not options_file:
            options_file = _DEFAULT_OPTIONS_FILE

        TestInitializer._init_test_globals(options_file)

        # Log important test options.
        Logger.info(f"Starting tests with the following options from: [{options_file}]")
        Logger.info(f"Test browser: [{Test.browser}]")
        Logger.info(f"Test host: [{Test.host}]")
        Logger.info(f"Test groups: {TestGroups.get_test_groups()}")

    @classmethod
    def stop_test_run(cls) -> None:
        """
        Shutdowns all processes and closes all resources after the tests have finished.
        :return: None
        """
        WebElementUtils.clear_browser_cookies()
        TestInitializer._close_browser()


# Hook in the test start and test stop.
setattr(unittest.TestResult, 'startTestRun', TestInitializer.start_test_run)
setattr(unittest.TestResult, 'stopTestRun', TestInitializer.stop_test_run)
