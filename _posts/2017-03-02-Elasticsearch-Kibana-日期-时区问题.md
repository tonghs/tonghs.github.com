---
published: true
layout: post
title: Elasticsearch Kibana 日期 时区问题
---

写入到 ElasticSearch 中的日期在 Kibana 中显示差 8 个小时，在 Kibana 中高级设置中可以往前设置 8 个时区，但是数据还是会出错。

最终解决办法，是在向 ElasticSearch 写数据的时候就带上时区信息。

需要安装 pytz

``` shell
$ pip install pytz
```

``` python
import pytz

tz = pytz.timezone('Asia/Shanghai')
datetime.datetime.now().replace(tzinfo=tz)
```
