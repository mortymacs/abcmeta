# abstractmethod

Python Abstract Method Decorator

This library provides a restricted way to validate abstract methods.
The Python's default abstract method library only validates the methods
that exist in the derived classes and nothing else.
What this library provides is apart from that validation it provides
validations over the method's signature.
All you need is to import 'ABCMeta' and 'abstractmethod' from this library.

### Quick start

```python
from typing import Dict, Text

from abstractmethod import ABCMeta, abstractmethod


class Base(ABCMeta):
    @abstractmethod
    def method_2(self, name: Text, age: int) -> Dict[Text, Text]:
        """Abstract method."""


class Drived(Base):
    def method_2(self, name: Text, age: int) -> Dict[Text, Text]:
        return {"name": "test"}
```

If you put a different signature, it will raise an error with 'diff' format with hints about what you've missed:

```python
class Drived(Base):
    def method_2(self, name: Text, age: int) -> List[Text]:
        return {"name": "test"}
```

And it will raise:

```
Traceback (most recent call last):
  File "/Workspaces/test.py", line 41, in <module>
    class Drived(Base):
  File "/usr/lib/python3.9/abc.py", line 85, in __new__
    cls = super().__new__(mcls, name, bases, namespace, **kwargs)
  File "/abcmethod/abstractmethod.py", line 179, in __init_subclass__
    raise AttributeError(
AttributeError: Signature of the derived method is not the same as parent class:
- method_2(self, name: str, age: int) -> Dict[str, str]
?                                        ^ ^     -----

+ method_2(self, name: str, age: int) -> List[str]
?                                        ^ ^

Derived method expected to return in 'typing.Dict[str, str]' type, but returns 'typing.List[str]'
```

### Issue

If you're faced with a problem, please file an [issue](https://github.com/mortymacs/abstractmethod/issues/new) on Github.


### Contribute

You're always welcome to contribute to the project! Please file an issue and send your great PR.