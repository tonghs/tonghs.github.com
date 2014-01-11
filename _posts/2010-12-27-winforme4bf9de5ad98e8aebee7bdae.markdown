---
author: ths
comments: true
date: 2010-12-27 08:50:00+00:00
layout: post
slug: winform%e4%bf%9d%e5%ad%98%e8%ae%be%e7%bd%ae
title: winform保存设置
wordpress_id: 420
categories:
- 分享
- 技术
tags:
- winform
- 设置
---

1.右键解决方案选择属性
    2.找到“设置”在右边的表格中 点击右键选择 “添加设置”，填入自己需要保存的属性的名称、类型和默认值。如：
           a) 名称：IsBoss； 类型：bool；范围：用户； 值：False。
    3.在form窗体代码页，导入命名空间 ： using 项目名称.Properties
           a)如你的项目名称为 set 则导入 using set.Properties;
    4.在窗体的load方法中调用该值：
           a) this.checkBox1.Checked = Settings.Default.IsBoss;
    5.在窗体的FormClosing方法中保存此值：
           a) Settings.Default.IsBoss = this.checkBox1.Checked;
           b) Settings.Default.Save();   //这句一定不能少，切记
    6.OK，这样就行了。



