---
author: ths
comments: true
date: 2010-12-27 08:37:00+00:00
layout: post
slug: google-app-engine%e6%90%ad%e5%bb%batwitter-api-proxy%e6%95%99%e7%a8%8b%ef%bc%88%e5%9b%be%e6%96%87%e7%89%88%ef%bc%89
title: Google App Engine搭建Twitter API Proxy教程（图文版）
wordpress_id: 415
categories:
- 分享
- 技术
tags:
- GAE
---

<





p>[  
![Photobucket](http://i575.photobucket.com/albums/ss197/tjf6892/google_app_engine.jpg)](http://s575.photobucket.com/albums/ss197/tjf6892/?action=view&current=google_app_engine.jpg)





#### Google app engine 是什么？





<





p>Google app engine 是 Google 提供的一个在线应用程序平台，支持 Python和Java。简单的说是在 Google app engine 上面直接运行用 Python/Java 写的程序，由 Google app engine 提供网络空间和带宽。





#### 什么是Twitter API proxy?





<





p>总的说来HTTP请求有两种不同形式，POST和GET（其实还有其它的一些请求,本文简略）。“Twitter REST API”也是通过这两种形式来调用的。





<





p>那么我们通过第三方应用或者第三方编程语言来调用Twitter REST API是不是和通常我们使用的代理相类似.说到这里Twitter API proxy不言而喻!





<





p>简单地说，就是把客户端发过来的POST和GET请求转发到原始API地址，并将返回的http header和内容返回给客户端，实现了原始twitter API的所有功能。而对客户端来说，除了提供一个可供配置的API地址选项，不需要做任何代码上的更改.(此段话为twip作者介绍,简单明了)





<





p>下面举个场景,通常你要查看某上推友的信息最常用方法是在twitter.com上直接查看，其实调用的是下面请求：  
GET [http://twitter.com/statuses/show/twitterapi.json](http://twitter.com/statuses/show/twitterapi.json)





<





p>如果你通过第三方应用或者第三方编程调用就是另外的一种请求方法了,假设你在[http://none.com/api架设了一个Twitter](http://none.com/api%E6%9E%B6%E8%AE%BE%E4%BA%86%E4%B8%80%E4%B8%AATwitter) API proxy，那么你可以用以下方式调用相同的API：





<





p>GET [http://none.com/api/status/show/twitterapi.json](http://none.com/api/status/show/twitterapi.json) 得到的效果是相同的.





#### **环境准备：Google App Engine**





<





p>先要注册Google App Engine，注册地址 [http://appengine.google.com/](http://appengine.google.com/) ，然后建立一个application，目前第一次使用需要验证用户手机，输入手机号码就收验证码即可，之后，就可以用yourid.appspot.com来访问你的app应用。





<





p>[![Photobucket](http://i575.photobucket.com/albums/ss197/tjf6892/6E7D1BDE6453DADE57CB41E2677F986F.jpg)](http://s575.photobucket.com/albums/ss197/tjf6892/?action=view&current=6E7D1BDE6453DADE57CB41E2677F986F.jpg)





<





p>目前第一次使用需要验证用户手机，输入手机号码就收验证码即可





<





p>[![Photobucket](http://i575.photobucket.com/albums/ss197/tjf6892/DCB1F0398A0C2DC0C858C3D1AE910691.jpg)](http://s575.photobucket.com/albums/ss197/tjf6892/?action=view&current=DCB1F0398A0C2DC0C858C3D1AE910691.jpg)





<





p>填写 **Application Identifier** (输入你想要的应用程序地址，相应会得到一个 yourid.appspot.com 的域名，记住这个) 和 **Application Title** (标题)以及勾选同意服务条款，点 **Save** 即完成创建。





<





p>[![Photobucket](http://i575.photobucket.com/albums/ss197/tjf6892/08B5B1EE2487CDA8BEBE296698D123EC.jpg)](http://s575.photobucket.com/albums/ss197/tjf6892/?action=view&current=08B5B1EE2487CDA8BEBE296698D123EC.jpg)





<





p>此外，还需要下载安装Google APP Engine的开发环境，注意Python的版本，需要是2.5系列的，不能使用2.6或更高的版本，否则运行会出错。





<





p>Google App Engine SDK 下载地址 [http://code.google.com/intl/zh-CN/appengine/downloads.html](http://code.google.com/intl/zh-CN/appengine/downloads.html)





<





p>Python 2.5.4 下载地址 [http://www.python.org/download/releases/2.5.4/](http://www.python.org/download/releases/2.5.4/)





<





p>关于Google App Engine的详细使用说明请参见[这个地址](http://www.williamlong.info/archives/1880.html)





#### **环境准备：BirdNest**





<





p>下载birdnest要注意是下载[分支branches/gae](http://birdnest.googlecode.com/svn/branches/gae)，别下载主干trunk，否则更新到GAE上也不能用，会报错。可以使用一个SVN工具下载。例如TortoiseSVN等。将其放到一个目录中，进入目录，编辑app.yaml文件，将第一行的application里的参数修改为自己的应用名。





<





p>注：derek我[打包birdnest下载](http://www.uushare.com/user/tjf6892/file/2275315)，免得在安装工具麻烦了！





<





p>[![Photobucket](http://i575.photobucket.com/albums/ss197/tjf6892/971FF43B2D2A7B36F06C4AAABB9DCFCA.jpg)](http://s575.photobucket.com/albums/ss197/tjf6892/?action=view&current=971FF43B2D2A7B36F06C4AAABB9DCFCA.jpg)





<





p>TortoiseSVN 下载地址：[http://tortoisesvn.net/downloads](http://tortoisesvn.net/downloads) （注意后面的Language packs下载，英文好的童鞋请无视）





<





p>TortoiseSVN使用方法：下载安装完毕后，在**Google APP Engine**安装目录（如我的E:Googlegoogle_appengine）下**新建一个文件夹**，随意起个名字（我的justinwayy），**右键单击文件夹**，在弹出菜单中选择**SVN检出**，然后在版本库URL中填入**Birdnest/gae的url**（**[http://birdnest.googlecode.com/svn/branches/gae/](http://birdnest.googlecode.com/svn/branches/gae/)**），点击确定，成功检出。





#### **发布应用到**Google App Engine





<





p>准备好了上面的一切后，就可以发布这个应用到自己的Appspot上了，执行 appcfg.py update 目录名，中间会要求输入Gmail的用户名和密码（输入密码时无反应，事实上密码已经录入了），之后就可以使用了。你创建的API地址应该是[yourid.appspot.com/api/](http://yourid.appspot.com/api/) 。  
[![Photobucket](http://i575.photobucket.com/albums/ss197/tjf6892/CBC4DA6D41D05EC721BB5C03DFFBD50F.jpg)](http://s575.photobucket.com/albums/ss197/tjf6892/?action=view&current=CBC4DA6D41D05EC721BB5C03DFFBD50F.jpg)





#### **使用BirdNest**





<





p>在twhirl里的使用方法是，打开账号管理Accounts manager，选择laconi.ca账户类型，输入：[你的twitter帐号名]@yourid.appspot.com，密码为Twitter密码，即可使用。





<





p>在twitterfox里的使用方法是，打开 C:Documents and SettingsAdministratorApplication DataMozillaFirefoxProfiles 随机信息 [.defaultextensionstwitternotifier@naan.net](mailto:.defaultextensionstwitternotifier@naan.net)components目录，编辑 nsTwitterFox.js文件，找不到的话直接在Documents and Settings中搜索nsTwitterFox.js文件，编辑该文件的38行，将其修改为 var TWITTER_API_URL = [http://yourid.appspot.com/api/](http://yourid.appspot.com/api/) 即可。





<





p>后记：实际在应中不是那么顺，通过api地址访问时在页面跳转时容易出错，所以就不再用了，只做学习了



