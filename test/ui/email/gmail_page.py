from typing import final

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from test.ui import WebPage
from test.ui.util import WebElementUtils


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

    def log_in(self, email: str, password: str) -> None:
        """
        Logs in to Gmail.
        :param email: The email to log in with.
        :param password: The password to log in with.
        :return: None
        """
        email_field = WebElementUtils.find_element(By.TAG_NAME, "input")

        WebElementUtils.send_keys(email_field, email, hide_log_output=True)
        WebElementUtils.send_keys(email_field, Keys.ENTER)

        # FIXME: Gmail is preventing the next step in the log in process.
        # TODO: Enter password and submit.

    def open_email(self, *, row: int = 0) -> None:
        """
        Opens an email.
        :param row: The row number corresponding to the email to open.
        :return: None
        """
        # TODO: Select the email corresponding to the row number.

    def send_email(self, *, to: str, subject: str, message: str, enable_email_protection: bool = False) -> None:
        """
        Composes and sends a new email.
        :param to: The email recipient.
        :param subject: The email subject.
        :param message: The email message.
        :param enable_email_protection: Whether to enable email protection.
        :return: None
        """
        # TODO: Compose a new email.
        # TODO: Enter the recipient, subject and message.
        # TODO: Enable email protection?
        # TODO: Send email.
