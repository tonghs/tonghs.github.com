---
author: ths
comments: true
date: 2010-11-30 05:25:14+00:00
layout: post
slug: '%e5%85%b3%e4%ba%8ediv%e4%b8%ad%e5%9e%82%e7%9b%b4%e5%af%b9%e9%bd%90%e5%92%8c%e6%b0%b4%e5%b9%b3%e5%af%b9%e9%bd%90%e7%9a%84%e9%97%ae%e9%a2%98%ef%bc%88%e5%85%bc%e5%ae%b9ie%e5%92%8cfirefox'
title: 关于div中垂直对齐和水平对齐的问题（兼容IE和Firefox)
wordpress_id: 136
categories:
- 技术
---





首先说水平对齐的问题，一般用text-align属性就可以了，但是仅用text-align：center；只能在ie中实现水平对齐，firefox中无法对齐，firefox可用下列属性，text-align: -moz-center !important;为了同时兼容ie和firefox，在实际写的时候要注意顺序firefox的属性在前，ie的属性在后，位置颠倒后无法ie无法解析，估计和浏览器的解析顺序有关，在vs2005中测试中是这样的。





下面说垂直居中问题，其实没有一个属性是严格的让元素在层中实现绝对的居中的，所谓的居中也是利用marginTop，即元素与浏览器上界面之间的空白区域实现的，只不过这个marginTop的值正好是屏幕的一半，有人要说了，现在屏幕的尺寸不一致怎么弄啊，这当然要用到JavaScript脚本动态控制marginTop的值了。





首先用JavaScript定义一个函数：










    


        

[view plain](http://blog.csdn.net/tonghuashuai2009/archive/2010/03/06/5351997.aspx#)[copy to clipboard](http://blog.csdn.net/tonghuashuai2009/archive/2010/03/06/5351997.aspx#)[print](http://blog.csdn.net/tonghuashuai2009/archive/2010/03/06/5351997.aspx#)[?](http://blog.csdn.net/tonghuashuai2009/archive/2010/03/06/5351997.aspx#)


    


    


        
  1. function init()

        
  2. {

        
  3. var obj = document.getElementById("main");

        
  4. obj.style.marginTop=screen.height/2-window.screenTop/2-100;

        
  5. }

    










然后在就是在页面加载的时候调用它了，可以在<body>标签中加onload时间调用init(),一开始我使用的是上面的代码，在ie中显示正常，但是在firefox中无法实现，问题出在window.screenTop上，firefox不支持，所以改用一下代码：










    


        

[view plain](http://blog.csdn.net/tonghuashuai2009/archive/2010/03/06/5351997.aspx#)[copy to clipboard](http://blog.csdn.net/tonghuashuai2009/archive/2010/03/06/5351997.aspx#)[print](http://blog.csdn.net/tonghuashuai2009/archive/2010/03/06/5351997.aspx#)[?](http://blog.csdn.net/tonghuashuai2009/archive/2010/03/06/5351997.aspx#)


    


    


        
  1. function init()

        
  2. {

        
  3. var obj = document.getElementById("tab");

        
  4. obj.style.marginTop=screen.height/2-200+"px";

        
  5. }

    










在这说一下为什么减掉200，screen.height/2所得到的值是屏幕的一半，而marginTop是元素到浏览器显示区域上边界的空白，如果是元素到屏幕上边界的空白就好了，可是事实不是这样，只能另想办法把把菜单栏、地址栏、工具栏等等的高度减去，但是我还没有找到怎么动态获得它们高度的方法，所有旧减掉了200，这样一来虽然不是绝对的居中但是还是可以接受的。



