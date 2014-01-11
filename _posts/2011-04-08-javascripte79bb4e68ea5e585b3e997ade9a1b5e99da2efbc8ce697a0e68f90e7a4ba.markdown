---
author: ths
comments: true
date: 2011-04-08 07:51:00+00:00
layout: post
slug: javascript%e7%9b%b4%e6%8e%a5%e5%85%b3%e9%97%ad%e9%a1%b5%e9%9d%a2%ef%bc%8c%e6%97%a0%e6%8f%90%e7%a4%ba
title: javascript直接关闭页面，无提示
wordpress_id: 604
categories:
- 技术
tags:
- javascript
- 关闭页面
---

<





p>在做一个带注册码的程序，如果注册不成功就自动关闭页面，用javascript关闭页面时会有提示：“您正在查看的网页正在试图关闭窗口 是否关闭窗口?”，如果点否的话就不关闭了，这就不能实现未注册限制了。怎么能不提示就直接关闭呢？方法如下：




    
    <script>
    window.opener=null;
    window.open('','_self');
    window.close();
    window.location.href="intro.html";
    </script>



