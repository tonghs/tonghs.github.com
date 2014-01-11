---
author: ths
comments: true
date: 2013-06-10 05:08:59+00:00
layout: post
slug: django%e4%bd%bf%e7%94%a8%e4%b8%ad%e6%96%87%e6%8a%a5%e9%94%99non-ascii-character-xxx-in-file-xxx-but-no-encoding-declared
title: Django使用中文报错:Non-ASCII character "xxx" in file xxx, but no encoding declared;
wordpress_id: 1153
categories:
- 技术
tags:
- Django
- Non-ASCII character
---

在使用[python](http://www.heycode.com/dict/python)+django的时候出现了这个错误，主要是因为用了中文
解决方法是在文件的第一行加上





 # -_- coding: utf-8 -_-





这样就可以了



