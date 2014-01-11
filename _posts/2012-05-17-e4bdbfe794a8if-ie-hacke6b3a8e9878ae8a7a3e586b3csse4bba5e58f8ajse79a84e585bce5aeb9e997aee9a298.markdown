---
author: ths
comments: true
date: 2012-05-17 09:22:00+00:00
layout: post
slug: '%e4%bd%bf%e7%94%a8if-ie-hack%e6%b3%a8%e9%87%8a%e8%a7%a3%e5%86%b3css%e4%bb%a5%e5%8f%8ajs%e7%9a%84%e5%85%bc%e5%ae%b9%e9%97%ae%e9%a2%98'
title: 使用if IE hack注释解决CSS以及JS的兼容问题
wordpress_id: 756
categories:
- 技术
tags:
- 浏览器兼容
---





在IE CSS hack(更多方法)当中常用到if IE 来判断浏览器的类型，解决CSS甚至于JS的兼容性问题，之前大家可能知道if IE来解决CSS的兼容性问题，其实if IE不仅仅是用于CSS hack的使用，我们在前端开发中甚至可以使用if IE来做JS的处理，如下面的代码：




    
    <span class="kwrd"><!</span>–[if IE 5]<span class="kwrd">></span> <span class="kwrd"><</span><span class="html">script</span><span class="kwrd">></span>document.write(”仅IE5.0与IE5.5可以识别”);<span class="kwrd"></</span><span class="html">script</span><span class="kwrd">></span> <span class="kwrd"><!</span>[endif]–<span class="kwrd">></span>
    
    <span class="kwrd"><!</span>–[if gte IE 5.0]<span class="kwrd">><</span><span class="html">script</span><span class="kwrd">></span>document.write(”IE5.0以及IE5.0以上版本都可以识别”);<span class="kwrd"></</span><span class="html">script</span><span class="kwrd">><!</span>[endif]–<span class="kwrd">></span>
    
    <span class="kwrd"><!</span>–[if IE 6]<span class="kwrd">><</span><span class="html">script</span><span class="kwrd">></span>document.write(”仅IE6可识别”);<span class="kwrd"></</span><span class="html">script</span><span class="kwrd">><!</span>[endif]–<span class="kwrd">></span>
    
    <span class="kwrd"><!</span>–[if lt IE 6]<span class="kwrd">><</span><span class="html">script</span><span class="kwrd">></span>document.write(”IE6以下版本可识别”);<span class="kwrd"></</span><span class="html">script</span><span class="kwrd">><!</span>[endif]–<span class="kwrd">></span>
    
    <span class="kwrd"><!</span>–[if gte IE 6]<span class="kwrd">><</span><span class="html">script</span><span class="kwrd">></span>document.write(”IE6以及IE6以上版本可识别”);<span class="kwrd"></</span><span class="html">script</span><span class="kwrd">><!</span>[endif]–<span class="kwrd">></span>
    
    <span class="kwrd"><!</span>–[if IE 7]<span class="kwrd">><</span><span class="html">script</span><span class="kwrd">></span>document.write(”仅IE7可识别”);<span class="kwrd"></</span><span class="html">script</span><span class="kwrd">></span> <span class="kwrd"><!</span>[endif]–<span class="kwrd">></span>
    
    <span class="kwrd"><!</span>–[if lt IE 7]<span class="kwrd">><</span><span class="html">script</span><span class="kwrd">></span>document.write(”IE7以下版本可识别”);<span class="kwrd"></</span><span class="html">script</span><span class="kwrd">><!</span>[endif]–<span class="kwrd">></span>
    
    <span class="kwrd"><!</span>–[if gte IE 7]<span class="kwrd">><</span><span class="html">script</span><span class="kwrd">></span>document.write(”IE7以及IE7以上版本可识别”);<span class="kwrd"></</span><span class="html">script</span><span class="kwrd">><!</span>[endif]–<span class="kwrd">></span>
    






  
下面对if IE做一下详细的解释：





lte：就是Less than or equal to的简写，也就是小于或等于的意思。





lt ：就是Less than的简写，也就是小于的意思。





gte：就是Greater than or equal to的简写，也就是大于或等于的意思。





gt ：就是Greater than的简写，也就是大于的意思。





! ：就是不等于的意思，跟javascript里的不等于判断符相同





当然我们也可以使用if IE的注释来引入 js文件，以及CSS hack（更多方法）文件，如下面的代码：




    
    <span class="kwrd"><!</span>–[if lte IE 6]<span class="kwrd">></span>
    <span class="kwrd"><!</span>– 如果IE浏览器版本小于等于6,调用ie6.css样式表 –<span class="kwrd">></span>
    <span class="kwrd"><</span><span class="html">link</span> <span class="attr">rel</span>=”<span class="attr">stylesheet</span>” <span class="attr">type</span>=”<span class="attr">text</span>/<span class="attr">css</span>” <span class="attr">href</span>=“<span class="attr">http:</span>//<span class="attr">js8</span>.<span class="attr">in</span>/<span class="attr">ie6</span>.<span class="attr">css</span>” <span class="kwrd">/></span>
    <span class="kwrd"><!</span>[endif]–<span class="kwrd">></span>
    
    <span class="kwrd"><!</span>–[if lte IE 6]<span class="kwrd">></span>
    <span class="kwrd"><!</span>– 如果IE浏览器版本小于等于6,调用ie6.js样式表 –<span class="kwrd">></span>
    <span class="kwrd"><</span><span class="html">script</span> <span class="attr">type</span>=”<span class="attr">text</span>/<span class="attr">javascript</span>” <span class="attr">src</span>=”<span class="attr">http:</span>//<span class="attr">js8</span>.<span class="attr">in</span>/<span class="attr">ie6</span>.<span class="attr">js</span>“<span class="kwrd">></</span><span class="html">script</span><span class="kwrd">></span>
    <span class="kwrd"><!</span>[endif]–<span class="kwrd">></span>
    






  
最后，其实if IE的判断是可以镶嵌来写的，如下面的代码，采用了多级的判断：




    
    <span class="kwrd"><!</span>–[if IE]<span class="kwrd">></span>
    <span class="kwrd"><</span><span class="html">h1</span><span class="kwrd">></span>您正在使用IE浏览器<span class="kwrd"></</span><span class="html">h1</span><span class="kwrd">></span>
    <span class="kwrd"><!</span>–[if IE 5]<span class="kwrd">></span>
    <span class="kwrd"><</span><span class="html">h2</span><span class="kwrd">></span>版本 5<span class="kwrd"></</span><span class="html">h2</span><span class="kwrd">></span>
    <span class="kwrd"><!</span>[endif]–<span class="kwrd">></span>
    
    <span class="kwrd"><!</span>–[if IE 5.0]<span class="kwrd">></span>
    <span class="kwrd"><</span><span class="html">h2</span><span class="kwrd">></span>版本 5.0<span class="kwrd"></</span><span class="html">h2</span><span class="kwrd">></span>
    <span class="kwrd"><!</span>[endif]–<span class="kwrd">></span>
    
    <span class="kwrd"><!</span>–[if IE 5.5]<span class="kwrd">></span>
    <span class="kwrd"><</span><span class="html">h2</span><span class="kwrd">></span>版本 5.5<span class="kwrd"></</span><span class="html">h2</span><span class="kwrd">></span>
    <span class="kwrd"><!</span>[endif]–<span class="kwrd">></span>
    
    <span class="kwrd"><!</span>–[if IE 6]<span class="kwrd">></span>
    <span class="kwrd"><</span><span class="html">h2</span><span class="kwrd">></span>版本 6<span class="kwrd"></</span><span class="html">h2</span><span class="kwrd">></span>
    <span class="kwrd"><!</span>[endif]–<span class="kwrd">></span>
    
    <span class="kwrd"><!</span>–[if IE 7]<span class="kwrd">></span>
    <span class="kwrd"><</span><span class="html">h2</span><span class="kwrd">></span>版本 7<span class="kwrd"></</span><span class="html">h2</span><span class="kwrd">></span>
    <span class="kwrd"><!</span>[endif]–<span class="kwrd">></span>
    <span class="kwrd"><!</span>[endif]–<span class="kwrd">></span>
    
    



更多的CSS Hack方法，请继续阅读[《主流浏览器的CSS Hack方法整理》](http://js8.in/382.html)



