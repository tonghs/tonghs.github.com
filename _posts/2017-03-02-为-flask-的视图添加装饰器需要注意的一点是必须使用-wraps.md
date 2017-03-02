---
published: true
layout: post
title: 为 flask 的视图添加装饰器需要注意的一点是必须使用 wraps
---

wraps 的作用有很多，主要是修改函数的签名，其作用之一是改变函数的 \_\_name\_\_，\_\_doc\_\_。如果你的装饰器不用 wraps，那么被装饰的不同的函数的名字都变成了相同的名字。在 flask 中注册这两个视图时就会发生冲突，提示：

```
AssertionError: View function mapping is overwriting an existing endpoint function
```

一个例子：

``` python
def login_required(func):
 
    @wraps(func)  # 这个装饰器必须有
    def wrap(*args, **kwargs):
        courier_id = request.headers.get('X-ID')
        token = request.headers.get('X-TOKEN')
        if verify_login_token(int(courier_id), token):
            return func(*args, **kwargs)
        else:
            return response(ResponseCode.UNAUTHORIZED)
 
    return wrap
```
