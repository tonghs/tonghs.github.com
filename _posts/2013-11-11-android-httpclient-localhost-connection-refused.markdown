---
author: ths
comments: true
date: 2013-11-11 12:48:57+00:00
layout: post
slug: android-httpclient-localhost-connection-refused
title: Android  httpclient localhost Connection refused
wordpress_id: 1273
categories:
- 技术
---

在开发RSS Android端时，用本机PC做server，调试中通过android simulator模拟器链接localhost或者127.0.0.1，报错如下：




    
    <code>Exception 1:java.net.ConnectException: localhost/127.0.0.1:8080 - 
    Connection refused
    </code>





百思不得其解，后来转念一想，localhost和127.0.0.1代表的是Android模拟器的本机，不是我的PC，于是改成改成电脑内网ip，成功获取数据。





记录下来特此提醒各位不要跟我一样犯二。



