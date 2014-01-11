---
author: ths
comments: true
date: 2011-07-08 08:41:00+00:00
layout: post
slug: '%e4%bd%bf%e7%94%a8updatepanel%e5%90%8e%e6%97%a0%e6%b3%95%e5%bc%b9%e5%87%ba%e6%8f%90%e7%a4%ba%e4%bf%a1%e6%81%af'
title: 使用updatepanel后无法弹出提示信息
wordpress_id: 652
categories:
- 技术
tags:
- Ajax
- updatepanel
- 控件
---

在使用updatepanel控件后原本可以弹出的alert框失效了,上网查了查,找到了如下解决方法.





<





p>传统的方式是利用





<





p>********Page.ClientScript.RegisterStartupScript****来注册客户端脚本实现信息提示，但这种方式在ajax中不起作用，必须选择





<





p>**System.Web.UI.ScriptManager.RegisterStartupScript来替代Page.ClientScript.RegisterStartupScript**





<





p>**举例:**





**System.Web.UI.ScriptManager.RegisterStartupScript**(this.updatepanel1, this.GetType(), "unReport", "alert('保存成功！');window.close();", true);



