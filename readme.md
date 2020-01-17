## 1. Jsonfy: Lightweight two-way binding of JSON and object without third-party dependency
## 2. How to use? you can see examples or Quick start
## 3. Welcome to submit your code and comments to a better Jsonfy
## 4. Quick start
```
class Foo(BaseJsonModel):
    infos1 = DictDesc("infos1")
    up = DateTimeDesc("up", format='%Y-%m-%d')
    down = DateTimeDesc("down")
f = Foo()
f.up = datetime.now()
f.down = datetime.now()
_dict = {
    "key": "value"
}
_set = {1, 2, 3}
_list = ['sss', 'ffff', 'ffff']
f.infos1 = _dict
print(f.toJson())
f_obj = f.fromJson(f.toJson())
print(f_obj)
```