---
layout: post
title: Python 标准库之：functools
tagline: null
category: null
tags: []
published: true

---
functools 模块包括：

* functools.cmp_to_key
* functools.reduce
* functools.total_ordering
* functools.partial
* functool.update_wrapper
* functool.wraps

functools.cmp_to_key
----

将老式的 比较函数（comparison function） 转化为 关键字函数（key function），是为了兼容 Python3。

functools.reduce
----
官方解释：

_This is the same function as reduce(). It is made available in this module to allow writing code more forward-compatible with Python 3._

和内置函数 reduce 功能一样，为了兼容 Python3。

functools.total_ordering
----

是一个类装饰器，为了方便定义类的比较排序方法，如果某个类定义了 `__lt__()`, `__le__()`, `__gt__()` 或 `__ge__()` 中的至少一个并且定义了 `__eq__()` 方法，那么用 functools.total_ordering 装饰该类，装饰器会补充其余的比较方法，这就减少了自己定义代码的工作量。

``` Python

@total_ordering
class Person:
    def __eq__(self, other):
        return self.name.lower() == other.name.lower()
    def __lt__(self, other):
        return self.name.lower() < other.name.lower()

```

functools.partial
----

函数参数分位置参数和关键字参数两种，而 partial 的作用就是冻结函数的部分参数（可以使位置参数和关键字函数），从而达到“重新定义”函数的签名，这样可以在某些情况下简化函数调用，举例说明：

``` Python

# 定义函数 add，实现三个数相加
def add(x, y, z=1):
    """this is a test method"""
    return x + y + z

```

想象如下场景：我们需要多次调用 add 函数，调用时 z 的值都是 3，那么可以这么写：

``` Python

add(1, 2, z=3)
add(2, 3, z=3)
add(5, 7, z=3)
...
add(7, 9, z=3)
...

```

因为调用时，关键字参数 z 永远等于 3，那么，可以简化不写吗？答案是可以的，下面就用到了 functools.partial 了：

``` Python

from functools import partial

add_ = partial(add, z=3)

# 那么，调用就可以写为：
add_(1, 2)
add_(2, 3)
add_(5, 7)
...
add_(7, 9)
...

```
需要注意的是：
此时，仍可以给 add_ 传递第三个参数 z，但必须这么写

``` Python

add_(1, 2, z=5)
```
如果不指定关键字，则会抛出如下异常：

``` Python

TypeError: add() got multiple values for keyword argument 'z'

```

同样用法可以用在位置参数上，但是需要注意的是，partial 提供的参数在原函数的位置关键字前，看 partial 的实现就可以理解：

``` Python

# Purely functional, no descriptor behaviour
def partial(func, *args, **keywords):
    """New function with partial application of the given arguments
    and keywords.
    """
    if hasattr(func, 'func'):
        args = func.args + args
        tmpkw = func.keywords.copy()
        tmpkw.update(keywords)
        keywords = tmpkw
        del tmpkw
        func = func.func

    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*(args + fargs), **newkeywords)
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc

```

functools.update_wrapper
----

在上面的例子里，函数 add 是有注释的（一般写明函数的调用方法等等），那么我们自己的 add_ 呢？看下面：

``` Python

print add.__doc__
print add_.__doc__

# 输出：
this is a test method 
partial(func, *args, **keywords) - new function with partial application
    of the given arguments and keywords.

```

所以，这时出现了一个问题，假如有人想用我们的 add_ 函数，但是想看一下 doc ，发现是没有的，那么 update_wrapper 就提供了解决办法：

``` Python

update_wrapper(add_, add)
print add_.__doc__

# 输出：


 this is a test method 

```

可以看到，原本属于 add 的 doc ，add_ 也有了，这样在 debug 的时候就很方便了。这就是 `update_wrapper` 的功能，它可以把被封装函数的 `__name__`、`__module__`、`__doc__` 和  `__dict__` 都复制到封装函数去（模块级别常量WRAPPER_ASSIGNMENTS, WRAPPER_UPDATES）。

源码如下：

``` Python

WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__doc__')
WRAPPER_UPDATES = ('__dict__',)
def update_wrapper(wrapper,
                   wrapped,
                   assigned = WRAPPER_ASSIGNMENTS,
                   updated = WRAPPER_UPDATES):
    for attr in assigned:
        setattr(wrapper, attr, getattr(wrapped, attr))
    for attr in updated:
        getattr(wrapper, attr).update(getattr(wrapped, attr, {}))
    return wrapper
    
```

这个功能在定义装饰器的时候应该是非常有用的。

functools.wraps
----

functools.wraps 就是用 partial 对 update_wrapper 做了包装，看实现：

```python

def wraps(wrapped,
          assigned = WRAPPER_ASSIGNMENTS,
          updated = WRAPPER_UPDATES):

    return partial(update_wrapper, wrapped=wrapped,
                   assigned=assigned, updated=updated)

```

使用场景：

``` python

from functools import wraps
def my_decorator(f):
     @wraps(f)
     def wrapper(*args, **kwds):
         print 'Calling decorated function'
         return f(*args, **kwds)
     return wrapper

@my_decorator
def example():
    """这里是文档注释"""
    print 'Called example function'

example()

# 下面是输出
"""
Calling decorated function
Called example function
"""
print example.__name__ # 'example'
print example.__doc__ # '这里是文档注释'

```
