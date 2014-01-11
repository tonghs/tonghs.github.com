---
author: ths
comments: true
date: 2013-11-11 12:34:40+00:00
layout: post
slug: python-%e4%b8%ad%e4%bd%bf%e7%94%a8-mysqldb%e6%8f%92%e5%85%a5%e4%b8%ad%e6%96%87%e9%97%ae%e9%a2%98
title: Python 中使用 MySQLdb插入中文问题
wordpress_id: 1271
categories:
- 技术
tags:
- mysql
- MySQLdb
- python
---

今天使用 MySQLdb 往 MySQL 插入中文数据时遇到一个异常：




    
    <code>UnicodeEncodeError: 'latin-1' codec can't encode characters in position 0-3: ordinal not in range(256)
    </code>





解决办法：





在创建连接的时候设置一下编码，如：




    
    <code>conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db", *charset="utf8"*)
    </code>





注意结尾的斜体：charset="utf8"



