---
author: ths
comments: true
date: 2013-06-10 05:18:07+00:00
layout: post
slug: mysql-workbench%e5%bf%ab%e6%8d%b7%e9%94%ae%e8%ae%be%e7%bd%ae
title: MySQL Workbench快捷键设置
wordpress_id: 1161
categories:
- 技术
- 折腾
tags:
- MySQL Workbench
- 自定义快捷键
---

MySQL Workbench是MySQL官方的客户端，但是有些快捷键使用不方便，想自定义，Google得如下方法（有人在StackOverflow的提问）：





You can modify the `main_menu.xml` file (for me on Ubuntu 12.04 this was in `/usr/share/mysql-workbench/data/`). After you modify it, you'll need to restart MySQL Workbench.





It'll look like this




    
    <code>    <value type="object" struct-name="app.MenuItem" id="com.mysql.wb.menu.query.exec"> 
          <link type="object" key="owner" struct-name="app.MenuItem">com.mysql.wb.menu.query</link> 
          <value type="string" key="caption">Execute (All or Selection)</value> 
          <value type="string" key="name">query.execute</value> 
          <value type="string" key="command">builtin:query.execute</value> 
          <value type="string" key="itemType">action</value> 
          <value type="string" key="shortcut">Modifier+E</value>
        </value></code>





The second to last line (Modifier+E) was edited by me. Previously it said "Modifier+Shift+Return". Note that this is NOT an alias (you cannot have both).



