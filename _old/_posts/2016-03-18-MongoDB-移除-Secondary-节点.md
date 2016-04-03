---
layout: post
title: MongoDB 移除 Secondary 节点
tagline: null
category: null
tags: []
published: true

---

在不知道节点信息的情况下要移除某个 secondary 节点。

首先要连接到住节点，然后查看主从状态：

```

host_name:PRIMARY> rs.status()

{
        "set" : "4caa650b-2780-41c2-98cd-547b01f8c49a",
        "date" : ISODate("2016-03-18T04:00:31Z"),
        "myState" : 1,
        "members" : [
                {
                        "_id" : 0,
                        "name" : "10.9.9.100:27017",
                        "health" : 1,
                        "state" : 2,
                        "stateStr" : "SECONDARY",
                        "uptime" : 455,
                        "optime" : Timestamp(1458273610, 2),
                        "optimeDate" : ISODate("2016-03-18T04:00:10Z"),
                        "lastHeartbeat" : ISODate("2016-03-18T04:00:31Z"),
                        "lastHeartbeatRecv" : ISODate("2016-03-18T04:00:30Z"),
                        "pingMs" : 1,
                        "syncingTo" : "10.10.9.52:27017"
                },
                {
                        "_id" : 1,
                        "name" : "10.10.9.52:27017",
                        "health" : 1,
                        "state" : 1,
                        "stateStr" : "PRIMARY",
                        "uptime" : 8560211,
                        "optime" : Timestamp(1458273610, 2),
                        "optimeDate" : ISODate("2016-03-18T04:00:10Z"),
                        "electionTime" : Timestamp(1458273183, 1),
                        "electionDate" : ISODate("2016-03-18T03:53:03Z"),
                        "self" : true
                }
        ],
        "ok" : 1
}
```

得知 Secondary 节点的 IP 和端口，即 10.9.9.100:27017，然后确定当前执行命令的节点是否是 Primary 节点：

```

host_name:PRIMARY>  db.isMaster()
{
        "setName" : "4caa650b-2780-41c2-98cd-547b01f8c49a",
        "setVersion" : 148197,
        "ismaster" : true,  # 表示是 primary 节点
        "secondary" : false,
        "hosts" : [
                "10.10.9.52:27017",
                "10.9.9.100:27017"
        ],
        "primary" : "10.10.9.52:27017",
        "me" : "10.10.9.52:27017",
        "maxBsonObjectSize" : 16777216,
        "maxMessageSizeBytes" : 48000000,
        "maxWriteBatchSize" : 1000,
        "localTime" : ISODate("2016-03-18T04:01:45.969Z"),
        "maxWireVersion" : 2,
        "minWireVersion" : 0,
        "ok" : 1
}
```

移除节点：

```

host_name:PRIMARY>  rs.remove("10.9.9.100:27017")
```

再次查看状态：

```

host_name:PRIMARY> rs.status()
{
        "set" : "4caa650b-2780-41c2-98cd-547b01f8c49a",
        "date" : ISODate("2016-03-18T04:06:37Z"),
        "myState" : 1,
        "members" : [
                {
                        "_id" : 1,
                        "name" : "10.10.9.52:27017",
                        "health" : 1,
                        "state" : 1,
                        "stateStr" : "PRIMARY",
                        "uptime" : 8560577,
                        "optime" : Timestamp(1458273988, 1),
                        "optimeDate" : ISODate("2016-03-18T04:06:28Z"),
                        "electionTime" : Timestamp(1458273183, 1),
                        "electionDate" : ISODate("2016-03-18T03:53:03Z"),
                        "self" : true
                }
        ],
        "ok" : 1
}
```

Secondary 结点已经移除。