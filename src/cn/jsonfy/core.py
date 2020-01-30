# -*- coding utf-8 -*-#
# ------------------------------------------------------------------
# Name:      core
# Author:    liangbaikai
# Date:      2020/1/16
# Desc:      there is a jsonfy core
# ------------------------------------------------------------------
import json
from datetime import datetime


class BaseDesc:

    def __init__(self, key, type, **kwargs):
        """

        :param key: serialization key
        :param type:  the type of filed
        :param kwargs: the extra info, if you want to hide a filed, just for hide=true; and is a DateTimeDesc you can use your format
        just for  format='%Y-%m-%d ('Y-%m-%d %H:%M:%S'  is default)
        """
        self.key = key
        self.type = type
        self.extra = kwargs

    def __get__(self, instance, owner):
        return instance.__dict__[self.key]

    def __delete__(self, instance):
        instance.__dict__.pop(self.key)

    def __set__(self, instance, value):
        # just check type  and null value is included
        if not isinstance(value, self.type) and value is not None:
            raise TypeError(
                'occured some error, attribute<%s=%s> require a %s type,'
                'please confirm a suitable type you gived' % (
                    self.key, value, self.type.__name__))


class IntDesc(BaseDesc):

    def __init__(self, key, type=None, **kwargs):
        self.type = int
        super().__init__(key, self.type, **kwargs)

    def __set__(self, instance, value):
        instance.__dict__[self.key] = int(value) if value else None
        super().__set__(instance, value)


class StrDesc(BaseDesc):
    def __init__(self, key, type=None, **kwargs):
        self.type = str
        super().__init__(key, self.type, **kwargs)

    def __set__(self, instance, value):
        instance.__dict__[self.key] = str(value) if value else None
        super().__set__(instance, value)


class BoolDesc(BaseDesc):
    def __init__(self, key, type=None, **kwargs):
        self.type = bool
        super().__init__(key, self.type, **kwargs)

    def __set__(self, instance, value):
        instance.__dict__[self.key] = bool(value) if value else None
        super().__set__(instance, value)


class NoneDesc(BaseDesc):
    def __init__(self, key, type=None, **kwargs):
        self.type = None
        super().__init__(key, self.type, **kwargs)

    def __set__(self, instance, value):
        instance.__dict__[self.key] = None


class FloatDesc(BaseDesc):
    def __init__(self, key, type=None, **kwargs):
        self.type = float
        super().__init__(key, self.type, **kwargs)

    def __set__(self, instance, value):
        instance.__dict__[self.key] = float(value) if value else None
        super().__set__(instance, value)


class SetDesc(BaseDesc):
    def __init__(self, key, type=None, **kwargs):
        self.type = set
        super().__init__(key, self.type, **kwargs)

    def __set__(self, instance, value):
        instance.__dict__[self.key] = set(value) if value else None
        super().__set__(instance, value)


class DateTimeDesc(BaseDesc):
    def __init__(self, key, type=None, **kwargs):
        self.type = datetime
        # the_default_format
        kwargs.setdefault('format', '%Y-%m-%d %H:%M:%S')
        super().__init__(key, self.type, **kwargs)

    def __set__(self, instance, value):
        instance.__dict__[self.key] = value if value else None
        super().__set__(instance, value)


class ListDesc(BaseDesc):
    def __init__(self, key, type=None, value=None, **kwargs):
        self.type = list
        super().__init__(key, self.type, **kwargs)

    def __set__(self, instance, value):
        instance.__dict__[self.key] = list(value) if value else None
        super().__set__(instance, value)


class DictDesc(BaseDesc):
    def __init__(self, key, type=None, **kwargs):
        self.type = dict
        super().__init__(key, self.type, **kwargs)

    def __set__(self, instance, value):
        instance.__dict__[self.key] = dict(value) if value else None
        super().__set__(instance, value)


class ObjectDesc(BaseDesc):
    def __init__(self, key, type, **kwargs):
        self.type = type
        super().__init__(key, self.type, **kwargs)

    def __set__(self, instance, obj_instance):
        instance.__dict__[self.key] = obj_instance
        super().__set__(instance, obj_instance)


class JsonMeta(type):

    def __new__(cls, name, bases, attrs):
        if attrs.get("__abstract__"):
            return type.__new__(cls, name, bases, attrs)
        mappings = {}
        for k, v in attrs.items():
            if isinstance(v, BaseDesc):
                mappings.setdefault(k, v)
        attrs['_mapping'] = mappings
        return type.__new__(cls, name, bases, attrs)


class BaseJsonModel(metaclass=JsonMeta):
    __abstract__ = True

    def __init__(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def toJson(self):
        json_dict = self.toDict()
        return json.dumps(json_dict, ensure_ascii=False)

    def _toDict(self, instance, mapping, target={}):
        for k in list(mapping.keys()):
            # hide the field
            if mapping.get(k) and mapping.get(k).extra and mapping.get(k).extra.get('hide'):
                continue
            if isinstance(mapping.get(k), ObjectDesc):
                child__mapping = mapping.get(k).type._mapping
                instance = instance.__dict__.get(k, None)
                if instance:
                    _target = self._toDict(instance, child__mapping, {})
                    target[k] = _target
            else:
                if instance:
                    __value = instance.__dict__.get(k, None)
                    if isinstance(mapping.get(k), SetDesc) and __value:
                        __value = list(__value)
                    if isinstance(mapping.get(k), DateTimeDesc) and __value:
                        __value = __value.strftime(
                            mapping.get(k).extra.get('format'))
                    target[k] = __value
        return target

    def fromJson(self, json_str):
        _dict = json.loads(json_str)
        return self._fromJson(self, _dict, self._mapping)

    def _fromJson(self, intance, _dict, mapping):
        for k in list(mapping.keys()):
            if mapping.get(k) and mapping.get(k).extra and mapping.get(k).extra.get('hide'):
                continue
            if isinstance(mapping.get(k), ObjectDesc):
                child__mapping = mapping.get(k).type._mapping
                empty_instance = mapping.get(k).type()
                setattr(intance, k, empty_instance)
                self._fromJson(empty_instance, _dict.get(k), child__mapping)
            else:
                _value = _dict.get(k, None)
                if _value:
                    if isinstance(mapping.get(k), DateTimeDesc):
                        _value = datetime.strptime(
                            _value, mapping.get(k).extra.get('format'))
                    else:
                        _value = mapping.get(k).type(_value)
                setattr(intance, k, _value)

        return intance

    def toDict(self):
        temp_mapping = self._mapping
        return self._toDict(self, temp_mapping, {})
