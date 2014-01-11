---
author: ths
comments: true
date: 2010-12-14 04:48:32+00:00
layout: post
slug: vs%e4%b8%adwinform%e6%b7%bb%e5%8a%a0%e5%8d%b8%e8%bd%bd%e7%a8%8b%e5%ba%8f
title: vs中winform添加卸载程序
wordpress_id: 305
categories:
- 技术
tags:
- vs
- 卸载
---





在vs.net2005下并没有直接生成卸载程序的功能,不过我们可以用msi来实现，按如下步骤就可实现：  

    在添加你的应用程序项目的时候，多添加一个msiexec.exe进去,这个文件在c:windowssystem32文件夹下,添加进去以后,为了让它更像个卸载程序,把他的名字改成"Uninstall.exe",当然这个关系不大,改不改都行的.





然后给他创建一个快捷方式,放到桌面或者"开始-程序"中,我选择放在了开始菜单中,然后下面我们要的做的就是查找这个部署项目的ProductCode了,鼠标左键单击项目名称,记住是左键单击,然后点击属性标签,注意:不是右击的属性,这个区别很大,这时你就可以看到ProductCode了,然后打开你创建的那个快捷方式的属性对话框,在Aguements属性中输入"/x {ProductCode}",注意这里的ProductCode是上面的属性ProductCode的值，比如：{340EEB0D-7A37-4889-86C0-D772F6713377}





好了,然后点击"生成解决方案"即可生成带有卸载功能的安装程序了。



