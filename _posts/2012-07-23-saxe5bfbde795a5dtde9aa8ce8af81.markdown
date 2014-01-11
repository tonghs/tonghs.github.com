---
author: ths
comments: true
date: 2012-07-23 11:28:00+00:00
layout: post
slug: sax%e5%bf%bd%e7%95%a5dtd%e9%aa%8c%e8%af%81
title: SAX忽略dtd验证
wordpress_id: 824
categories:
- 技术
tags:
- dtd
- xml
---

最近遇到一个问题，解析xml时非常慢，时不时提示网络无法到达错误，后来得知是解析xml需要验证dtd，于是搜得一下方法  
把Validating设成false   





    
    SAXParserFactory   spfactory   =   SAXParserFactory.newInstance();  
    spfactory.setValidating(<span class="kwrd">false</span>);





或者








    
    SAXBuilder   builder   =   <span class="kwrd">new</span>   SAXBuilder( <span class="str">"org.apache.xerces.parsers.SAXParser "</span>,   <span class="kwrd">true</span>);
    builder.setFeature( <span class="str">"http://apache.org/xml/features/nonvalidating/load-external-dtd "</span>,   <span class="kwrd">false</span>);  
    







