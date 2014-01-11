---
author: ths
comments: true
date: 2011-07-08 08:45:00+00:00
layout: post
slug: '%e5%9c%a8%e5%b8%b8%e8%a7%84%e7%b1%bb%e4%b8%ad%e4%bd%bf%e7%94%a8response'
title: 在常规类中使用response
wordpress_id: 653
categories:
- 技术
tags:
- MessageBox
- Response
- web
- 封装
---

众所周知，web程序中没有MessageBox类，但有时要用怎么办呢，自己写呗，封装成单独的类就行了，但是web程序是通过Response.Write()方法，而常规类中不能使用Response对象，咋办，可用如下办法：System.Web.HttpContext.Current.Response.Write()，轻松解决。



