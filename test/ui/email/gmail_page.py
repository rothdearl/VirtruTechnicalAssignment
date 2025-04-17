from typing import final

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from test.ui import WebElementUtils, WebPage
from test.util import TestUtils


@final
class GmailPage(WebPage):
    """
    A class for accessing Gmail.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance.
        """
        super().__init__("https://mail.google.com/mail/")

    @staticmethod
    def log_in(email: str, password: str) -> None:
        """
        Logs in to Gmail.
        :param email: The email to log in with.
        :param password: The password to log in with.
        :return: None
        """
        email_field = WebElementUtils.find_element(By.TAG_NAME, "input")

        WebElementUtils.send_keys(email_field, email)
        WebElementUtils.send_keys(email_field, Keys.ENTER)

        # FIXME: Gmail is preventing the next step in the log in process.

    def wait_for_page_to_load(self) -> None:
        """
        Waits for the page to load.
        :return: None
        """
        TestUtils.pause_test(1, message=f"Loading {self.absolute_path}")
