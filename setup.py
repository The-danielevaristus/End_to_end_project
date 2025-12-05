from setuptools import setup, find_packages
from typing import List


def get_requirements(path: str = "requirements.txt") -> List[str]:
    """Reads the requirements file and returns a list of dependencies.

    Accepts an optional `path` so external callers (like pip/setuptools)
    that pass a config/settings argument won't raise a TypeError.
    """
    requirement_lst: List[str] = []
    try:
        with open(path, "r") as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != "-e .":
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print(f"requirements file '{path}' not found.")
    return requirement_lst


setup(
name="NetworkSecurityProject",
version="0.0.1",
author="Evaristus Daniel",
author_email="danielevaristus72@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),
)