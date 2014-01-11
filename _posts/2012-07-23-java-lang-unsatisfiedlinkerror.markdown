---
author: ths
comments: true
date: 2012-07-23 11:47:00+00:00
layout: post
slug: java-lang-unsatisfiedlinkerror
title: java.lang.UnsatisfiedLinkError
wordpress_id: 831
categories:
- 技术
tags:
- java.lang.UnsatisfiedLinkError
- JNI
---

在使用JNI时发现了如下错误：java.lang.UnsatisfiedLinkError  
01-01 09:24:00.119: ERROR/AndroidRuntime(766): java.lang.UnsatisfiedLinkError: nativeRelease  
原因之一：动态库中没有这个jni函数，去源码一看，果然函数名写错了。



