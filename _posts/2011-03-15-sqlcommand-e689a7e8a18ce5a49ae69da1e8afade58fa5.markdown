---
author: ths
comments: true
date: 2011-03-15 02:32:00+00:00
layout: post
slug: sqlcommand-%e6%89%a7%e8%a1%8c%e5%a4%9a%e6%9d%a1%e8%af%ad%e5%8f%a5
title: SqlCommand 执行多条语句
wordpress_id: 553
categories:
- 技术
tags:
- SqlCommand
- 多条语句
---

SqlCommand可以执行多条语句,只要把多条SQL语句用分号隔开就OK了,比如要同时查找多个表:只要语句是"select * from name1;select * from name2"就行了.就是一个批处理机制.  
但是对于插入语句,虽然写在一起执行,但是系统不会默认的构造事务处理,如,一个有错,一个没有错,插入后就是错的,没有事务处理的回滚机制,所以尽量少用这个东西.  
同样可以用SqlDataAdapter把读出的结果填充在DataSet中.



