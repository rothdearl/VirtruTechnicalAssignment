from typing import final

from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions

from test.ui.util import UIGlobals as Test
from test.util import Logger, TestUtils


@final
class WebElementUtils:
    """
    Utility class for executing and logging actions for web elements.
    """

    @staticmethod
    def clear_browser_cookies() -> None:
        """
        Clears all browser cookies.
        :return: None
        """
        Logger.info("Clearing browser cookies...")
        Test.webdriver.delete_all_cookies()
        Logger.info("Browser cookies cleared.")

    @staticmethod
    def click(element: WebElement) -> None:
        """
        Clicks an element.
        :param element: The element to click.
        :return: None
        """
        info = WebElementUtils.get_element_info(element)

        Logger.info(f"Clicking: {info}")
        WebElementUtils.wait_for_element(element)
        element.click()
        Logger.info(f"Element clicked: {info}")

    @staticmethod
    def close_opened_windows() -> None:
        """
        Closes all opened windows except the initial window.
        :return: None
        """
        windows = Test.webdriver.window_handles

        # Close all windows/tabs except the initial window.
        for i, window in enumerate(windows):
            if i:
                WebElementUtils.close_window(window)

        # Load the initial window/tab.
        WebElementUtils.switch_to_window(windows[0])

    @staticmethod
    def close_window(window: str) -> None:
        """
        Closes the window.
        :param window: The window to close.
        :return: None
        """
        Logger.info(f"Closing window: {window}")
        WebElementUtils.switch_to_window(window)
        Test.webdriver.close()

    @staticmethod
    def find_element(by: str, value: str, *, retries: int = 0) -> WebElement:
        """
        Finds an element within the default context.
        :param by: The means to locate the element by.
        :param value: The locator value.
        :param retries: The number of times to retry when the element is not found.
        :return: A web element.
        """
        return WebElementUtils.find_element_within_context(Test.webdriver, by, value, retries=retries)

    @staticmethod
    def find_element_within_context(context: WebElement, by: str, value: str, *, retries: int = 0) -> WebElement:
        """
        Finds an element within the context.
        :param context: The context to find within.
        :param by: The means to locate the element by.
        :param value: The locator value.
        :param retries: The number of times to retry when the element is not found.
        :return: A web element.
        """
        attempt = 0
        element = None

        while attempt <= retries:
            if attempt > 0:
                Logger.info(f"Retry {attempt} of {retries}")

            try:
                attempt += 1
                Logger.info(f"Finding element: {WebElementUtils.get_locator_info(by, value)}")
                element = context.find_element(by, value)
                Logger.info(f"Element found: {WebElementUtils.get_element_info(element)}")
                break
            except NoSuchElementException:
                Logger.warning("Unable to find element.")

        return element

    @staticmethod
    def find_elements(by: str, value: str, *, retries: int = 0) -> list[WebElement]:
        """
        Finds an element within the default context.
        :param by: The means to locate the element by.
        :param value: The locator value.
        :param retries: The number of times to retry when the element is not found.
        :return: A web element.
        """
        return WebElementUtils.find_elements_within_context(Test.webdriver, by, value, retries=retries)

    @staticmethod
    def find_elements_within_context(context: WebElement, by: str, value: str, *, retries: int = 0) -> list[WebElement]:
        """
        Finds elements within the context.
        :param context: The context to find within.
        :param by: The means to locate the elements by.
        :param value: The locator value.
        :param retries: The number of times to retry when the elements are not found.
        :return: A list of web element.
        """
        attempt = 0
        elements = None

        while attempt <= retries:
            if attempt > 0:
                Logger.info(f"Retry {attempt} of {retries}")

            try:
                Logger.info(f"Finding elements: {WebElementUtils.get_locator_info(by, value)}")
                elements = context.find_elements(by, value)
                Logger.info(f"Elements {('not found' if not elements else 'found')}.")
                break
            except NoSuchElementException:
                Logger.warning("Unable to find elements.")

        return elements

    @staticmethod
    def get_element_info(element: WebElement) -> str:
        """
        Returns the element info.
        :param element: The element to get the info for.
        :return: The element info.
        """
        return f"<{element.tag_name}:{element.aria_role}>"

    @staticmethod
    def get_locator_info(locator: str, value: str) -> str:
        """
        Returns the locator info.
        :param locator: The means to find the element by.
        :param value: The locator value.
        :return: The locator info.
        """
        return f"<By.{locator}={value}>"

    @staticmethod
    def is_hidden(element: WebElement) -> bool:
        """
        Returns true if the element is a hidden element.
        :param element: The element to check.
        :return: True or false.
        """
        is_hidden = False

        if element.value_of_css_property("display") == "none" or element.value_of_css_property(
                "opacity") == "0" or element.value_of_css_property("visibility") == "hidden":
            is_hidden = True

        return is_hidden

    @staticmethod
    def load_url(url: str, seconds: int = 0) -> None:
        """
        Loads the URL.
        :param url: The URL to load.
        :param seconds: The number of seconds to wait for the page to load.
        :return: None
        """
        Logger.info(f"Loading URL: {url}")
        Test.webdriver.get(url)
        TestUtils.pause_test(seconds, message="Waiting for page to load...")

    @staticmethod
    def send_keys(element: WebElement, keys: str) -> None:
        """
        Sends the keys to the element.
        :param element: The element to send the keys to.
        :param keys: The keys to send.
        :return: None
        """
        info = WebElementUtils.get_element_info(element)

        Logger.info(f"Sending keys [{repr(keys)}] to: {info}")
        WebElementUtils.wait_for_element(element)
        element.send_keys(keys)
        Logger.info(f"Keys sent to: {info}")

    @staticmethod
    def switch_to_default_content() -> None:
        """
        Switches to either the first frame on the page or the main document.
        :return: None
        """
        Logger.info("Switching content to default...")
        Test.webdriver.switchto.default_content()
        Logger.info("Content switched.")

    @staticmethod
    def switch_to_frame(element: WebElement) -> None:
        """
        Switches to the frame.
        :param element: The frame to switch to.
        :return: None
        """
        Logger.info(f"Switching content to: {WebElementUtils.get_element_info(element)}")
        Test.webdriver.switch_to.frame(element)
        Logger.info("Content switched.")

    @staticmethod
    def switch_to_window(window: str) -> None:
        """
        Switches to the window.
        :param window: The window to switch to.
        :return: None
        """
        Logger.info(f"Switching to window: {window}")
        Test.webdriver.switch_to.window(window)
        Logger.info("Window switched.")

    @staticmethod
    def wait_for_element(element: WebElement) -> None:
        """
        Waits for an element to be ready.
        :param element: The element to wait for.
        :return: None
        """
        # Don't wait for elements that are intended to be hidden.
        if not WebElementUtils.is_hidden(element):
            try:
                Logger.info(f"Waiting for element {WebElementUtils.get_element_info(element)} to be ready.")
                Test.webdriver_wait.until(expected_conditions.visibility_of(element))
                Test.webdriver_wait.until(expected_conditions.element_to_be_clickable(element))
                Logger.info("Element is ready.")
            except NoSuchElementException:
                Logger.warning("Unable to find element.")
