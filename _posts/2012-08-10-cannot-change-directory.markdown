---
author: ths
comments: true
date: 2012-08-10 06:29:00+00:00
layout: post
slug: cannot-change-directory
title: cannot change directory
wordpress_id: 853
categories:
- 折腾
tags:
- cannot change directory
- SELINUX
- setenforce 0
- vsftp
---

在RHEL5中，SELINUX可以用来加强系统的安全性，但如果设置不当，则会给你带来很多麻烦。 





所以一般情况下，很多RHCE习惯在X下去打开终端来操作，这样操作的好处是一旦SELINUX阻止掉某一操作，桌面的右上角会弹出一个黄色的五角星。单击这个五角星，会显示SELINUX阻止了哪些操作，并且提供解决的方法。你只需要将解决的代码复制到终端中去运行一下就OK。但千万注意，有时候它所提供的解决代码的路径不一定和你系统设置的文件或者服务的路径相一致，如果是这样，请你自己改一下。如果不改，造成的后果可能是致命的（系统崩溃，无法启动）。 





当然，你可以将SELINUX永久关闭掉，但不建议你这么去做。在RHCE的考试中，关掉SELINUX会被扣分而影响你的总成绩。如果你想临时关掉它，可以键入如下命令： setenforce 0 





在使用FTP时如果报错“cannot change directory。。。”十有八九就是SELINUX阻止掉了。你可以用setenforce 0 暂时关掉SELINUX后再尝试一下。或者关闭SELINUX对FTP的阻止 





setsebool ftpd_disable_trans 1



