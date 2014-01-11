---
author: ths
comments: true
date: 2012-10-06 01:29:47+00:00
layout: post
slug: '%e7%bc%96%e8%af%91-mod_python%e9%94%99%e8%af%af%ef%bc%82apxserror-command-failed-with-rc65536%ef%bc%82%e9%97%ae%e9%a2%98%e7%9a%84%e8%a7%a3%e5%86%b3'
title: '编译 mod_python错误＂apxs:Error: Command failed with rc=65536＂问题的解决'
wordpress_id: 909
categories:
- 技术
tags:
- mod_python
---

apxs:Error: Command failed with rc=65536





需要修改mod_python的源代码





vim src/connobject.c





把第142行





!(b == APR_BRIGADE_SENTINEL(b) ||





改为





!(b == APR_BRIGADE_SENTINEL(bb) ||



