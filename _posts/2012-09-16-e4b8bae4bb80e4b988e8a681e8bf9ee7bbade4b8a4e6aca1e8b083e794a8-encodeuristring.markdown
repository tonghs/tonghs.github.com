---
author: ths
comments: true
date: 2012-09-16 08:48:00+00:00
layout: post
slug: '%e4%b8%ba%e4%bb%80%e4%b9%88%e8%a6%81%e8%bf%9e%e7%bb%ad%e4%b8%a4%e6%ac%a1%e8%b0%83%e7%94%a8-encodeuristring'
title: Struts2中js传值及GET方式传值中文乱码问题！
wordpress_id: 880
categories:
- 技术
tags:
- 调用 encodeURI(String)
---

Struts2中js传值及GET方式传值中文乱码问题！





js代码 
    
    function submit(){  
        var title=document.getElementByIdx_x("test");  
        var url="/ActionTest/ActionFirst.action?test="+encodeURI(encodeURI(title.innerHTML));  
        window.location.href=url;  
    } 
    
    function submit(){
        var title=document.getElementByIdx_x("test").value;
        var url="/ActionTest/ActionFirst.action?test="+title.innerHTML;
        window.location.href=encodeURI(url);
    }
    
    








页面中的值！






Java代码

    
    <input type="text" name="test" id="test"/>  
    <input type="submit" value="提交" onClick="javascript:submit();"/>  
     <input type="text" name="test" id="test"/>
    <input type="submit" value="提交" onClick="javascript:submit();"/>
    

  
服务器端解码后打印






Java代码






后台

    
    String test = request.getParameter("test")+"";
    test = java.net.URLDecoder.decode(test, "UTF-8"));
    System.out.println(test); 
    

  
前台转两次码，后台转一次码。。






为什么要连续两次调用 encodeURI(String) 方法呢？是因为 Java 中的 request.getParameter(String) 方法会进行一次 URI 的解码过程，调用时内置的解码过程会导致乱码出现。而 URI 编码两次后， request.getParameter(String) 函数得到的是原信息 URI 编码一次的内容。接着用 java.net.URLDecoder.decode(String str,String codename) 方法，将已经编码的 URI 转换成原文。



