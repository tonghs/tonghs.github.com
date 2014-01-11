---
author: ths
comments: true
date: 2012-08-10 06:22:00+00:00
layout: post
slug: redhat-rhel-6-1%e5%ae%89%e8%a3%85gcc
title: RedHat RHEL 6.1安装gcc
wordpress_id: 850
categories:
- 折腾
tags:
- gcc
- RedHat RHEL 6.1
---

HEL 6.1默认是没有gcc和gcc-c++环境的，而且我也没有$购买正版服务。  
只能想办法本地安装了，总结方法如下：  
上传安装镜像rhel-server-6.1-x86_64-dvd.iso，  
然后将镜像文件挂，如/mnt  
# mount -o loop rhel-server-6.1-x86_64-dvd.iso /mnt  
# cd /mnt/Packages  
# rpm -ivh glibc-common-2.12-1.25.el6.x86_64.rpm  
# rpm -ivh kernel-headers-2.6.32-131.0.15.el6.x86_64.rpm  
# rpm -ivh libgcc-4.4.5-6.el6.x86_64.rpm  
# rpm -ivh glibc-2.12-1.25.el6.x86_64.rpm  
# rpm -ivh libgomp-4.4.5-6.el6.x86_64.rpm  
# rpm -ivh nscd-2.12-1.25.el6.x86_64.rpm  
# rpm -ivh glibc-headers-2.12-1.25.el6.x86_64.rpm  
# rpm -ivh glibc-devel-2.12-1.25.el6.x86_64.rpm  
# rpm -ivh mpfr-2.4.1-6.el6.x86_64.rpm  
# rpm -ivh ppl-0.10.2-11.el6.x86_64.rpm  
# rpm -ivh cloog-ppl-0.15.7-1.2.el6.x86_64.rpm  
# rpm -ivh cpp-4.4.5-6.el6.x86_64.rpm  
# rpm -ivh gcc-4.4.5-6.el6.x86_64.rpm  
注：以上是安装gcc，软件安装顺序不能错。  
******************************************  
# rpm -ivh libstdc++-4.4.5-6.el6.x86_64.rpm  
# rpm -ivh libstdc++-devel-4.4.5-6.el6.x86_64.rpm  
# rpm -ivh gcc-c++-4.4.5-6.el6.x86_64.rpm  
注：以上是安装gcc-c++



