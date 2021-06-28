"""Unit test for abstractmethod library."""
from typing import Dict, List, Text, Tuple

from abstractmethod import ABCMeta, abstractmethod


class Parent(ABCMeta):
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


class Derived(Parent):
    def method_1(self, name, age):
        pass

    def method_2(self, name: Text, age: int) -> Dict[Text, Text]:
        return {"name": "test"}

    def method_4(self, name: Text, age: int) -> Tuple[Text, Text]:
        return ("name", "test")
