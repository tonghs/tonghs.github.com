---
published: true
layout: post
title: 阿里云 MongoDB Primary 和 Secondary 节点变化的问题
---

![](https://ww3.sinaimg.cn/large/006tNc79gy1fd8a7glvpvj30ea08xdfr.jpg)

在阿里云的 MongoDB 控制台示例关系处，有一句提示：Primary、Secondary节点不固定，可能发生变化，客户端请使用Connection String URI连接来保证高可用。

也就是说，阿里云提供了两个节点，一个副本集，而且在使用过程中这两个节点 谁是 Primary，谁是 Secondary 是变化的，不确定的，所以使用的时候不能只连接一个节点，如果发生变化，连接的节点变为 Secondary，就会报 AutoReconnect: not master and slaveOk=false 的错误。阿里云给出的正确的连接方式是：
 
```
客户端使用Connection String URI连接实例 （****部分替换为为root密码）
请使用MongoDB 3.0以上版本的driver
mongodb://root:****@dds-bp1156dc1fedf0b41.mongodb.rds.aliyuncs.com:3717,dds-bp1156dc1fedf0b42.mongodb.rds.aliyuncs.com:3717/admin?replicaSet=mgset-1036203
```
