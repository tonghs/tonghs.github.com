---
published: true
layout: post
title: python File 对象的 read() readline() readlines() xreadlines()
tag: []
---
## file.read([size])

从文件中最多读取 size 字节的内容，如果 size 为负数或胜率，则读取所有的内容。

## file.readline([size])

从文件中读取整行内容，包括结尾换行符号，如果 size 存在且不为空，则最大读取 size 字节的内容，此时可能返回不完整的行。

## file.readlines([sizehint])

该方法返回的是读取的行的列表，所以可以用 for ... in 方式遍历，当 sizehint 存在且不为空时，返回读取的多行内容，内容大小大约为 sizehint。

## file.xreadlines()

和 readlines 不同的是，该方法返回的是迭代器，和 iter(f) 一样。
