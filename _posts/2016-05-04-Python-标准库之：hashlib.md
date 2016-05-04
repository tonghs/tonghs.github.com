---
published: true
layout: post
tags: []
---
该库提供的加密方法有：

* md5
* sha1
* sha224
* sha256
* sha384
* sha512

官方提供的使用示例如下：

``` python
import hashlib
m = hashlib.md5()
m.update("Nobody inspects")
m.update(" the spammish repetition")
m.digest()
m.hexdigest()
```

其他使用方法类似。

下面介绍集中常用的加密算法：

* md5

一种广泛使用的密码加密方法，该算法会生成一个 128位（32位 16进制）的 hash 值，也就是说经过 md5 加密后，生成的结果是固定长度的，所以可以用于校验文件完整性，另外常见的场景就是密码加密。

该算法不可逆，通常破解方式为暴力破解。

* sha

sha（全称为 Secure Hash Algorithm）家族包括一系列的算法，包括是 sha-1、sha-224、sha-256、sha-384，和 sha-512，该系列算法同样能计算出一个长度固定的字串，其中 sha-1、sha-224、sha-256 可适用于长度不超过2^64的二进制位的消息，sha-384 和 sha-512 适用于长度不超过2^128二进制位的消息。

sha 算法家族哈希值大小及输出长度

sha-1 算法的哈希值大小为160位，其计算输出长度为40位。
sha-224 算法的哈希值大小为224位，其计算输出长度为56位。
sha-256 算法的哈希值大小为256位，其计算输出长度为64位。
sha-384 算法的哈希值大小为384位，其计算输出长度为96位。
sha-512 算法的哈希值大小为384位，其计算输出长度为128位。
