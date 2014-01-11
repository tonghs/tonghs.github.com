---
author: ths
comments: true
date: 2011-03-16 07:53:00+00:00
layout: post
slug: mysql-unknown-command-%e9%97%ae%e9%a2%98
title: mysql unknown command ‘''问题
wordpress_id: 559
categories:
- 技术
tags:
- mysql
- unknown command ‘''
---

在制作数据库自动安装包时遇到了这个提示：mysql unknown command ‘''，看了一下sql脚本文件，发现是一个转义字符，不应该出错的，google了一翻发现了如下问题：





打开sql脚本文件，查找character-set方式，发现时utf8，但是我的数据库是sjis的，所以问题就出在这了





解决方法如下：





在mysql命令中添加--default-character-set参数即可，构造为：mysql -h %host% -u %username% -p%password% --default-character-set=utf8 < picprocess.sql



