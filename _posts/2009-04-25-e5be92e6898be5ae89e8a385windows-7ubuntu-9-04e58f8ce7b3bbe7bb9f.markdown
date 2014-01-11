---
author: ths
comments: true
date: 2009-04-25 14:33:00+00:00
layout: post
slug: '%e5%be%92%e6%89%8b%e5%ae%89%e8%a3%85windows-7ubuntu-9-04%e5%8f%8c%e7%b3%bb%e7%bb%9f'
title: 徒手安装windows 7+ubuntu 9.04双系统
wordpress_id: 94
categories:
- 折腾
tags:
- boot
- windows
- 双系统
- 电脑
- 盘根
---


**最近windows里最火的是windows7，linux里最火的当属ubuntu9.04了，相信喜欢尝鲜的朋友已经用过了。本人电脑迷一个，喜欢玩系统，今天就在这里吧两个最火的系统安装到一块，很爽的啊！**






**这里说徒手是指只要有一台联网的电脑就可以了，我们选择硬盘完全安装，为什么要选择这种安装方式呢，原因如下：1.不愿花银子去卖光盘刻，再说也没有刻录机，ubuntu倒是可以免费得到，可是得等啊，于是只能硬盘安装；2.既然是尝鲜，还是全新安装的比较好，升级的没感觉。**






**下面正式开始，安装思路是先安装windows7，然后是ubuntu9.04，然后修改grub增加windows启动项。**





**具体步骤如下：**





**一、安装windows7**





**请参考我以前的文章[http://blog.sina.com.cn/s/blog_5e66e6c90100cqsn.html](http://blog.sina.com.cn/s/blog_5e66e6c90100cqsn.html)**





**二、安装ubuntu9.04**





**到**[**www.ubuntu.com.cn**](http://www.ubuntu.com.cn/)**下载ubuntu9.04的光盘镜像到C盘根目录，将casper目录下的initrd.gz和vmlinuz解压到C盘根目录，到**[**http://www.xdowns.com/soft/xdowns.asp?softid=47562&downid=30&id=50273**](http://www.xdowns.com/soft/xdowns.asp?softid=47562&downid=30&id=50273)**下载grub4dos解压其中的grldr、grldr.mbr、grub.exe（注意一定要有grldr.mbr，如果是xp就不用了，如果是vista、win7就一定要有grldr.mbr，切记！）****然后新建memu.lst文件内容如下：**





**title
Install Ubuntu 9.04**** **





**root
(hd0,0) **





**kernel
(hd0,0)/vmlinuz boot=casper
iso-scan/filename=/ubuntu-9.04-desktop-i386.iso ro quiet splash
locale=zh_CN.UTF-8**





**initrd
/initrd.gz **





**boot  
**






**复制xp系统里的boot.ini到C盘根目录，在最后一行加上c:grldr.mbr="grub"（注意是grldr.mbr）如果身边没有xp系统那我就吧boot.ini的代码贴出来供大家使用了，代码如下：**





**[boot loader]  

timeout=30  

default=multi(0)disk(0)rdisk(0)partition(1)WINDOWS  

[operating systems]  

multi(0)disk(0)rdisk(0)partition(1)WINDOWS="Microsoft Windows XP
Professional" /noexecute=optin /fastdetect  

c:grldr.mbr="grub"**






**至此准备工作完成，重启机器，在选择菜单选择grub，就会自动进入ubuntu的live
cd桌面环境，接下来的一步也很重要啊，打开终端（应用程序-附件-终端）输入如下代码：**





**sudo umount -l
/isodevice**






**然后双击桌面上的安装图标，安装正式开始，安装和分区有自己看情况定，在此不再赘述。**






**三、修改grub添加windows启动菜单**






**安装完重启后会发现无法进入windows7，需要我们进行如下步骤：**





**进入ubuntu，打开终端，输入“sudo gedit
/boot/grub/menu.lst加入如下代码即可：**





**title
Windows  Seven  

root (hd0,0)  

makeactive  

chainloader +1**






**再适当设置一下等待时间就大公告成了，这样在启动时，按esc即可进行多系统选择了。**






**至此，windows7+ubuntu9.04双系统安装完毕。  
**





**  

 **



