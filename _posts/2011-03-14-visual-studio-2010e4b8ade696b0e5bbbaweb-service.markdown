---
author: ths
comments: true
date: 2011-03-14 08:29:00+00:00
layout: post
slug: visual-studio-2010%e4%b8%ad%e6%96%b0%e5%bb%baweb-service
title: visual studio 2010中新建web service
wordpress_id: 552
categories:
- 技术
- 折腾
tags:
- vs
- web service
---

<





p>在 Visual Studio 2010 的新建 Web 应用程序或者 Web 网站窗口中，如果你选择 .NET 4.0，会发现缺少了 ASP.NET Web Services 模板。你可能会怀疑 VS 2010 是不是不支持 ASP.NET Web Services 了？答案是否定的！你可以通过下面两种方式建立 ASP.NET Web Services 项目或网站：





<





p>1.如果直接选择 .NET 4.0，可以选择 ASP.NET Empty Web Site/Application 模板，建立空的 Web 网站或项目，在添加新项窗口中，你依然会发现 Web Service 这个项模板。





<





p>2.可以先选择 .NET 2.0/3.0/3.5，就可以选择 ASP.NET Web Services 模板建立了，之后如果需要 .NET 4.0 的新特性，可以在项目属性窗口或网站属性页窗口的 Build 选项卡中选择 .NET 4.0。





从 Visual Studio 2010 对 .NET 4.0 故意隐藏 ASP.NET Web Services 模板来看，**显然已不建议使用 ASP.NET Web Services 建立新的服务，WCF 服务应该是新项目的首选。**



