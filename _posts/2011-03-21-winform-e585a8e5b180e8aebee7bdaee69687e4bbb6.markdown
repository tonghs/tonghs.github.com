---
author: ths
comments: true
date: 2011-03-21 09:06:00+00:00
layout: post
slug: winform-%e5%85%a8%e5%b1%80%e8%ae%be%e7%bd%ae%e6%96%87%e4%bb%b6
title: winform 全局设置文件
wordpress_id: 577
categories:
- 技术
tags:
- winform
- 设置
---

<





p>开vs的“解决方案资源管理器”，在项目文件夹下打开“Properties”文件夹，双击“Settings.settings”，然后可以打开项目配置信息，在里面添加你要的配置项，设置好配置项的名称、类型和值，然后在程序里面就可以用了。





<





p>使用方法：  
1、添加命名空间: using 项目名称.Properties;  
2、使用变量 xxx = Settings.Default.配置项名称;  
3、修改并保存变量:  
Settings.Default.配置项名称 = 值;  
Settings.Default.Save();





C#生成exe的时候，同时会自动生成一个配置文件，例如exe的名称是 aaa.exe，则配置文件的名称为 aaa.exe.config，拷贝exe的时候应将配置文件一起拷贝过去，否则配置信息将会丢失。





除了这种方法，还有另一种方法，就是用静态变量，写一个类，让后添加一个静态成员变量，就可以了。



