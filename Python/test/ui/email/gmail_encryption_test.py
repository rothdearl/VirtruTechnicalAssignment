import os
import unittest
from typing import final

from test import TestGroups
from test.ui.util import UIGlobals as Test
from test.util import TestUtils


@final
@unittest.skipUnless(TestGroups.is_in_test_groups("encryption", "gmail", "ui"), "Not in test groups.")
class GmailEncryptionTest(unittest.TestCase):
    """
    Tests encrypted emails via Gmail.
    """

    def test_send_encrypted_email(self) -> None:
        """
        Tests sending an encrypted email.
        :return: None
        """
        from test.ui.email import GmailPage  # Avoid circular import.
        gmail = GmailPage()

        gmail.navigate_to()

        # Validate the Gmail loaded.
        self.assertEqual("Gmail", Test.webdriver.title)

        gmail.log_in(os.getenv("LOGIN_EMAIL"), os.getenv("LOGIN_PASSWORD"))

        TestUtils.pause_test(5, message="Pausing to demonstrate Gmail is being blocked.")
