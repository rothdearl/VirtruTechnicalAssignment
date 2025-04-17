from typing import final

from selenium import webdriver
from selenium.webdriver.common.options import ArgOptions

from test.ui.util import WebBrowsers
from test.util import Logger, TestOptions


@final
class WebDriverFactory:
    """
    Factory class for creating web driver instances.
    """

    @staticmethod
    def _set_headless(options: ArgOptions) -> None:
        """
        Sets whether the driver will run headless.
        :param options: The driver options.
        :return: None
        """
        if TestOptions.get_bool_option("driver", "headless"):
            options.add_argument("--headless")

    @staticmethod
    def get_webdriver_instance(browser: int | str | WebBrowsers) -> webdriver:
        """
        Returns a web driver instance.
        :param browser: The browser to create a driver for.
        :return: A web driver instance.
        :raises ValueError: If the browser is not supported.
        """
        if isinstance(browser, str):
            browser = browser.upper()

        Logger.info(f"Creating WebDriver for [{browser}]...")

        match browser:
            case WebBrowsers.CHROME | WebBrowsers.CHROME.name | WebBrowsers.CHROME.value:
                options = webdriver.ChromeOptions()
                WebDriverFactory._set_headless(options)
                driver = webdriver.Chrome(options=options)
            case WebBrowsers.EDGE | WebBrowsers.EDGE.name | WebBrowsers.EDGE.value:
                options = webdriver.EdgeOptions()
                WebDriverFactory._set_headless(options)
                driver = webdriver.Edge(options=options)
            case WebBrowsers.FIREFOX | WebBrowsers.FIREFOX.name | WebBrowsers.FIREFOX.value:
                options = webdriver.FirefoxOptions()
                WebDriverFactory._set_headless(options)
                driver = webdriver.Firefox(options=options)
            case _:
                Logger.error(f"Unsupported Web Browser: [{browser}]")
                raise ValueError

        # Configure driver.
        driver.maximize_window()
        driver.implicitly_wait(TestOptions.get_int_option("driver", "wait.timeout"))

        Logger.info("WebDriver created.")

        return driver
