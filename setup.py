# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 21:26:48 2023

@author: DSN RAJU
"""

from setuptools import find_packages, setup
from typing import List
HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="Reliance Industries Stock Forecast",
    version=1.0,
    author="DSN RAJU",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)