---
published: false
layout: post
title: Python 标准库之：string
---
源代码见：[Lib/string.py](http://hg.python.org/cpython/file/2.7/Lib/string.py)

string 模块包含大量有用的常量和类，常用的字符串支持的方法可参考该模块。

## 字符串常量

常用的有：

string.ascii_lowercase

小写字母'abcdefghijklmnopqrstuvwxyz'。不依赖区域设置。

string.ascii_uppercase

大写的字母'ABCDEFGHIJKLMNOPQRSTUVWXYZ'。不依赖区域设置。

string.ascii_letters

`ascii_lowercase` 和a `scii_uppercase` 常量的连接串。不依赖区域设置。

string.digits

字符串 '1234567890'。

string.hexdigits

字符串 '1234567890abcdefABCDEF'。

string.lowercase

一个字符串，包含所有被认为是小写字母的字符。在大多数系统上，这是字符串'abcdefghijklmnopqrstuvwxyz'。特定的值依赖于区域设置，并调用locale.setlocale()时将更新。

string.uppercase

一个字符串，包含所有被认为是大写字母的字符。在大多数系统上，这是'ABCDEFGHIJKLMNOPQRSTUVWXYZ'的字符串。特定的值依赖于区域设置，并调用locale.setlocale()时将更新。

string.letters

`string.lowercase` 和 `string.uppercase` 的连接串。特定的值依赖于区域设置，并调用locale.setlocale()时将更新。

string.octdigits

字符串 '01234567' 即八进制数。

string.whitespace

包含所有被视为空格的字符串，在大多数系统上，这包括空格、制表符、换行、回车、换页和垂直制表符。

string.punctuation

标点字符的 ASCII 字符的字符串。

string.printable

可打印的字符的字符串。包括 digits, letters, punctuation 和 whitespace。


关于这部分，见源码吧：

``` python

# Some strings for ctype-style character classification
whitespace = ' \t\n\r\v\f'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters = lowercase + uppercase
ascii_lowercase = lowercase
ascii_uppercase = uppercase
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'
hexdigits = digits + 'abcdef' + 'ABCDEF'
octdigits = '01234567'
punctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + letters + punctuation + whitespace

```

## 格式化字符串

``` python
class string.Formatter
```

`format(format_string, **args, ****kwargs)`

该方法的使用方法类似于 string.format()，两种掌握一种即可，个人推荐后者，因为用起来比较简单，不需要实例化一个类。format() 实际是对 vformat() 调用的封装。见源码片段：

``` python
def format(*args, **kwargs):
    if not args:
        raise TypeError("descriptor 'format' of 'Formatter' object "
                        "needs an argument")
    self, args = args[0], args[1:]  # allow the "self" keyword be passed
    try:
        format_string, args = args[0], args[1:] # allow the "format_string" keyword be passed
    except IndexError:
        if 'format_string' in kwargs:
            format_string = kwargs.pop('format_string')
        else:
            raise TypeError("format() missing 1 required positional "
                            "argument: 'format_string'")
    return self.vformat(format_string, args, kwargs)
```

使用举例：

``` python
import string

s = 'hello {name}'

f = string.Formatter()
f.format(s, name='tom')

# 输出
'hello tom'
```

`vformat(format_string, args, kwargs)`

该方法执行真正的格式化工作。注意该方法的后两个参数是 `args` 和 `kwargs` 而不是 `*args` 和 `**kwargs`。根据 format 的源码，得知 vformat 的调用方式为：

``` python
import string

s = 'hello {name}'

f = string.Formatter()
f.vformat(s, (), dict(name='tom'))

# 输出
'hello tom'
```

## 模板字符串

`class string.Template(template)`






