## 1. Jsonfy: Lightweight two-way binding of JSON and object without third-party dependency
## 2. pip install jsonfy 
## 3. How to use? you can see examples or Quick start 
## 4. Welcome to submit your code and comments to a better Jsonfy 
## 5. Quick start：
```
import time
from datetime import datetime

class Foo(BaseJsonModel):
    infos1 = DictDesc("infos1")
    up = DateTimeDesc("up", format='%Y-%m-%d')
    down = DateTimeDesc("down")
    
    
if __name__ == '__main__':
    f = Foo()
    _fake_time = datetime.now()
    f.up = _fake_time
    f.down = _fake_time
    _dict = {"key": "value"}
    f.infos1 = _dict
    
    print(f.toJson())
    f_obj = f.fromJson(f.toJson())
    print(f_obj)
```