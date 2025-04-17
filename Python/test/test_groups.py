import os
from typing import final


@final
class TestGroups:
    """
    A class to manage test groups.
    """

    @staticmethod
    def get_test_groups() -> list[str]:
        """
        Returns the test groups.
        :return: The test groups.
        """
        test_groups = os.getenv("TEST_GROUPS")

        return [group.strip() for group in test_groups.split(",")] if test_groups else []

    @staticmethod
    def is_in_test_groups(*groups: str) -> bool:
        """
        Returns true if the TEST_GROUPS environment variable is not set or any group is in TEST_GROUPS.
        :param groups: The list of groups to check.
        :return: True or false.
        """
        has_match = True

        if test_groups := TestGroups.get_test_groups():
            for group in groups:
                if group in test_groups:
                    has_match = True
                    break
            else:
                has_match = False

        return has_match
