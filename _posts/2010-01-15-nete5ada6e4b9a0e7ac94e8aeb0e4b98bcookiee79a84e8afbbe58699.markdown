---
author: ths
comments: true
date: 2010-01-15 11:43:00+00:00
layout: post
slug: net%e5%ad%a6%e4%b9%a0%e7%ac%94%e8%ae%b0%e4%b9%8bcookie%e7%9a%84%e8%af%bb%e5%86%99
title: .net学习笔记之Cookie的读写
wordpress_id: 78
categories:
- 技术
tags:
- cookie
- it
---

//写入Cookie<br/>
       
HttpCookie cookie = new HttpCookie("newcookie");<br/>
       
cookie["name"] = "tonghuashuai";<br/>
       
cookie["age"] = "27";<br/>
       
cookie["dt"] = DateTime.Now.ToString();<br/>
       
Response.Cookies.Add(cookie);<br/>
       
Response.Write("写入成功");<br/>
//读出Cookie<br/>
       
HttpCookie getcook = Request.Cookies["newcookie"];<br/>
       
Response.Write(getcook["name"]);<br/>
       
Response.Write("<br>" +
getcook["age"]);<br/>
       
Response.Write("<br>" +
getcook["dt"]);<br/><br/>



