---
author: ths
comments: false
date: 2012-12-02 03:37:35+00:00
layout: post
slug: http-%e9%94%99%e8%af%af-500-19-internal-server-error-%e6%97%a0%e6%b3%95%e8%ae%bf%e9%97%ae%e8%af%b7%e6%b1%82%e7%9a%84%e9%a1%b5%e9%9d%a2%ef%bc%8c%e5%9b%a0%e4%b8%ba%e8%af%a5%e9%a1%b5%e7%9a%84%e7%9b%b8
title: HTTP 错误 500.19 - Internal Server Error 无法访问请求的页面，因为该页的相关配置数据无效
wordpress_id: 978
categories:
- 技术
tags:
- '500.19'
- http错误
---

HTTP 错误 500.19 - Internal Server Error无法访问请求的页面，因为该页的相关配置数据无效。




    
    定义了重复的“system.web.extensions/scripting/scriptResourceHandler”节
    <sectionGroup name="scripting" type="System.Web.Configuration.ScriptingSectionGroup, System.Web.Extensions, Version=3.5.0.0, Culture=neutral, PublicKeyToken=31BF3856AD364E35">
     <section name="scriptResourceHandler" type="System.Web.Configuration.ScriptingScriptResourceHandlerSection, System.Web.Extensions, Version=3.5.0.0, Culture=neutral, PublicKeyToken=31BF3856AD364E35" requirePermission="false" allowDefinition="MachineToApplication"/>
    <sectionGroup name="webServices" type="System.Web.Configuration.ScriptingWebServicesSectionGroup, System.Web.Extensions, Version=3.5.0.0, Culture=neutral, PublicKeyToken=31BF3856AD364E35">





解决方法：更改了iis7.5中应用程序池的设置为 2.0 即可.



