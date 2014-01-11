---
author: ths
comments: true
date: 2011-06-01 02:57:00+00:00
layout: post
slug: mysql-server-has-gone-away%e9%97%ae%e9%a2%98%e7%9a%84%e8%a7%a3%e5%86%b3%e6%96%b9%e6%b3%95
title: MySQL server has gone away问题的解决方法
wordpress_id: 631
categories:
- 技术
tags:
- mysql
---

最近的项目中图片要以二进制形式存到数据库中，在备份还原数据库时遇到了这个问题：





#### MySQL server has gone away





<





p>大概浏览了一下，主要可能是因为以下几种原因：  
一种可能是发送的SQL语句太长，以致超过了max_allowed_packet的大小，如果是这种原因，你只要修改my.cnf，加大max_allowed_packet的值即可。





<





p>还有一种可能是因为某些原因导致超时，比如说程序中获取数据库连接时采用了Singleton的做法，虽然多次连接数据库，但其实使用的都是同一个连接，而且程序中某两次操作数据库的间隔时间超过了wait_timeout（SHOW STATUS能看到此设置），那么就可能出现问题。最简单的处理方式就是把wait_timeout改大，当然你也可以在程序里时不时顺手mysql_ping()一下，这样MySQL就知道它不是一个人在战斗。





<





p>解决MySQL server has gone away





<





p>1、应用程序（比如PHP）长时间的执行批量的MYSQL语句。最常见的就是采集或者新旧数据转化。  
解决方案：  
在my.cnf文件中添加或者修改以下两个变量：  
wait_timeout=2880000  
interactive_timeout = 2880000   
关于两个变量的具体说明可以google或者看官方手册。如果不能修改my.cnf，则可以在连接数据库的时候设置CLIENT_INTERACTIVE，比如：  
sql = "set interactive_timeout=24*3600";  
mysql_real_query(...)





2、执行一个SQL，但SQL语句过大或者语句中含有BLOB或者longblob字段。比如，图片数据的处理  
解决方案：  
在my.cnf文件中添加或者修改以下变量：  
max_allowed_packet = 10M(也可以设置自己需要的大小)  
max_allowed_packet 参数的作用是，用来控制其通信缓冲区的最大长度。



