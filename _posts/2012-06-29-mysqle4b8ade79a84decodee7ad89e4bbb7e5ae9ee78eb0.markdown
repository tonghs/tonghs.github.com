---
author: ths
comments: true
date: 2012-06-29 02:53:00+00:00
layout: post
slug: mysql%e4%b8%ad%e7%9a%84decode%e7%ad%89%e4%bb%b7%e5%ae%9e%e7%8e%b0
title: mysql中的decode等价实现
wordpress_id: 820
categories:
- 技术
tags:
- decode
- mysql
---

Select title,case Emergency when 1 then '紧急' else '普通' End as emergency from already_sign  
select a.title,if(a.Emergency=1,'紧急','普通')emergency from already_sign a



