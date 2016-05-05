---
published: false
layout: post
tags: []
---

``` python
class LRUCache:

    # @param length, an integer
    def __init__(self, length):
        self.cache = {}
        self.used_list = []
        self.length = length

    # @return an integer
    def get(self, key):
        if key in self.cache:
            if key != self.used_list[-1]:
                self.used_list.remove(key)
                self.used_list.append(key)
            return self.cache[key]
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.cache:
            self.used_list.remove(key)
        elif len(self.cache) == self.length:
            self.cache.pop(self.used_list.pop(0))
        self.used_list.append(key)
        self.cache[key] = value
```

从 python3.2 开始内置了 functools.lru_cache，使用 functools 模块的 lur_cache 装饰器，可以缓存最多 maxsize 个此函数的调用结果，从而提高程序执行的效率，特别适合于耗时的函数。