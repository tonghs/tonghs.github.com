---
author: ths
comments: true
date: 2010-01-22 00:50:00+00:00
layout: post
slug: '%e8%ae%a9ewebeditor%e5%85%bc%e5%ae%b9ie8'
title: 让eWebEditor兼容IE8
wordpress_id: 74
categories:
- 技术
tags:
- ewebeditor
- it
- 兼容ie8
---

  也在今天公司的一个同事装了windows7
，在管理网站时发现后台的在线编辑的按钮失效，只有少数几个能用，以前他用的xp系统没问题，我首先想到的是eWebEditor和IE8的兼容问题，网站是我开发的，但是ewebeditor不是我弄的，只能google了，google了一下，猜想得到验证，确实是兼容性的问题，有很多人都遇到了这个问题，解决方法也不难，下面是我看的一篇解决方法的文章的片段：





   
**是因为ie8屏蔽了anonymous方法所以要改成onclick方法，打开include下面的editor.js文件，有这样的段代码：**






**    
if (element.YUSERONCLICK) (element.YUSERONCLICK +
"anonymous()");**





**把那个anonymous方法改成onclick就可以了。**






**   
问题是解决了，心情也舒畅了，结果没过两个小时我的会员就像我反应页面出问题，我换到别人的电脑上一看，这叫一个汗，原来把那个方法改成onclick之后在ie7下面就不管用了，毕竟现在很多人用的还是ie7，这叫一个头疼，于是还是去网上找，总是感觉不可能是我一个人遇到这样的问题。**






**    
最后果然还是在csdn上找到了答案：**





**if(navigator.appVersion.match(/8./i)=='8.')  

   
{  

     
if (element.YUSERONCLICK) (element.YUSERONCLICK +
"onclick(event)");    


   }  

else**





**  
{  

    
if (element.YUSERONCLICK) (element.YUSERONCLICK +
"anonymous()");  

}**






**   
用这样一段代码，对浏览器的版本做一个判断就好了，但是我却不知道在ie6下面管不管用，毕竟现在用ie6的人少了，一时我也不知道去哪测试。**





**  **
上面提到的IE6的问题我也测试了下，没什么问题，问题解决。



