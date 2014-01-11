---
author: ths
comments: true
date: 2013-11-23 16:19:07+00:00
layout: post
slug: '%e5%85%b3%e4%ba%8e-onlyrss-%e9%a1%b5%e9%9d%a2%e5%8a%a0%e8%bd%bd%e9%80%9f%e5%ba%a6%e7%9a%84%e4%bc%98%e5%8c%96%ef%bc%88%e5%a4%9a%e5%9b%be%e7%89%87%e5%8f%8a%e5%a4%9a-dom%ef%bc%89'
title: 关于 OnlyRSS 页面加载速度的优化（多图片及多 DOM）
wordpress_id: 1678
categories:
- OnlyRSSWeb
- 技术
tags:
- DOM
- img
- 延迟加载
---

其实使用 `OnlyRSS` 已经用了有一段时间了，在这期间偶尔会出现加载比较慢的问题，有时候一页内容要加载 10s 左右，在一般宽带环境下也一样，我断定应该不是网络问题。





但是一直找不到问题根源，但是还是一直在用，后来慢慢发现跟我订阅的一个网站有关--[`数字尾巴`](http://www.dgtle.com/)（注：是一个非常不错的分享社区，风格养眼，文章质量也很不错），只要当前页中包含`数字尾巴`的内容，就能感觉到速度慢，如果一页中包含多篇文章，那就出现了我说的问题--加载时间大于 5s。





后来我想了下，应该是跟图片相关，因为`数字尾巴`分享的文章有很多高质量的图片，占文章的很大比例，如下图，（为了显示方便，我已经将图隐掉，只留下名称）：





![图片](http://ww2.sinaimg.cn/bmiddle/e94cbcecjw1eavdlkl47qj20gj0o577m.jpg)





所以我就想到了是这些精美图片影响了加载速度。为了验证，我就当都点开了`数字尾巴`的订阅，只显示这个网站的内容，发现果然如我所想。





问题找到了，就该着手去解决了。





我大概的文章显示是这样的流程：先把文章内容从数据库中查出，然后转为 json response 到浏览器端，然后浏览器解析 json 后动态添加到页面展示。以显示 20 篇`数字尾巴`的文章，每篇文章 10 张图片为例，我单独获取这些内容的 json，纯 json 也就 300k 左右，如果是加载纯文字，300k 应该没有什么问题，但是要加载 200 多张图片却要耗费大量时间。





于是我就想，应该先让文字内容显示出来，图片只占位，等文字加载完成然后再加载图片。但是怎么实现呢？网上貌似有 jquery 的库，用起来还算方便，但是后来我想了下，自己用其他方式实现也不难，下面是思路：





我们知道，图片要显示设置读取 `<img>` 标签中的 `src` 属性，根据 `src` 属性的 `url` 获取图片路径加载。所以，我想我不给 `src` 赋值就行了，`<img>` 标签没有 `src` 属性，就只显示 `title` 属性中的文本，这样就能实现文字内容加载，并且完成 `<img>` 占位。那么文字加载完后加载图片时去哪读取 `url` 呢？我用的方法是，给  标签一个属性加：src_no，`value` 就是图片的 `url`，这样，加载图片是只需要读取 src_no 的值，然后赋给 `src` 即可。下面是代码修改（`Python`）：





原代码：




    
    <code>items_json = json.dumps(list_temp)
    </code>





现改为：




    
    <code>items_json = json.dumps(list_temp).replace('src', 'src_no')
    </code>





这样，原本 `<img src='http://xxxx' title='xxx'/>` 就被替换为 `<img src_no='http://xxxx' title='xxx'/>`。





然后前台 js 中定义如下函数，在文本加载完毕后调用即可：




    
    <code>function showImg(){
        $('img').each(function(){
            $(this).attr('src', $(this).attr('src_no'));
            $(this).removeAttr('src_no');
        });
    }
    </code>





至此，解决图片多导致加载慢问题。





怀着激动的心情，把页面放到 `YSlow` 中跑了以下，得分基本都是 A，然后往下看突然出现了一个 F，如下图：





![YSlow](http://ww4.sinaimg.cn/bmiddle/e94cbcecjw1eaveewz9ubj207v0c13zm.jpg)





详细信息为：





> 
  
> 
> Grade F on Reduce the number of DOM elements
> 
> 
  
  
> 
> There are 2552 DOM elements on the page
> 
> 






天啊，2552 个 DOM，DOM 数影响加载了。于是再回页面，查看 `html` 代码如下：





![html 代码](http://ww1.sinaimg.cn/bmiddle/e94cbcecjw1eaveib3783j20av0dmgob.jpg)





这只是一片文章的一个片段，居然出现了这么多 `div`,后来我发现基本上是一行一个 `div`，甚至 `<br>` 都用一个 `div` 来包含。用 `div` 来实现换行？太有创意了吧。





我以为是我的程序中解析错误，后来想了下不应该，于是直奔`数字尾巴`网站，打开一篇文章，查看 `html` 代码，发现跟我刚才看到的一样。原来原网站就是这样，这让我觉得减少自己页面中的 DOM 数是非常必要的了，准备下一步优化。不过`数字尾巴`那边我就无能为力了...希望`数字尾巴`的开发者能看到这篇文章吧。



