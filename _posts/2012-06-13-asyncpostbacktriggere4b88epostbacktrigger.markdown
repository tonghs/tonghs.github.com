---
author: ths
comments: true
date: 2012-06-13 06:49:00+00:00
layout: post
slug: asyncpostbacktrigger%e4%b8%8epostbacktrigger
title: AsyncPostBackTrigger与PostBackTrigger
wordpress_id: 808
categories:
- 技术
tags:
- AsyncPostBackTrigger
- PostBackTrigger
- 局部刷新
---

在ASP.NET AJAX中有两种Triggers：分别为AsyncPostBackTrigger和PostBackTrigger，AsyncPostBackTrigge用来指定某个服务器端控件以及其将触发的服务器端事件作为该UpdatePanel的异步更新触发器，它需要设置的属性有控件ID和服务端控件的事件；PostBackTrigger用来指定在UpdatePanel中的某个服务端控件，它所引发的回送不使用异步回送，而仍然是传统的整页回送。 





写个例子: 





updatepanel 中有个button 如果给它设置成PostBackTrigger .点button页面刷新 





updatepanel 外有个 button 如果给它设置成AsyncPostBackTrigger 点button页面不刷新



