---
author: ths
comments: true
date: 2012-08-10 05:56:00+00:00
layout: post
slug: '%e8%a3%85%e4%ba%86flash-player%e5%8d%b4%e6%89%93%e4%b8%8d%e5%bc%80swf-%ef%bc%9f'
title: 装了flash player却打不开swf ？
wordpress_id: 848
categories:
- 折腾
tags:
- flashplayer
- swf
---

[![clip_image002](http://img1.51cto.com/attachment/200911/25/13184_1259140451gDeC.jpg)](http://img1.51cto.com/attachment/200911/25/13184_1259140450suYU.jpg)





文件图标是讨厌的方块，表面就是没有程序关联的文件格式。。。 





再看看控制面板的“添加删除程序” 





[![clip_image004](http://img1.51cto.com/attachment/200911/25/13184_1259140452HL5Z.jpg)](http://img1.51cto.com/attachment/200911/25/13184_1259140451W2SQ.jpg)





看起来应该没啥问题。既然如此，咱就重装一遍flash playere咯 





上官网，到下载页面[http://get.adobe.com/flashplayer/](http://get.adobe.com/flashplayer/)





[![clip_image006](http://img1.51cto.com/attachment/200911/25/13184_1259140453qU3u.jpg)](http://img1.51cto.com/attachment/200911/25/13184_1259140452cE9E.jpg)





一步步的下载，安装，完成。问题依旧。程序没问题，文件也没问题。只好问baidu喽 





原因基本上弄清楚了，因为默认情况下官网提供的 flash player都是浏览器关联的，例如我们在控制面板的“添加删除程序”里面看到的“Adobe Flash Player 10 ActiveX”就是IE的控件。 





而我们需要的是独立的（standalone）播放器。网上提供的一般的解决办法都是变通的使用暴风之类播放器来打开。但总觉得没原来的player小巧玲珑啊。 





功夫不负有心人啊，终于给让我找到了。原来独立的flash player是跟着开发工具Flash CS4 Professional套件一起的。官网提供了下载页面 





[http://www.adobe.com/support/flashplayer/downloads.html](http://www.adobe.com/support/flashplayer/downloads.html)，注意和上面的页面是不同的。如下图 





[![clip_image008](http://img1.51cto.com/attachment/200911/25/13184_1259140459XOjz.jpg)](http://img1.51cto.com/attachment/200911/25/13184_1259140455nkso.jpg)





下载这个44MB的zip包解压就会看到我们要的FlashPlayer.exe 





[![clip_image010](http://img1.51cto.com/attachment/200911/25/13184_1259140461L8Kc.jpg)](http://img1.51cto.com/attachment/200911/25/13184_1259140460friT.jpg)





将它copy到程序安装目录C:WINDOWSsystem32MacromedFlash下即可。 





接下来当然就是右击swf文件，选择打开方式，指定以FlashPlayer.exe来打开，搞定！以后就都可以直接双击打开了。



