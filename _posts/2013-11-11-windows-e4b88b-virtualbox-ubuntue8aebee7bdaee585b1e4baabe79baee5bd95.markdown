---
author: ths
comments: true
date: 2013-11-11 12:06:41+00:00
layout: post
slug: windows-%e4%b8%8b-virtualbox-ubuntu%e8%ae%be%e7%bd%ae%e5%85%b1%e4%ba%ab%e7%9b%ae%e5%bd%95
title: windows 下 virtualbox ubuntu设置共享目录
wordpress_id: 1259
categories:
- 技术
- 折腾
tags:
- ubuntu
- virtualbox
- 共享目录
---

有个紧急问题需要解决，公司手头没有linux机器，于是就在自己机子上折腾了，virtualbox ubuntu，最省事儿，在共享目录时遇到问题，只需两步，特将步骤记录如下：







  1. windows中操作：设置共享目录，Devices -> Shared Folders，添加一个共享文件夹，固定和临时无所谓，名字为win_share，最好是英文。



  2. 虚拟机中操作：sudo mkdir /mnt/shared





sudo mount -t vboxsf win_share /mnt/shared






取消挂载：sudo umount -f /mnt/shared



