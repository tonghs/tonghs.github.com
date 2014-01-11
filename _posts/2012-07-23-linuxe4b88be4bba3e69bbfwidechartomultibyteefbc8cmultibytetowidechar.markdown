---
author: ths
comments: true
date: 2012-07-23 11:39:00+00:00
layout: post
slug: linux%e4%b8%8b%e4%bb%a3%e6%9b%bfwidechartomultibyte%ef%bc%8cmultibytetowidechar
title: linux下代替WideCharToMultiByte，MultiByteToWideChar
wordpress_id: 827
categories:
- 技术
tags:
- mbstowcs()
- MultiByteToWideChar
- wcstombs()
- WideCharToMultiB
---

Linux下面的没有命名为 WideCharToMultiByte() 和 MultiByteToWideChar() 函数，WideCharToMultiByte，MultiByteToWideChar是windows下的函数，在linux下也有类似的两个函数：  
**mbstowcs()  
wcstombs()  
**值得注意的是:  
size_t mbstowcs(wchar_t *wcstr,const char *mbstr,size_t count);  
这个函数的第三个参数count，大小一定要是mbstr长度的2倍，**否则出来的中文也会是乱码**。



