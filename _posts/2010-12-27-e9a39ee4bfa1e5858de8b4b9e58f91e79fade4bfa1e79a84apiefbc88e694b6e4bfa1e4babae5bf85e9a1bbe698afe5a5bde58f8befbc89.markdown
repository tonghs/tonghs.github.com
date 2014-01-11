---
author: ths
comments: true
date: 2010-12-27 08:53:00+00:00
layout: post
slug: '%e9%a3%9e%e4%bf%a1%e5%85%8d%e8%b4%b9%e5%8f%91%e7%9f%ad%e4%bf%a1%e7%9a%84api%ef%bc%88%e6%94%b6%e4%bf%a1%e4%ba%ba%e5%bf%85%e9%a1%bb%e6%98%af%e5%a5%bd%e5%8f%8b%ef%bc%89'
title: 飞信免费发短信的API（收信人必须是好友）
wordpress_id: 421
categories:
- 分享
- 技术
tags:
- API
- 飞信
---

<





p>[飞信](http://www.fetion.com.cn/)是由中国移动通信集团公司推出的一款集商务应用和娱乐功能为一体的，基于手机应用以及与Internet深度互通的即时通讯产品，可免费给好友发送短信。  
　　1、下载中国移动飞信PC客户端软件（[http://www.fetion.com.cn/downloads/pc.aspx](http://www.fetion.com.cn/downloads/pc.aspx)），并注册开通飞信。注册成为飞信用户，下载飞信PC客户端、使用PC客户端基本功能，不收取费用。  
　　2、通过PC客户端，邀请并添加免费短信接收方的手机号码（仅限中国移动）到您的飞信好友，该手机号需要通过通过PC客户端、或回复短信接受您的邀请；  
　　3、通过 [http://sms.api.bz/](http://sms.api.bz/) 提供的 API 接口，即可免费给飞信好友发短信。利用本API接口可进行日程提醒、服务器监控、报警、故障通知或短信自动控制等功能。





* * *





<





p>飞信免费发短信API接口在线演示： [http://sms.api.bz/](http://sms.api.bz/)  
　　飞信免费发短信API接口调用方式（通过HTTP访问以下网址、支持GET和POST）：





<





p>[http://sms.api.bz/fetion.php?username=](http://sms.api.bz/fetion.php?username=)您的移动飞信登录手机号&password=您的移动飞信登录密码&sendto=接收短信的飞信好友手机号&message=短信内容





<





p>　　注：短信内容最大长度为180个汉字，超过180个汉字不发送。返回的信息为UTF-8编码的中文文本信息。





* * *





<





p>　　例1：在Linux命令行下通过curl命令给自己的手机号（假设为13800138000）发送短信





<





p>curl [http://sms.api.bz/fetion.php?username=13800138000&password=123456&sendto=13800138000&message=短信内容](http://sms.api.bz/fetion.php?username=13800138000&password=123456&sendto=13800138000&message=短信内容)





注意事项：用该方法发信息时，收信人必须是自己好友



