---
author: ths
comments: true
date: 2010-11-30 05:28:47+00:00
layout: post
slug: '%e5%9c%a8winform%e4%b8%ad%e8%a7%a3%e6%9e%90html%e6%a0%87%e7%ad%be'
title: 在winform中解析html标签
wordpress_id: 144
categories:
- 技术
---





最近在弄公司的系统时遇到一个问题，有一个winform要调用网站的数据库，数据库中存的是经过eWebEditor处理过的文章，都带有html标签，当时想用正则表达式过滤掉，但是还是放弃了原因有三：1.我对正则表达式了解很少；2.虽说我可以现学正则表达式，但是实现起来也是很麻烦的；3.如果过滤掉的话文章的格式就没有了。于是上网找这方面的控件，不是很理想。最后在百度知道上100分悬赏找到了解决方法，很简单的，不需要第三方控件，直接用WebBrower就能实现，用到了WebBrower.DocumentText属性，比如要显示的html代码如下：adc</br>def,则可用下面方法解析显示：





string str = "abc</br>def"; //实际是数据库中的文章





WebBrower.DocumentText = str; //显示



