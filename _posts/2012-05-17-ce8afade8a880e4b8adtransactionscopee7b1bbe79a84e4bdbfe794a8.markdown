---
author: ths
comments: true
date: 2012-05-17 09:12:00+00:00
layout: post
slug: c%e8%af%ad%e8%a8%80%e4%b8%adtransactionscope%e7%b1%bb%e7%9a%84%e4%bd%bf%e7%94%a8
title: C#语言中TransactionScope类的使用
wordpress_id: 752
categories:
- 技术
tags:
- c
- TransactionScope
---

如果在C#中使用TransactionScope类(分布式事务),则须注意如下事项:  
1、在项目中引用using System.Transactions命名空间（先要在添加net组件的引用）; 





2、具体示例如下： 
    
    <span style="color: #808080">/// <summary></span>
    <span style="color: #808080">/// 发送消息</span>
     <span style="color: #808080">/// </summary></span>
    <span style="color: #808080">/// <param name="sendUserId"></param></span>
    <span style="color: #808080">/// <param name="toUser">格式7FFA3AF2-E74B-4174-8403-5010C53E49A7|userName,7FFA3AF2-E74B-4174-8403-5010C53E49A7|userName</param></span>
    <span style="color: #808080">/// <param name="content"></param></span>
    <span style="color: #808080">/// <param name="sendedStatus">表示已送</param></span>
    <span style="color: #808080">/// <returns></returns></span>
    <span style="color: #0000ff">public</span> <span style="color: #0000ff">static</span> <span style="color: #0000ff">int</span> sendMessage(<span style="color: #0000ff">string</span> sendUserId, <span style="color: #0000ff">string</span> toUser, <span style="color: #0000ff">string</span> content, <span style="color: #0000ff">string</span> sendedStatus)
    {           
        <span style="color: #0000ff">int</span> receiveCount = 0;
        TransactionOptions transactionOption = <span style="color: #0000ff">new</span> TransactionOptions();
    
        <span style="color: #008000">//设置事务隔离级别</span>
        transactionOption.IsolationLevel = System.Transactions.IsolationLevel.ReadCommitted;
    
        <span style="color: #008000">// 设置事务超时时间为60秒</span>
        transactionOption.Timeout = <span style="color: #0000ff">new</span> TimeSpan(0, 0, 60);
    
        <span style="color: #0000ff">using</span> (TransactionScope scope = <span style="color: #0000ff">new</span> TransactionScope(TransactionScopeOption.Required, transactionOption))
        {
        <span style="color: #0000ff">try</span>
        {
            <span style="color: #008000">//在这里实现事务性工作</span>
    <span style="color: #008000">//发送消息</span>
            insertMessage(sendUserId, toUser, content, sendedStatus);
    
    <span style="color: #008000">//在接收信息表中插入记录</span>
            receiveCount += insertReceiveMessage(userids[0], sendUserId, content, "<span style="color: #8b0000">0</span>");
           
            <span style="color: #008000">// 没有错误,提交事务</span>
            scope.Complete();
        }
        <span style="color: #0000ff">catch</span> (Exception ex) {
            <span style="color: #0000ff">throw</span> <span style="color: #0000ff">new</span> Exception("<span style="color: #8b0000">发送信息异常,原因:</span>"+ex.Message);
        }<span style="color: #0000ff">finally</span>{
            <span style="color: #008000">//释放资源</span>
            scope.Dispose();
          }                               
        }
        <span style="color: #0000ff">return</span> receiveCount;
    }

  






3、对MSDTC组件设置:  
步骤:  
在控制面板--->管理工具--->服务 中，开启Distributed Transaction Coordinator 服务。  
a.控制面板->管理工具->组件服务->计算机->我的电脑->右键->属性  
b.选择MSDTC页, 确认"使用本地协调器"  
c.点击下方"安全配置"按钮  
d.勾选: "允许网络DTC访问","允许远程客户端","允许入站","允许出站","不要求进行身份验证".  
e.对于数据库服务器端, 可选择"要求对呼叫方验证"  
f.勾选:"启用事务Internet协议（TIP)事务"。  
g.在双方防火墙中增加MSDTC.exe例外  
可用命令行: netsh firewall set allowedprogram %windir%system32msdtc.exe MSDTC enable





4、重启IIS服务器。



