import time
from typing import final

from test.util import Logger


@final
class TestUtils:
    """
    Utility class for generic test operations.
    """

    @staticmethod
    def pause_test(seconds: int = 0, *, message: str = None) -> None:
        """
        Pauses the test.
        :param seconds: The number of seconds to pause.
        :param message: An optional message to log.
        :return: None
        """
        if seconds > 0:
            if message:
                Logger.info(message)

            Logger.info(f"Pausing test for {seconds} seconds.")
            time.sleep(seconds)
            Logger.info("Test resuming.")
