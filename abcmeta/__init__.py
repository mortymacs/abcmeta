"""ABCMeta library implementation.

This library provides a restricted way to validate abstract methods.
The Python's default abstract method library only validates the methods
that exist in the derived classes and nothing else.
What this library provides is apart from that validation it provides
validations over the method's signature.
All you need is to import 'ABCMeta' and 'abstractmethod' from this library.
"""
import inspect
from abc import ABCMeta as BuiltinABCMeta
from abc import abstractmethod as builtin_abstractmethod
from difflib import ndiff
from itertools import count
from typing import Any, Callable, List, Optional, Text, Tuple, Type

__all__ = ["ABC", "abstractmethod"]


def _get_signature(method: Callable) -> Tuple[Type, List[Tuple[Text, Type]], Text]:
    """Get a method signature.

    Args:
        method (Callable): a callable method.

    Returns:
        Tuple[Type, List[Tuple[Text, Type]], Text]: the method signature.
    """
    method_signature = inspect.signature(method)
    method_parameters = []
    for param_name, param in method_signature.parameters.items():
        if param.annotation == inspect.Signature.empty:
            method_parameters.append((param_name, Any))
        else:
            method_parameters.append((param_name, param.annotation))

    method_signature_str = "{}{}".format(method.__name__, str(method_signature))
    if method_signature.return_annotation == inspect.Signature.empty:
        return Any, method_parameters, method_signature_str
    return method_signature.return_annotation, method_parameters, method_signature_str


def _compare_signatures_details(
    source_method: Tuple[Type, List[Tuple[Text, Type]]],
    derived_method: Tuple[Type, List[Tuple[Text, Type]]],
) -> Text:
    """Compare source and derived methods and returns a diff.

    Args:
        source_method (Tuple[Type, List[Tuple[Text, Type]]]): source method signature.
        derived_method (Tuple[Type, List[Tuple[Text, Type]]]): derived method signature.

    Returns:
        Text: comparision result in the 'diff' format.
    """
    # Check return type.
    if source_method[0] != derived_method[0]:
        return (
            "Derived method expected to return in '{}' type, but returns '{}'".format(
                source_method[0], derived_method[0]
            )
        )

    # Check method parameters by length.
    if len(source_method[1]) != len(derived_method[1]):
        return "Derived method expected to get {} parameters but gets {}".format(
            len(source_method[1]), len(derived_method[1])
        )

    # Check method parameters by name and type.
    for index, (param_name, param_type) in enumerate(source_method[1]):
        derived_param_name, derived_param_type = derived_method[1][index]
        if param_name != derived_param_name:
            return "Derived method expected to get '{}' paramter, but gets '{}'".format(
                param_name, derived_param_name
            )
        if param_type != derived_param_type:
            return (
                "Derived method expected to get '{}:{}' paramter's type,"
                " but gets '{}:{}'".format(
                    param_name, param_type, derived_param_name, derived_param_type
                )
            )

    return "Check comparision result"


def _compare_signatures(source_method: Text, derived_method: Text) -> Optional[Text]:
    """Compare source and derived methods and returns a diff.

    Args:
        source_method (Text): source method signature.
        derived_method (Text): derived method signature.

    Returns:
        Optional[Text]: comparision result in the 'diff' format.
    """
    if source_method == derived_method:
        return None

    diff = ndiff(
        source_method.splitlines(keepends=True),
        derived_method.splitlines(keepends=True),
    )
    return "\r\n".join(diff)


def _prepare_text_to_raise(diff: Text, diff_details: Text) -> Text:
    """It should prepare text for raising the error.

    Args:
        diff (Text): comparision result.
        diff_details (Text): comparision result details.

    Returns:
        Text: prepared text for raising the error.
    """
    return "{}\r\n{}".format(diff, diff_details)


def abstractmethod(funcobj: Callable) -> Callable:
    """Abstract method restricted implementation.

    Note:
        Logic is exactly the same as the `abc.abstractmethod` function
        except it adds an extra attribute.

    .. _abc.py/abstractmethod:
       https://github.com/python/cpython/blob/main/Lib/abc.py#L7
    """
    builtin_abstractmethod(funcobj)
    funcobj.__isabstractmethod_restricted__ = True
    return funcobj


# pylint: disable=too-few-public-methods
class ABC(metaclass=BuiltinABCMeta):
    """Abstract base class"""

    def __init_subclass__(cls):
        """Python built-in method."""
        super().__init_subclass__()

        errors = []
        error_count = count(1)
        for name, obj in vars(cls.__base__).items():

            # Ignore uncallable methods.
            if not callable(obj):
                continue

            # Ignore if it's not an abstract method.
            if not hasattr(obj, "__isabstractmethod__") or not hasattr(
                obj, "__isabstractmethod_restricted__"
            ):
                continue
            if not obj.__isabstractmethod__ or not obj.__isabstractmethod_restricted__:
                continue

            # Make sure the derived class has implemented the abstract method.
            if name not in cls.__dict__:
                errors.append(
                    "{}: incorrect implementation.\r\n"
                    "Derived class '{}' has not implemented '{}' method of the"
                    " parent class '{}'".format(
                        next(error_count), cls.__name__, name, cls.__base__.__name__
                    )
                )
                continue

            derived_method = getattr(cls, name)

            # Get methods signatures.
            *obj_method_signature, obj_method_signature_str = _get_signature(obj)
            *derived_method_signature, derived_method_signature_str = _get_signature(
                derived_method
            )

            # Compare signatures.
            diff = _compare_signatures(
                obj_method_signature_str, derived_method_signature_str
            )

            # Raise signature error.
            if diff:
                diff_details = _compare_signatures_details(
                    obj_method_signature, derived_method_signature
                )
                errors.append(
                    "{}: incorrect signature.\r\n"
                    "Signature of the derived method is not the same as parent"
                    " class:\r\n{}".format(
                        next(error_count), _prepare_text_to_raise(diff, diff_details)
                    )
                )

        if errors:
            raise AttributeError("\n{}".format("\n\n".join(errors)))
