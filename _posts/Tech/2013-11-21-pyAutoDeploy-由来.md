---
layout: post
title: pyAutoDeploy 由来
---
不折腾就会死。

由于经费问题，自己的 `VPS` 内存一直没有升级，256 内存玩玩勉强够用，最近折腾了几个 `Python` 的站，发现每次 `git push` 后 `ssh` 到 `VPS` 上去 `git pull` 真的是十分麻烦，于是开始折腾持续集成工具，一路选下来，最终选择了 `Jenkins`，折腾过程请移步另一篇博文：[Python 持续集成方案][1]。

本以为可以高枕无忧了，结果在某一天看 `VPS` 系统占用时，发现内存占用 100%，着实汗了一把，第一想到的就是 `Jenkins`，`Java` 的东西吃内存大户啊，想来想去没有好的办法，于是本着`自己动手，丰衣足食`的精神决定自己用 `Python` 写一个，彻底和 `Java` 撇清关系，于是就有了这个工具。

pyAutoDeploy，基于 `Python` `web.py`，在各位大牛看来可能是 piece of shit，但是目前确实解决了我的问题。

GitHub 地址：<https://github.com/tonghuashuai/pyAutoDeploy>，欢迎大家拍砖

 [1]: http://www.tonghs.com/?p=1293