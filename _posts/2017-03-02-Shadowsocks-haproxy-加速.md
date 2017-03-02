---
published: true
layout: post
title: Shadowsocks HAProxy 加速
---

安装 HAProxy:

`sudo apt-get install haproxy`

编辑配置文件 /etc/haproxy/haproxy.cfg

```
global
        ulimit-n  51200

defaults
        log global
        mode    tcp
        option  dontlognull
        contimeout 1000
        clitimeout 150000
        srvtimeout 150000

frontend ss-in
        bind *:8388
        default_backend ss-out

backend ss-out
        server server1 222.222.222.222:2222 maxconn 20480
```

启动服务：

`service haproxy restart`

或者

`haproxy -f /etc/haproxy/haproxy.cfg`

