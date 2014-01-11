---
author: ths
comments: true
date: 2012-07-23 12:09:00+00:00
layout: post
slug: linux%e4%b8%8b-c%e8%af%ad%e8%a8%80-cgi%e7%8e%af%e5%a2%83%e6%b5%8b%e8%af%95
title: linux下 c语言 CGI环境测试
wordpress_id: 837
categories:
- 技术
tags:
- c
- CGI
- linux
---

**1,在Redhat9下建立hello.c文件**




    
    #include <stdio.h>
    #include <<span class="kwrd">string</span>.h>
    
    main()
    {
        printf(<span class="str">"Content type: text/html/n/n"</span>);
       
        printf(<span class="str">"<html>/n"</span>);
        printf(<span class="str">"<head><title>An html page from a cgi</title></head>/n"</span>);
        printf(<span class="str">"<body bgcolor=/"</span>#666666/<span class="str">"></body>/n"</span>);
        printf(<span class="str">"</html>/n"</span>);
        fflush(stdout);
    }
    
    









****






**2,编译生成hello.cgi文件。**






**#arm-linux-gcc -o hello.cgi hello.c**






**3,将hello.cgi文件放到目标板网页服务器主目录。**






**4,修改其权限，这一步非常重要，我就是因为这一步走了很多弯路。**






**#chmod +x hello.cgi**






**5,通过浏览器访问**






**地址栏写入**






**10.10.145.91/hello.cgi**






**这样就会显示hello.cgi生成的页面。**






**注意，这里只是输出页面能够成功，但是，我做了另外的测试，  
比如用system函数来执行shell命令就会出现问题**



