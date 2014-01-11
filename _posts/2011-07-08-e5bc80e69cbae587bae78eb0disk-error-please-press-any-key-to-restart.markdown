---
author: ths
comments: true
date: 2011-07-08 08:38:00+00:00
layout: post
slug: '%e5%bc%80%e6%9c%ba%e5%87%ba%e7%8e%b0disk-error-please-press-any-key-to-restart'
title: 开机出现Disk error please Press any key to restart
wordpress_id: 651
categories:
- 折腾
tags:
- Disk error
- USB
- U盘
---

今天要给公司的笔记本安装部署开发的产品，从开发机到安装机使用U盘拷的，安装完毕后要求重启，我重启，然后屏幕出现两行E文：  
disk error  
please press any key to restart





我当时第一个想法就是系统文件坏了，后来细想提示是disk error应该是硬盘的问题，不会是硬盘被我搞坏了吧，淡定，沉着，要随时保持清醒的头脑，紧张影响人的思考……好像心里活动比较长。





我再想，对了我U盘没拔下来啊，是不是U盘的问题啊，一般电脑不能正常启动都是USB设备在作怪，我迅速拔掉U盘，and press any key to restart，过来，正常启动了。





上网一查原因，应该是笔记本设置了默认USB启动，而我的U盘没有做成启动盘，所以就报错了。



