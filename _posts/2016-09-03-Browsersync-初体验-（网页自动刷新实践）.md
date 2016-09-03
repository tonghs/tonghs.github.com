---
published: true
layout: post
---
官网：[https://www.browsersync.io/](https://www.browsersync.io/)
中文网站（非官方）：[http://www.browsersync.cn/](http://www.browsersync.cn/)

页面开发自动刷新已经不是什么新鲜事情了，作为 Web 开发者，在调试/测试页面时不停的切换刷新是一件非常费时的事情，好在有比我们更懒的人做出了好用的工具，省时省力的工具，还是要学一下的。

[Browsersync](https://www.browsersync.io/)，官方介绍：Time-saving synchronised browser testing。

![](http://www.browsersync.cn/img/sync-demo.gif) 

![](http://www.browsersync.cn/img/scroll-demo.gif)

简单来说，Browsersync 可以让浏览器实时、快速响应您的文件更改（html、js、css、sass、less等）并自动刷新页面，可以同时在PC、平板、手机等设备下进项调试。有了它，您不用在多个浏览器、多个设备间来回切换，频繁的刷新页面。更神奇的是您在一个浏览器中滚动页面、点击等行为也会同步到其他浏览器和设备中，这一切还可以通过可视化界面来控制。

下面介绍个简单的例子：

## 安装

1. 安装 Node.js，参见 [http://nodejs.org/download/](http://nodejs.org/download/)
2. 安装 BrowserSync
```
npm install -g browser-sync
```

## 使用

BrowserSync 分两种使用场景，一种是静态网站（较少），另外一种是动态网站（较多）

1. 静态网站（[示例代码](http://www.browsersync.cn/example/packages/BrowsersyncExample.zip))

假设网站中只有 html、CSS 和 JavaScript。

```
cd YOUR-SITE-DIR
browser-sync start --server --files "css/*.css, js/**/*.js, *.html"
```

启动 log：

```
[BS] Access URLs:
 --------------------------------------
       Local: http://localhost:3002
    External: http://10.173.12.189:3002
 --------------------------------------
          UI: http://localhost:3003
 UI External: http://10.173.12.189:3003
 --------------------------------------
[BS] Serving files from: ./
[BS] Watching files...
```

此时，BrowserSync 会启动一个 server（Serving files from: ./），并开始监听 --files 参数中制定的文件的变动。访问 http://localhost:3002 即可看到效果。

2. 动态网站

这也是最常见的使用场景，一般大家都已经或者将要使用一门动态语言（PHP，Python，Java）搭建网站，此时的使用略有不同，就要用到 BrowserSync 的 proxy 模式。

首先假设你的网站的域名（也可以是 IP）是：http://a.com 。

```
browser-sync start --proxy "a.com" --files "css/*.css, js/**/*.js, template/**/*.html"
```

启动 log：

```
[BS] Proxying: http://a.com
[BS] Access URLs:
 --------------------------------------
       Local: http://localhost:3002
    External: http://10.173.12.189:3002
 --------------------------------------
          UI: http://localhost:3003
 UI External: http://10.173.12.189:3003
 --------------------------------------
[BS] Watching files...
```

此时看到第一行：Proxying: http://a.com 代表 BrowserSync 已经建立了到 baidu.com 的代理，并开始监听 a.com 下的的文件（css/*.css, js/**/*.js, template/**/*.html）。

注意，此时要访问 http://localhost:3002 ，此时所有的请求需要由 BrwserSync 作为请求代理到真实的 a.com。

enjoy it。


