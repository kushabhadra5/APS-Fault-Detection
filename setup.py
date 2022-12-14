#This file is important whenever we build a python project.
#This file consists the code we have created in package format.
from setuptools import find_packages,setup

from typing import List

REQUIREMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements()->List[str]:
    """This will consist a list of all the libraries and dependencies 
    we are going to require while building the project"""
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
    requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
    
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list



setup(
    name="sensor",
    version="0.0.2",
    author="Kushal",
    author_email="akushabhadra5@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(),
)