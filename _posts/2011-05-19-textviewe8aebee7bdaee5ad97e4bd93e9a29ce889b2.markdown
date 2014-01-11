---
author: ths
comments: true
date: 2011-05-19 03:19:36+00:00
layout: post
slug: textview%e8%ae%be%e7%bd%ae%e5%ad%97%e4%bd%93%e9%a2%9c%e8%89%b2
title: TextView设置字体颜色
wordpress_id: 621
categories:
- 技术
tags:
- TextView
---

最近再学习android，再设置TextView颜色时遇到了问题，读取资源文件中的颜色时，设置无效，代码如下：

tv.setTextColor(R.color.red);

其实这个写法不对，正确的写法为：

tv.setTextColor(getResources().getColor(R.color.red));





