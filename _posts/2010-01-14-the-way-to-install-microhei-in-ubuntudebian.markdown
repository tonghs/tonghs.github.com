---
author: ths
comments: true
date: 2010-01-14 07:53:00+00:00
layout: post
slug: the-way-to-install-microhei-in-ubuntudebian
title: The way to install MicroHei in ubuntu/debian
wordpress_id: 80
categories:
- 折腾
tags:
- font
- it
- microhei
- ubuntu/debian
---

First, extract the font files with





  






   tar zxvf
wqy-microhei*.tar.gz





  






Then, change to root user, move the extracted folder,
"wqy-microhei"





under /usr/share/fonts/wenquanyi/ (If this dir does not exist,
use





mkdir -p /usr/share/fonts/wenquanyi/ to create it
first.)





  






Then edit /etc/X11/xorg.conf or /etc/X11/XF86Config-4





and find the section with FontPath. Append





  






   FontPath
/usr/share/fonts/wenquanyi/wqy-microhei





  






under any of the FontPath line, save this file.





  






Then, if your system has /etc/fonts/fonts.conf, edit





it and append





  







  <dir>/usr/share/fonts/wenquanyi/wqy-microhei/</dir>





  






before </fontconfig>





  






  






Restart X server and you should be able to use this
font.



