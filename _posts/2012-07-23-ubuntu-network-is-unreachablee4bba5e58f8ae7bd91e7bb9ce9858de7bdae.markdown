---
author: ths
comments: true
date: 2012-07-23 12:26:00+00:00
layout: post
slug: ubuntu-network-is-unreachable%e4%bb%a5%e5%8f%8a%e7%bd%91%e7%bb%9c%e9%85%8d%e7%bd%ae
title: ubuntu network is unreachable以及网络配置
wordpress_id: 845
categories:
- 折腾
tags:
- linux
- network is unreachable
- ubuntu
- 网络配置
---

此问题的解决方法就是：增加一个缺省的网关。 





　　总结一下，步骤如下： 





　　1.配置ip，配置 /etc/network/interfaces 文件 





　　2.然后是DNS，配置 /etc/resolv.conf 





　　例如： 





　　配置静态IP地址 





　　sudo vim /etc/network/interfaces 





　　内容如下： 





　　auto lo 





　　iface lo inet loopback 





　　iface eth0 inet static 





　　address 172.16.15.97 





　　netmask 255.255.248.0 





　　gateway 172.16.15.253 





　　auto eth0 





　　配置DNS 





　　vim /etc/resolv.conf 





　　增加以下内容： 





　　nameserver 211.95.193.97 





　　nameserver 211.92.8.161 





　　3.增加默认网关 





　　route add default gw 172.16.15.253 





　　4.重新启动网络配置 





　　sudo /etc/init.d/networking restart



