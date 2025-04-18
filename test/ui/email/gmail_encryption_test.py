import os
import unittest
from typing import final

from test import TestGroups
from test.ui.util import WebElementUtils
from test.util import TestUtils


@final
@unittest.skipUnless(TestGroups.is_in_test_groups("encryption", "gmail", "ui"), "Not in test groups.")
class GmailEncryptionTest(unittest.TestCase):
    """
    Tests encrypted emails via Gmail.
    """

    @staticmethod
    def test_send_encrypted_email() -> None:
        """
        Tests sending an encrypted email.
        :return: None
        """
        from test.ui.email import GmailPage  # Avoid circular import.
        gmail = GmailPage()

        # Navigate to Gmail and log in.
        gmail.navigate_to()
        gmail.log_in(os.getenv("GMAIL_LOGIN_EMAIL"), os.getenv("GMAIL_LOGIN_PASSWORD"))

        TestUtils.pause_test(5, message="Pausing to demonstrate Gmail is being blocked.")

        # Compose and send a new email with email protection.
        gmail.send_email(to=os.getenv("GMAIL_LOGIN_EMAIL"), subject="Virtru Technical Assignment",
                         message="This is an encrypted message.", enable_email_protection=True)

        TestUtils.pause_test(5, message="Wait for the email to appear in the inbox.")
        WebElementUtils.refresh_page()

        # Open the newly sent email and verify it was encrypted.
        gmail.open_email(row=0)
        # TODO: Verify the email was encrypted.
