import configparser
import os
from typing import final

from definitions import OPTIONS_DIR
from test.util import Logger, TestGlobals as Test


@final
class TestOptions:
    """
    Utility class for accessing test options.
    """

    @staticmethod
    def get_bool_option(section: str, option: str) -> bool:
        """
        Gets an option. The default value is false.
        :param section: The section name.
        :param option: The option name.
        :return: An option.
        """
        value = TestOptions.get_with_default(section, option, default_value="False").upper()

        return value == "TRUE"

    @staticmethod
    def get_int_option(section: str, option: str) -> int:
        """
        Gets an option. The default value is 0.
        :param section: The section name.
        :param option: The option name.
        :return: An option.
        """
        value = TestOptions.get_with_default(section, option, default_value="0")

        return int(value) if value else 0

    @staticmethod
    def get_option(section: str, option: str) -> str:
        """
        Gets an option. The default value is an empty string.
        :param section: The section name.
        :param option: The option name.
        :return: An option.
        """
        return TestOptions.get_with_default(section, option, default_value="")

    @staticmethod
    def get_options(section: str, option: str) -> list[str]:
        """
        Returns a list of options. The default value is an empty list.
        :param section: The section name.
        :param option: The option name.
        :return: A list of options.
        """
        value = TestOptions.get_with_default(section, option, default_value="")

        return [split.strip() for split in value.split(",")] if value else []

    @staticmethod
    def get_with_default(section: str, option: str, *, default_value: str) -> str:
        """
        Gets an option.
        :param section: The section name.
        :param option: The option name.
        :param default_value: The default value.
        :return: An option.
        """
        value = default_value

        try:
            value = Test.options.get(section, option)
            Logger.info(f"Getting option <{option} = {value}> from section [{section}].")
        except (configparser.NoSectionError, configparser.NoOptionError):
            Logger.warning(f"Section [{section}] with option <{option}> not found.")

        return value

    @staticmethod
    def load_options(file: str) -> None:
        """
        Loads options from the file.
        :param file: The file to load the options from.
        :return: None
        :raises ValueError: If the file does not exist.
        """
        file = os.path.join(OPTIONS_DIR, file)

        if not file or not os.path.exists(file):
            Logger.error(f"Options file [{file}] does not exist.")
            raise FileNotFoundError

        Logger.info(f"Loading options file: [{file}]")
        Test.options = configparser.ConfigParser()
        Test.options.read(file)
        Logger.info("Options file loaded.")
