---
author: ths
comments: true
date: 2011-04-21 01:39:00+00:00
layout: post
slug: sqlserver-%e8%af%ad%e5%8f%a5%e6%94%b6%e9%9b%86
title: sqlserver 语句收集
wordpress_id: 619
categories:
- 技术
tags:
- sql
---

最近在做一个代码自动生成的工具，要用到数据库，于是就有了以下代码：





SELECT ISNULL(OBJECTPROPERTY(OBJECT_ID('Admin'), 'IsUserTable'), 0) /*是否存在表*/  
select name from syscolumns where id=object_id('Admin')/*查询字段*/  
select * from SysObjects where xtype='u'/*查询所有表*/  
select * from master.dbo.sysdatabases where dbid>4/*查询所有数据库*/  
SELECT syscolumns.name,systypes.name,syscolumns.length FROM syscolumns,systypes WHERE syscolumns.xusertype = systypes.xusertype and syscolumns.id = object_id('Key') /*查询字段名、类型和长度*/



