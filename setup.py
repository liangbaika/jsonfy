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
    version="0.3",
    keywords=["pip", "json", "jsonfy", "obj"],
    description="Jsonfy: Lightweight two-way binding of JSON and object without third-party dependency",
    long_description="Jsonfy: Lightweight two-way binding of JSON and object without third-party dependency, suppoert nesting,complex obj"
                     "[Jsonfy: 一款轻量级的无第三方依赖的json和对象的双向绑定的工具，支持复杂类型，嵌套类型，自定义某个字段是否序列化等,欢迎使用]",

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
