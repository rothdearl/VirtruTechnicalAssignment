from abc import ABC, abstractmethod
from typing import final

from test.ui import WebElementUtils
from test.ui.util import UIGlobals


class WebPage(ABC):
    """
    A parent class for all classes that represent a web page.
    """

    @abstractmethod
    def __init__(self, path) -> None:
        """
        Initializes a new instance.
        :param path: The path to the page relative to the host.
        """
        self.path = path

    @final
    @property
    def absolute_path(self) -> str:
        """
        Returns the absolute path to the page.
        :return: The absolute path to the page.
        """
        return UIGlobals.host + self.path

    @final
    @property
    def name(self) -> str:
        return type(self).__name__

    @final
    def navigate_to(self) -> None:
        """
        Navigates to the page.
        :return: None
        """
        WebElementUtils.load_url(self.absolute_path)
        self.wait_for_page_to_load()

    def wait_for_page_to_load(self) -> None:
        """
        Waits for the page to load.
        :return: None
        """
