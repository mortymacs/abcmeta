# abcmeta
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/mortymacs/abcmeta/Python%20package)](https://github.com/mortymacs/abcmeta/actions/workflows/python-test.yml)
[![PyPi version](https://badgen.net/pypi/v/abcmeta/)](https://pypi.org/project/abcmeta)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/abcmeta.svg)](https://pypi.python.org/pypi/abcmeta/)
[![PyPI version fury.io](https://badge.fury.io/py/abcmeta.svg)](https://pypi.python.org/pypi/abcmeta/)
[![PyPI download month](https://img.shields.io/pypi/dm/abcmeta.svg)](https://pypi.python.org/pypi/abcmeta/)

Python meta class and abstract method library with restrictions.

This library provides a restricted way to validate abstract methods.
The Python's default abstract method library only validates the methods
that exist in the derived classes and nothing else.
What this library provides is apart from that validation it provides
validations over the method's signature.
All you need is to import `ABCMeta` and `abstractmethod` from this library.

It works on both annotations and without annotations methods.

### Installation

You can install the package by `pip`:

```bash
$ pip install abcmeta
```

> Note: abcmeta supports Python3.6+.

### Quick start

```python
from typing import Dict, Text

from abcmeta import ABC, abstractmethod


class Base(ABC):
    @abstractmethod
    def method_2(self, name: Text, age: int) -> Dict[Text, Text]:
        """Abstract method."""

    @abstractmethod
    def method_3(self, name, age):
        """Abstract method."""

class Drived(Base):
    def method_2(self, name: Text, age: int) -> Dict[Text, Text]:
        return {"name": "test"}

    def method_3(self, name, age):
        pass
```

If you put a different signature, it will raise an error with 'diff' format with hints about what you've missed:

```python
class Drived(Base):
    def method_2(self, name: Text, age: int) -> List[Text]:
        return {"name": "test"}
```

And it will raise:

```python
Traceback (most recent call last):
  File "/Workspaces/test.py", line 41, in <module>
    class Drived(Base):
  File "/usr/lib/python3.9/abc.py", line 85, in __new__
    cls = super().__new__(mcls, name, bases, namespace, **kwargs)
  File "/abcmeta/__init__.py", line 179, in __init_subclass__
    raise AttributeError(
AttributeError: Signature of the derived method is not the same as parent class:
- method_2(self, name: str, age: int) -> Dict[str, str]
?                                        ^ ^     -----

+ method_2(self, name: str, age: int) -> List[str]
?                                        ^ ^

Derived method expected to return in 'typing.Dict[str, str]' type, but returns 'typing.List[str]'
```

For different parameter names:

```python
class Drived(Base):
    def method_2(self, username: Text, age: int) -> List[Text]:
        return {"name": "test"}
```

And it will raise:

```python
Traceback (most recent call last):
  File "/Workspaces/test.py", line 41, in <module>
    class Drived(Base):
  File "/usr/lib/python3.9/abc.py", line 85, in __new__
    cls = super().__new__(mcls, name, bases, namespace, **kwargs)
  File "/abcmeta/__init__.py", line 180, in __init_subclass__
    raise AttributeError(
AttributeError: Signature of the derived method is not the same as parent class:
- method_2(self, name: str, age: int) -> Dict[str, str]
+ method_2(self, username: str, age: int) -> Dict[str, str]
?                ++++

Derived method expected to get name paramter, but gets username
```

### Issue

If you're faced with a problem, please file an [issue](https://github.com/mortymacs/abcmeta/issues/new) on Github.


### Contribute

You're always welcome to contribute to the project! Please file an issue and send your great PR.

### License

Please read the [LICENSE](./LICENSE) file.
