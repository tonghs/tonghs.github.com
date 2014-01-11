---
author: ths
comments: false
date: 2012-12-02 03:33:31+00:00
layout: post
slug: '%e6%95%b0%e6%8d%ae%e8%a1%a8%e6%8c%89%e5%a4%a7%e5%b0%8f%e6%8e%92%e5%ba%8f%ef%bc%88sqlserver%ef%bc%89'
title: 数据表按大小排序（sqlserver）
wordpress_id: 975
categories:
- 技术
tags:
- sql
- 排序
---

select OBJECT_NAME(ID)
          ,SIZE = sum(reserved) * CONVERT(FLOAT, (SELECT LOW FROM MASTER.DBO.SPT_VALUES WHERE NUMBER = 1 AND TYPE = 'E')) /1024.00/1024.00
          --表大小（字节）= 8192 x Num_Pages (M)
      from sysindexes
      where indid in (0,1,255)
      GROUP BY ID
      ORDER BY SIZE DESC



