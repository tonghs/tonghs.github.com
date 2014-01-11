---
author: ths
comments: true
date: 2013-06-10 04:58:45+00:00
layout: post
slug: '%e4%b8%ba%e4%bb%80%e4%b9%88%e8%a6%81%e8%bf%9e%e7%bb%ad%e4%b8%a4%e6%ac%a1%e8%b0%83%e7%94%a8-encodeuristring-2'
title: 为什么要连续两次调用 encodeURI(String)
wordpress_id: 1144
categories:
- 技术
tags:
- encodeURI
---

为什么要连续两次调用 encodeURI(String) 方法呢？是因为 Java 中的 request.getParameter(String) 方法会进行一次 URI 的解码过程，调用时内置的解码过程会导致乱码出现。而 URI 编码两次后， request.getParameter(String) 函数得到的是原信息 URI 编码一次的内容。接着用 java.net.URLDecoder.decode(String str,String codename) 方法，将已经编码的 URI 转换成原文。



