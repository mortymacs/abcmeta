"""Test for abcmeta library.

Test for multiple errors.
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

    @abstractmethod
    def method_5(self, name: Text, age: int) -> Tuple[Text, Text]:
        """Abstract method."""



class ABCDerived(ABCParent):
    def method_(self, name, age): # Intentional typo (Same error as Test 1)
        pass

    def method_2(self, name: int, age: int) -> Dict[Text, Text]:  # New
        return {"name": "test"}

    def method_4(self, family: Text, age: int) -> Tuple[Text, Text]:  # Test 4
        return ("name", "test")

    def method_5(self, name: Text, age: int) -> str:
        """Abstract method."""

