from datetime import datetime
from typing import final


@final
class DateUtils:
    """
    Utility class for dates.
    """

    @staticmethod
    def to_iso_string(date: datetime.date) -> str:
        """
        Returns an ISO 8601 formatted string representation of the date.
        :param date: The date to format.
        :return: A string.
        """
        # Return date without milliseconds.
        return f"{date.isoformat()[:-7]}Z"
