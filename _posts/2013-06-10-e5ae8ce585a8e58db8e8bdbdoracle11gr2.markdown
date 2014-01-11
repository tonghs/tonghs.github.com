---
author: ths
comments: true
date: 2013-06-10 04:36:56+00:00
layout: post
slug: '%e5%ae%8c%e5%85%a8%e5%8d%b8%e8%bd%bdoracle11gr2'
title: 完全卸载oracle11gR2
wordpress_id: 1136
categories:
- 技术
tags:
- oracle
---

实现方法：





　　1、开始－＞设置－＞控制面板－＞管理工具－＞服务停止所有Oracle服务；





　　2、在安装目录中找到并运行deinstall.exe；





　　3、运行regedit，选择HKEY_LOCAL_MACHINE\SOFTWARE\ORACLE，按del键删除这个入口；





　　4、运行regedit，选择HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services，滚动这个列表，删除所有Oracle入口；





　　5、运行refedit，选择KEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Eventlog\Application，删除所有Oracle入口；





　　6、重新启动计算机，重起后才能完全删除Oracle所在目录 ；





　　7、如有必要，删除所有Oracle相关的ODBC的DSN；





　　8、到事件查看器中，删除Oracle相关的日志说明：如果有个别DLL文件无法删除的情况，则不用理会，重新启动，开始新的安装，安装时，选择一个新的目录，则，安装完毕并重新启动后，老的目录及文件就可以删除掉了。



