# -*- coding utf-8 -*-#
# ------------------------------------------------------------------
# Name:      test
# Author:    liangbaikai
# Date:      2020/1/16
# Desc:      test for jsonfy
# ------------------------------------------------------------------
import time
from datetime import datetime

from cn.jsonfy.core import BaseJsonModel, FloatDesc, IntDesc, ObjectDesc, StrDesc, DictDesc, SetDesc, ListDesc, \
    DateTimeDesc


class Son(BaseJsonModel):
    score = FloatDesc("score")
    age = IntDesc("age")


class Student(BaseJsonModel):
    score = FloatDesc("score")
    age = IntDesc("age")
    s = ObjectDesc("s", Son)


class Person(BaseJsonModel):
    name = StrDesc("name")
    age = IntDesc("age",hide=True)
    st = ObjectDesc("st", Student)


class Foo(BaseJsonModel):
    infos1 = DictDesc("infos1")
    infos2 = SetDesc("infos2")
    infos3 = ListDesc("infos3")
    up = DateTimeDesc("up", format='%Y-%m-%d')
    down = DateTimeDesc("down")


if __name__ == '__main__':
    _start=time.time()
    ffff = Foo()
    ffff.up = datetime.now()
    ffff.down = datetime.now()
    _dict = {
        "a": "aaaa"
    }
    _set = {1, 2, 3}
    _list = ['sss', 'ffff', 'ffff']
    ffff.infos1 = _dict
    ffff.infos2 = _set
    ffff.infos3 = _list
    print(ffff.toJson())
    ggg = ffff.fromJson(ffff.toJson())
    print(ggg)
    for i in range(10000):
        p = Person()
        p.name = "张三" + str(i)
        p.age = 22

        s = Student()
        s.score = 90.22
        s.age = 25
        son = Son(score=222222.00, age=21111112)
        s.s = son
        p.st = s

        xx = p.toJson()
        print(xx)
        p2 = Person()
        obj2 = p2.fromJson(xx)
        print(obj2)
    print(time.time()-_start)