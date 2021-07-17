"""Unit test for abcmeta library."""
from typing import Dict, Text, Tuple

from abcmeta import ABCMeta, abstractmethod


class ABCMetaParent(ABCMeta):
    @abstractmethod
    def method_1(self, name, age):
        pass

    @abstractmethod
    def method_2(self, name: Text, age: int) -> Dict[Text, Text]:
        """Abstract method."""

    def method_3(self):
        pass

    @abstractmethod
    def method_4(self, name: Text, age: int) -> Tuple[Text, Text]:
        """Abstract method."""


class ABCMetaDerived(ABCMetaParent):
    def method_1(self, name, age):
        pass

    def method_2(self, name: Text, age: int) -> Dict[Text, Text]:
        return {"name": "test"}

    def method_4(self, name: Text, age: int) -> Tuple[Text, Text]:
        return ("name", "test")
