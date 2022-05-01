"""Test for abcmeta library.

different return type in the derived class.
"""
from typing import Dict, Text, Tuple

from abcmeta import ABC, abstractmethod


class ABCParent(ABC):
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


class ABCDerived(ABCParent):
    def method_1(self, name, age):
        pass

    def method_2(self, name: Text, age: int) -> Dict[Text, int]:
        return {"name": "test"}

    def method_4(self, name: Text, age: int) -> Tuple[Text, Text]:
        return ("name", "test")
