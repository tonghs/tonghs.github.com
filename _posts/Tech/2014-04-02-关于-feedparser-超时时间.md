---
layout: post
title: 关于 feedparser 超时时间
---
在 `OnlyRSS` 项目中用到了 feedparser，在使用中发现在解析一些 badurl 时会 block 掉，于是想设置解析超时时间，但是查文档发现 parser 方法没有超时参数。最后 google 到了 feedparser 项目中的 [issue221](https://code.google.com/p/feedparser/issues/detail?id=221) 说的就是这个问题，其中有解决办法：

> developers have had the ability to set a global timeout for over seven years by importing the socket library and setting the timeout in this way:

    import socket
    socket.setdefaulttimeout(<timeout in floating seconds>)