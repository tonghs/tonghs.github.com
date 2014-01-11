---
author: ths
comments: true
date: 2013-06-10 05:10:36+00:00
layout: post
slug: django%e9%85%8d%e7%bd%ae%e5%b1%80%e5%9f%9f%e7%bd%91%e8%ae%bf%e9%97%ae
title: Django配置局域网访问
wordpress_id: 1155
categories:
- 技术
tags:
- Django
- 局域网访问
---

默认方法启动django
manage.py runserver
这时启动的服务只能在本机访问，这是因为服务只向本机（127.0.0.1：8000）提供，所以局域网的其他机器不能访问。
如果想让网络上的其他计算机能够访问djang的服务，需要更改启动django的命令
manage.py runserver 本机的IP:端口
即可





访问的时候需要指明是http访问，格式如下：





http://<ip>:<port>









我用此法，在局域网内测试通过



