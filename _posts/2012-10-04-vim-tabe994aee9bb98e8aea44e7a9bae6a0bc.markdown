---
author: ths
comments: true
date: 2012-10-04 13:52:02+00:00
layout: post
slug: vim-tab%e9%94%ae%e9%bb%98%e8%ae%a44%e7%a9%ba%e6%a0%bc
title: vim tab键默认4空格
wordpress_id: 883
categories:
- 折腾
---

为了vim更好的支持python写代码,修改tab默认4个空格有两种设置方法：
1. vim /etc/vimrc





> set ts=4
set sw=4







  1. vim /etc/vimrc





> set ts=4
set expandtab
set autoindent





我用的第一种方法实现的，mac 10.8.2系统 vim 7.3



