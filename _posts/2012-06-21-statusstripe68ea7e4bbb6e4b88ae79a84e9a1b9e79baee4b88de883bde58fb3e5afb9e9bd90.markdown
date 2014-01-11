---
author: ths
comments: true
date: 2012-06-21 06:46:00+00:00
layout: post
slug: statusstrip%e6%8e%a7%e4%bb%b6%e4%b8%8a%e7%9a%84%e9%a1%b9%e7%9b%ae%e4%b8%8d%e8%83%bd%e5%8f%b3%e5%af%b9%e9%bd%90
title: statusStrip控件上的项目不能右对齐
wordpress_id: 818
categories:
- 技术
tags:
- statusStrip
- winform
- 右对齐
---

方法一： 





在状态栏所有项目(StatusLabel、ProgressBar、DropDownButton等)前添加一个空白的StatusLabel (Text属性为空)，并将其Spring属性设为True。 





Spring属性的作用是设置该项是否填满剩余空间，设为True以后，当程序运行时后面的项就都挤到右边，实现右对齐。 





如果需要一部分项靠左，一部分靠右，那就在两部分中间插入空白StatusLabel，同时设其Spring属性为True。 





方法二： 





设置StatusStrip控件的LayoutStyle属性为HorizontalStackWithOverflow 或 StackWithOverflow。 





然后在代码中修改状态栏上某项的Alignment为Right，就有靠右效果。 





例如： this.toolStripStatusLabel1.Alignment = ToolStripItemAlignment.Right; 





注意如果是多个项，那靠左对齐的从左往右排列，靠右对齐的从右往左排列。



