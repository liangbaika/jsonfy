# -*- coding utf-8 -*-#
# ------------------------------------------------------------------
# Name:      setup
# Author:    liangbaikai
# Date:      2020/1/17
# Desc:      there is a python file description
# ------------------------------------------------------------------
from setuptools import setup, find_packages

setup(
    name="jsonfy",
    version="0.2.0",
    keywords=["pip", "json", "jsonfy", "obj"],
    description="Jsonfy: Lightweight two-way binding of JSON and object without third-party dependency",
    long_description="Jsonfy: Lightweight two-way binding of JSON and object without third-party dependency, suppoert nesting,complex obj",
    license="MIT Licence",

    url="https://github.com/1144388620lq/jsonfy",
    author="liangbaikai",
    author_email="1144388620@qq.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    platforms="any",
    install_requires=[]

)
