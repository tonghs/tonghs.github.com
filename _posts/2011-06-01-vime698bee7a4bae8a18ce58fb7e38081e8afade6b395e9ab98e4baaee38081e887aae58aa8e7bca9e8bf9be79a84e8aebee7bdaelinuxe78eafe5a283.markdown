---
author: ths
comments: true
date: 2011-06-01 02:57:00+00:00
layout: post
slug: vim%e6%98%be%e7%a4%ba%e8%a1%8c%e5%8f%b7%e3%80%81%e8%af%ad%e6%b3%95%e9%ab%98%e4%ba%ae%e3%80%81%e8%87%aa%e5%8a%a8%e7%bc%a9%e8%bf%9b%e7%9a%84%e8%ae%be%e7%bd%aelinux%e7%8e%af%e5%a2%83
title: vim显示行号、语法高亮、搜索字符串高亮、自动缩进的设置(Linux环境)
wordpress_id: 633
categories:
- 折腾
tags:
- vim
- 搜索字符串高亮
- 自动缩进
- 行号
- 语法高亮
---

在终端 输入以下命令来编辑vimrc配置文件：  
sudo vim /etc/vim/vimrc  
或者 sudo gedit /etc/vim/vimrc  
1、显示行号  
在文件末端添加一新行，输入 set nu  
2、语法高亮  
在文件中找到 "syntax on 这一行，去掉前面的双引号"，双引号是注释的意思  
3、自动缩进  
在文件末尾添加一行，输入 set autoindent  
在添加一行，输入 set cindent  
其中 autoindent 是自动缩进； cindent是特别针对 C语言语法自动缩进  
4、搜索字符串高亮  
在 vimrc 里加入：set hlsearch



