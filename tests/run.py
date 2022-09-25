#!/usr/bin/env python
import os
import pathlib
import subprocess

BASE = pathlib.Path(__file__)
os.environ["PYTHONPATH"] = BASE.parent.parent.as_posix()


def run_test(test_file: str, expected_output: str, expected_exit_code: int):
    """Run test by executing Python file."""
    expected_output = expected_output.replace("\n", "")
    process = subprocess.run(
        ["python", "tests/{}".format(test_file)],
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    output = process.stderr.decode().replace("\r\n", "").replace("\n", "")
    assert process.returncode == expected_exit_code
    assert expected_output in output


# Correct usage.
run_test("correct_class_test.py", "", 0)

# Incorrect usages.
TEST_1 = """AttributeError: 1: incorrect implementation.
Derived class 'ABCDerived' has not implemented 'method_1' method of the parent class 'ABCParent'

2: incorrect implementation.
Derived class 'ABCDerived' has not implemented 'method_2' method of the parent class 'ABCParent'
"""
run_test("incorrect_class_1_test.py", TEST_1, 1)

TEST_2 = """AttributeError: 1: incorrect signature.
Signature of the derived method is not the same as parent class:
- method_1(self, name, age)
?                    -----

+ method_1(self, name)
Derived method expected to get 3 parameters but gets 2
"""
run_test("incorrect_class_2_test.py", TEST_2, 1)

TEST_3 = """AttributeError: 1: incorrect signature.
Signature of the derived method is not the same as parent class:
- method_2(self, name: str, age: int) -> Dict[str, str]
?                      ^ -

+ method_2(self, name: int, age: int) -> Dict[str, str]
?                      ^^

Derived method expected to get 'name:<class 'str'>' paramter's type, but gets 'name:<class 'int'>'
"""
run_test("incorrect_class_3_test.py", TEST_3, 1)

TEST_4 = """AttributeError: 1: incorrect signature.
Signature of the derived method is not the same as parent class:
- method_4(self, name: str, age: int) -> Tuple[str, str]
?                ^  ^

+ method_4(self, family: str, age: int) -> Tuple[str, str]
?                ^  ^^^

Derived method expected to get 'name' paramter, but gets 'family'
"""
run_test("incorrect_class_4_test.py", TEST_4, 1)

TEST_5 = """AttributeError: 1: incorrect signature.
Signature of the derived method is not the same as parent class:
- method_2(self, name: str, age: int) -> Dict[str, str]
?                                                  ^ -

+ method_2(self, name: str, age: int) -> Dict[str, int]
?                                                  ^^

Derived method expected to return in 'typing.Dict[str, str]' type, but returns 'typing.Dict[str, int]'
"""
run_test("incorrect_class_5_test.py", TEST_5, 1)

TEST_6 = """AttributeError: 1: incorrect implementation.
Derived class 'ABCDerived' has not implemented 'method_1' method of the parent class 'ABCParent'

2: incorrect signature.
Signature of the derived method is not the same as parent class:
- method_2(self, name: str, age: int) -> Dict[str, str]
?                      ^ -

+ method_2(self, name: int, age: int) -> Dict[str, str]
?                      ^^

Derived method expected to get 'name:<class 'str'>' paramter's type, but gets 'name:<class 'int'>'

3: incorrect signature.
Signature of the derived method is not the same as parent class:
- method_4(self, name: str, age: int) -> Tuple[str, str]
?                ^  ^

+ method_4(self, family: str, age: int) -> Tuple[str, str]
?                ^  ^^^

Derived method expected to get 'name' paramter, but gets 'family'

4: incorrect signature.
Signature of the derived method is not the same as parent class:
- method_5(self, name: str, age: int) -> Tuple[str, str]
?                                        ------   ------

+ method_5(self, name: str, age: int) -> str
Derived method expected to return in 'typing.Tuple[str, str]' type, but returns '<class 'str'>'
"""
run_test("incorrect_class_6_test.py", TEST_6, 1)
