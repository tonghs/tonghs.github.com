---
author: ths
comments: true
date: 2012-10-06 00:45:47+00:00
layout: post
slug: mountain-lion-cgi-%e8%bf%90%e8%a1%8c%e7%8e%af%e5%a2%83
title: Mountain Lion CGI 运行环境
wordpress_id: 901
categories:
- 技术
tags:
- apache
- CGI
- mac
- Python/Django/web.py
---

如果你是一名 Web 开发者，很多时候都需要在本地搭建服务器测试环境，比如 Apache+python cgi这样的环境。事实上 Mac OS X 中想要搭建这样的环境很简单，本文我们就会将详细的教程分享给大家。





首先需要说明的是，Mac OS X 系统其实已经集成了 Apache环境，用户手动开启即可。在之前的 OS X 系统中，只需要进入「系统偏好设置——共享」，然后开启「Web 共享」就可以打开 Apache。不过在最新的 Mountain Lion 中苹果取消了这个共享功能的图形界面，只能从命令行开启。





![](http://img.guomii.com/2012/08/Snip20120806_3-600x353.png)Mountain Lion 中已经没有”Web共享”







### 启用 Apache/Web 共享





打开终端，运行启动 Apache 命令：





> sudo apachectl start





关闭命令：





> sudo apachectl stop





重启命令：





> sudo apachectl restart





查看 Apache 版本命令：





> httpd -v





Mountain Lion 中集成的 Apache 版本如下：





> mbp:~ eyon$ httpd -v
Server version: Apache/2.2.22 (Unix)
Server built: Jun 20 2012 13:57:09





启用 Apache 之后，你可以直接在浏览器中访问 http://localhost，如果出现”It works!”就表示运行正常。





![](http://img.guomii.com/2012/08/Snip20120806_6.png)





### Root 目录





启用 Apache 之后，你首先得知道网页文件应该放到哪个目录才能正常运行，相信有过 Linux 服务器配置经验的对此不会陌生。OS X 中默认有两个目录可以直接运行你的 Web 程序，大家记下即可。





系统级的根目录是：





> /Library/WebServer/Documents/





它对应的网址是：





> http://localhost





下面就要说CGI了，CGI文件对应的目录是：





> **/Library/WebServer/CGI-Executables**





他对应的网址是：





> http://localhost/cgi-bin





将cgi文件放到这个目录即可访问。











