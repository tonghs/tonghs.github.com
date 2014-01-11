---
author: ths
comments: true
date: 2013-07-06 02:37:29+00:00
layout: post
slug: '%e8%ae%a9eclipse%e6%94%af%e6%8c%81%e7%b1%bb%e4%bc%bcvs%e7%9a%84region'
title: 让eclipse支持类似VS的Region
wordpress_id: 1179
categories:
- 分享
- 折腾
tags:
- coffee-bytes
- eclipse
- folding
- region
---

原帖地址：_[http://my.oschina.net/goberl/blog/63654](http://my.oschina.net/goberl/blog/63654)_





1.插件下载、安装
eclipse plugin：http://incubator.apache.org/isis/com.cb.eclipse.folding.KAM-3.5.zip（也叫com.cb.eclipse.folding 1.06，还有个名字：coffee-bytes），若链接失效可搜索名称找资源。复制插件到相应目录，重启eclipse。





2.插件配置
选择 "Windows->Preferences"





选择 "Java->Editor->Folding"





选中 "Enable folding" option





在 "Select folding to use:" 选项中选择 "Coffee Bytes Java Folding"





选中 "User Defined Regions" 然后到"User Defined Regions"下设置一下标示符。





确定后重启eclipse即可生效。





![](http://static.oschina.net/uploads/space/2012/0625/112848_VLpl_197184.png)
![](http://static.oschina.net/uploads/space/2012/0625/112908_GNtG_197184.png)
![](http://static.oschina.net/uploads/space/2012/0625/112920_Ca6c_197184.png)



