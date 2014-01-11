---
author: ths
comments: true
date: 2012-06-21 06:37:00+00:00
layout: post
slug: listitemtype-item-%e5%92%8clistitemtype-alternatingitem
title: ListItemType.Item 和ListItemType.AlternatingItem
wordpress_id: 813
categories:
- 技术
tags:
- AlternatingItem
- Datalist
- ListItemType
---

Datalist在绑定时判断是不是数据行是最开始写的是：




    
    <span class="kwrd">if</span>  (e.Item.ItemType  ==  ListItemType.Item)







发现偶数行有问题,后来debug发现,偶数行的ItemType为AlternatingItem，不是item，于是改写为




    
    <span class="kwrd">if</span> (e.Item.ItemType == ListItemType.Item || e.Item.ItemType == ListItemType.AlternatingItem)







