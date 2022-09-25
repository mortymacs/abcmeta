from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="abcmeta",
    version="2.1.0",
    author="Morteza NourelahiAlamdari",
    author_email="m@0t1.me",
    description="Python meta class and abstract method library with restrictions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="AGPLv3",
    url="https://github.com/mortymacs/abcmeta",
    project_urls={"Bug Tracker": "https://github.com/mortymacs/abcmeta/issues"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.6",
)
