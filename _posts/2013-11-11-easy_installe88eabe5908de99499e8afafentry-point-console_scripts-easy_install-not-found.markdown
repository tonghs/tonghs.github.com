---
author: ths
comments: true
date: 2013-11-11 11:53:46+00:00
layout: post
slug: easy_install%e8%8e%ab%e5%90%8d%e9%94%99%e8%af%afentry-point-console_scripts-easy_install-not-found
title: easy_install莫名错误:Entry point ('console_scripts', 'easy_install') not found`
wordpress_id: 1254
categories:
- 技术
tags:
- easy_install
---

最近在vps中用easy_install安装包时收到以下错误：




    
    <code>/usr/bin/easy_install-2.6:7: UserWarning: Module pkg_resources was already imported from /System/Library/Frameworks/Python.framework/Versions/2.6/Extras/lib/python/pkg_resources.pyc, but /Library/Python/2.6/site-packages is being added to sys.path
      from pkg_resources import load_entry_point
    /usr/bin/easy_install-2.6:7: UserWarning: Module site was already imported from /System/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/site.pyc, but /Library/Python/2.6/site-packages is being added to sys.path
      from pkg_resources import load_entry_point
    Traceback (most recent call last):
      File "/usr/bin/easy_install-2.6", line 10, in <module>
        load_entry_point('setuptools==0.6c9', 'console_scripts', 'easy_install')()
      File "/System/Library/Frameworks/Python.framework/Versions/2.6/Extras/lib/python/pkg_resources.py", line 271, in load_entry_point
        return False
      File "/System/Library/Frameworks/Python.framework/Versions/2.6/Extras/lib/python/pkg_resources.py", line 2173, in load_entry_point
        deps = []
    ImportError: Entry point ('console_scripts', 'easy_install') not found
    </code>





google许久原因不详，重装easy_install后就好了。
还请大牛解答。



