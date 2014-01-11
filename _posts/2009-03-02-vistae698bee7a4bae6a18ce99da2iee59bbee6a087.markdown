---
author: ths
comments: true
date: 2009-03-02 00:36:00+00:00
layout: post
slug: vista%e6%98%be%e7%a4%ba%e6%a1%8c%e9%9d%a2ie%e5%9b%be%e6%a0%87
title: vista显示桌面IE图标
wordpress_id: 107
categories:
- 折腾
tags:
- ie
- vista
- 电脑
---


**前天下血本给我的小黑加到了1G内存，运行速度终于上来了，把windows7格了换了vista，跑的还行，比512内存时流畅了不少，不过还是有些停顿，现在就说说vista一个很不爽的问题：桌面IE图标的问题，虽说可以在桌面建立它的快捷方式，可是看着多不爽啊，下面就是找回IE图标的方法：**





**找到如下的注册表分支：  

　　HKEY_CURRENT_USERSoftwareMicrosoftWindowsCurrentVersion
Explorer HideDesktopIcons NewStartPanel（注：当Windows
Vista使用经典主题时，则应为:  

HKEY_CURRENT_USERSoftwareMicrosoftWindowsCurrentVersionExplorerHideDesktopIcons
ClassicStartMenu）如果不存在相应分支，创建之;创建名为“{871C5380-42A0-1069-A2EA-08002B30309D}”的DWORD
(32位)注册表项;将其值设为“0”。**






**回到桌面，刷新就可以看看熟悉的IE了。**



