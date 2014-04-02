---
layout: post
title: GAE中 urlfetch CRC 错误
---
在使用 urlfetch.fetch(url) 时遇到 CRC 错误

	IOError: CRC check failed

看详细错误信息跟 gzip 有关，网上查了下得到如下总结：

urlfetch 抓下来的额网页是 gzip 压缩的，解码过程中报错，原因可能是 gzip 压缩不标准导致解析错误，网友给了绕过这个问题的方法，伪装 header，伪装一个Accept-Encoding，假装不懂gzip。于是对方服务器就把没有经过压缩的网页发过来了：

查 gae 的 API 发现 fetch 方法有 headers 参数，看官方示例

	import urllib
	
	from google.appengine.api import urlfetch
	
	form_fields = {
	  "first_name": "Albert",
	  "last_name": "Johnson",
	  "email_address": "Albert.Johnson@example.com"
	}
	form_data = urllib.urlencode(form_fields)
	result = urlfetch.fetch(url=url,
	    payload=form_data,
	    method=urlfetch.POST,
	    headers={'Content-Type': 'application/x-www-form-urlencoded'})
	    
	    
于是我的代码改为：

	urlfetch.fetch(url, headers={Accept-Encoding': ''})