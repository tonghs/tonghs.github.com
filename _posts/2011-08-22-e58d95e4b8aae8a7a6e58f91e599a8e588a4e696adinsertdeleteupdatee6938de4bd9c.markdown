---
author: ths
comments: true
date: 2011-08-22 06:00:00+00:00
layout: post
slug: '%e5%8d%95%e4%b8%aa%e8%a7%a6%e5%8f%91%e5%99%a8%e5%88%a4%e6%96%adinsertdeleteupdate%e6%93%8d%e4%bd%9c'
title: 单个触发器判断Insert/Delete/Update操作
wordpress_id: 661
categories:
- 技术
tags:
- 操作
- 触发器
---

做BI的都知道，数据库会涉及到增量抽取，我采用的办法是用触发器跟踪数据表的增、删、该，但是这样的话每个表得些三个触发器，工作量增加了三倍，于是我就想能不能用一个，然后在触发器中判断操作，上网查了下，发现了这么一句话：





<





p>插入操作（Insert）：Inserted表有数据，Deleted表无数据  
删除操作（Delete）：Inserted表无数据，Deleted表有数据  
更新操作（Update）：Inserted表有数据（新数据），Deleted表有数据（旧数据）





<





p>这就好办了，于是有了如下代码：





create trigger tr_DEALER  
on DEALER  
for update,insert,delete  
as





if exists(select 1 from inserted) and exists(select 1 from deleted)  
insert INCREMENT (INCREMENT_ID,TABLE_NAME,[ACTION] )  
select DL_ID,'DEALER','update'  
from inserted  
else  
if exists(select 1 from inserted) and not exists(select 1 from deleted)  
insert INCREMENT (INCREMENT_ID,TABLE_NAME,[ACTION] )  
select DL_ID,'DEALER','insert'  
from inserted  
else  
if not exists(select 1 from inserted) and exists(select 1 from deleted)  
insert INCREMENT (INCREMENT_ID,TABLE_NAME,[ACTION] )  
select DL_ID,'DEALER','delete'  
from deleted





go



