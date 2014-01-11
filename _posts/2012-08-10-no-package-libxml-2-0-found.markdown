---
author: ths
comments: true
date: 2012-08-10 06:26:00+00:00
layout: post
slug: no-package-libxml-2-0-found
title: No package 'libxml-2.0' found
wordpress_id: 851
categories:
- 折腾
tags:
- libxml-2.0
---

这里显示一个错误信息：  
checking for LIBXML2... configure: error: Package requirements (libxml-2.0 >= 2.6) were not met:  
No package 'libxml-2.0' found  
Consider adjusting the PKG_CONFIG_PATH environment variable if you  
installed software in a non-standard prefix.  
Alternatively, you may set the environment variables LIBXML2_CFLAGS  
and LIBXML2_LIBS to avoid the need to call pkg-config.  
See the pkg-config man page for more details.  
但是我们在上面其实已经安装上 libxml2 了的，这里只是一个 环境变量没有设置好而已。  
解决办法： 确定 /usr/local/libxml2/lib/pkgconfig 目录下有 libxml-2.0.pc  
export PKG_CONFIG_PATH=/usr/local/libxml2/lib/pkgconfig:$PKG_CONFIG_PATH  
再次生成 makefile , 这样就成功了



