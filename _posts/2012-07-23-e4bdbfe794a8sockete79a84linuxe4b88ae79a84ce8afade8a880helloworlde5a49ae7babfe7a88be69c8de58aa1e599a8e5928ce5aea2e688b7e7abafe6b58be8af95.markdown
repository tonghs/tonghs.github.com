---
author: ths
comments: true
date: 2012-07-23 12:15:00+00:00
layout: post
slug: '%e4%bd%bf%e7%94%a8socket%e7%9a%84linux%e4%b8%8a%e7%9a%84c%e8%af%ad%e8%a8%80helloworld%e5%a4%9a%e7%ba%bf%e7%a8%8b%e6%9c%8d%e5%8a%a1%e5%99%a8%e5%92%8c%e5%ae%a2%e6%88%b7%e7%ab%af%e6%b5%8b%e8%af%95'
title: 使用socket的Linux上的C语言helloworld多线程服务器和客户端测试程序
wordpress_id: 839
categories:
- 技术
tags:
- c
- linux
- socket
---

///////////////////////////////////////////////////////////////////////////////////  
服务器端程序的编译  
gcc -o multi_thread_server multi_thread_server -lpthread  
客户端程序的编译  
gcc -o multi_thread_client multi_thread_client.c -lpthread  
服务器程序和客户端程应当分别运行在2台计算机上.  
服务器端程序的运行,在一个计算机的终端执行  
./multi_thread_server  
客户端程序的运行,在另一个计算机的终端中执行  
./multi_thread_client 运行服务器程序的计算机的IP地址  
在实际编程和测试中,可以用2个终端代替2个计算机,这样就可以在一台计算机上测试网络程序,  
服务器端程序的运行,在一个终端执行  
./multi_thread_server  
客户端程序的运行,在另一个终端中执行  
./multi_thread_client 127.0.0.1  
说明: 任何计算机都可以通过127.0.0.1访问自己. 也可以用计算机的实际IP地址代替127.0.0.1
    
    <span class="rem">///////////////////////////////////////////////////////////////////////////////////</span>
    <span class="rem">//multi_thread_server.c</span>
    <span class="rem">///////////////////////////////////////////////////////////////////////////////////</span>
    <span class="rem">//本文件是多线程并发服务器的代码</span>
    #include <netinet/<span class="kwrd">in</span>.h>    <span class="rem">// for sockaddr_in</span>
    #include <sys/types.h>    <span class="rem">// for socket</span>
    #include <sys/socket.h>    <span class="rem">// for socket</span>
    #include <stdio.h>        <span class="rem">// for printf</span>
    #include <stdlib.h>        <span class="rem">// for exit</span>
    #include <<span class="kwrd">string</span>.h>        <span class="rem">// for bzero</span>
    #include <pthread.h>
    #include <sys/errno.h>    <span class="rem">// for errno</span>
    
    <span class="preproc">#define</span> HELLO_WORLD_SERVER_PORT    6666 
    <span class="preproc">#define</span> LENGTH_OF_LISTEN_QUEUE  20
    <span class="preproc">#define</span> BUFFER_SIZE 1024
    <span class="preproc">#define</span> THREAD_MAX    5
    <span class="kwrd">void</span> * talk_to_client(<span class="kwrd">void</span> *data)
    {
        <span class="kwrd">int</span> new_server_socket = (<span class="kwrd">int</span>)data;
        <span class="kwrd">char</span> buffer[BUFFER_SIZE];
        bzero(buffer, BUFFER_SIZE);
        strcpy(buffer,<span class="str">"Hello,World! 从服务器来！"</span>);
        strcat(buffer,<span class="str">"/n"</span>); <span class="rem">//C语言字符串连接</span>
        <span class="rem">//发送buffer中的字符串到new_server_socket,实际是给客户端</span>
        send(new_server_socket,buffer,BUFFER_SIZE,0);
    
        bzero(buffer,BUFFER_SIZE);
        <span class="rem">//接收客户端发送来的信息到buffer中</span>
        <span class="kwrd">int</span> length = recv(new_server_socket,buffer,BUFFER_SIZE,0);
        <span class="kwrd">if</span> (length < 0)
        {
            printf(<span class="str">"Server Recieve Data Failed!/n"</span>);
            exit(1);
        }
        printf(<span class="str">"/nSocket Num: %d /t %s"</span>,new_server_socket, buffer);
        <span class="rem">//关闭与客户端的连接</span>
        close(new_server_socket); 
        pthread_exit(NULL);
    }
    <span class="kwrd">int</span> main(<span class="kwrd">int</span> argc, <span class="kwrd">char</span> **argv)
    {
        <span class="rem">//设置一个socket地址结构server_addr,代表服务器internet地址, 端口</span>
        <span class="kwrd">struct</span> sockaddr_in server_addr;
        bzero(&server_addr,<span class="kwrd">sizeof</span>(server_addr)); <span class="rem">//把一段内存区的内容全部设置为0</span>
        server_addr.sin_family = AF_INET;
        server_addr.sin_addr.s_addr = htons(INADDR_ANY);
        server_addr.sin_port = htons(HELLO_WORLD_SERVER_PORT);
    
        <span class="rem">//创建用于internet的流协议(TCP)socket,用server_socket代表服务器socket</span>
        <span class="kwrd">int</span> server_socket = socket(AF_INET,SOCK_STREAM,0);
        <span class="kwrd">if</span>( server_socket < 0)
        {
            printf(<span class="str">"Create Socket Failed!"</span>);
            exit(1);
        }
        
        <span class="rem">//把socket和socket地址结构联系起来</span>
        <span class="kwrd">if</span>( bind(server_socket,(<span class="kwrd">struct</span> sockaddr*)&server_addr,<span class="kwrd">sizeof</span>(server_addr)))
        {
            printf(<span class="str">"Server Bind Port : %d Failed!"</span>, HELLO_WORLD_SERVER_PORT); 
            exit(1);
        }
        
        <span class="rem">//server_socket用于监听</span>
        <span class="kwrd">if</span> ( listen(server_socket, LENGTH_OF_LISTEN_QUEUE) )
        {
            printf(<span class="str">"Server Listen Failed!"</span>); 
            exit(1);
        }
        
        
        <span class="kwrd">int</span> i;
        <span class="kwrd">while</span>(1) <span class="rem">//服务器端要一直运行</span>
        {
    
            <span class="rem">//定义客户端的socket地址结构client_addr</span>
            <span class="kwrd">struct</span> sockaddr_in client_addr;
            socklen_t length = <span class="kwrd">sizeof</span>(client_addr);
    
            <span class="rem">//接受一个到server_socket代表的socket的一个连接</span>
            <span class="rem">//如果没有连接请求,就等待到有连接请求--这是accept函数的特性</span>
            <span class="rem">//accept函数返回一个新的socket,这个socket(new_server_socket)用于同连接到的客户的通信</span>
            <span class="rem">//new_server_socket代表了服务器和客户端之间的一个通信通道</span>
            <span class="rem">//accept函数把连接到的客户端信息填写到客户端的socket地址结构client_addr中</span>
            <span class="kwrd">int</span> new_server_socket = accept(server_socket,(<span class="kwrd">struct</span> sockaddr*)&client_addr,&length);
            <span class="kwrd">if</span> ( new_server_socket < 0)
            {
                printf(<span class="str">"Server Accept Failed!/n"</span>);
                <span class="kwrd">break</span>;
            }
            pthread_t child_thread;
            pthread_attr_t child_thread_attr;
            pthread_attr_init(&child_thread_attr);
            pthread_attr_setdetachstate(&child_thread_attr,PTHREAD_CREATE_DETACHED);
            <span class="kwrd">if</span>( pthread_create(&child_thread,&child_thread_attr,talk_to_client, (<span class="kwrd">void</span> *)new_server_socket) < 0 )
                printf(<span class="str">"pthread_create Failed : %s/n"</span>,strerror(errno));
        }
        <span class="rem">//关闭监听用的socket</span>
        close(server_socket);
        <span class="kwrd">return</span> 0;
    }
    <span class="rem">///////////////////////////////////////////////////////////////////////////////////</span>
    <span class="rem">// multi_thread_client.c </span>
    <span class="rem">///////////////////////////////////////////////////////////////////////////////////</span>
    <span class="rem">//本文件是客户机多线程多次重复与服务交互的代码</span>
    #include <netinet/<span class="kwrd">in</span>.h>    <span class="rem">// for sockaddr_in</span>
    #include <sys/types.h>    <span class="rem">// for socket</span>
    #include <sys/socket.h>    <span class="rem">// for socket</span>
    #include <stdio.h>        <span class="rem">// for printf</span>
    #include <stdlib.h>        <span class="rem">// for exit</span>
    #include <<span class="kwrd">string</span>.h>        <span class="rem">// for bzero</span>
    #include <pthread.h>
    #include <sys/errno.h>    <span class="rem">// for errno</span>
    
    <span class="preproc">#define</span> HELLO_WORLD_SERVER_PORT    6666 
    <span class="preproc">#define</span> BUFFER_SIZE 1024
    
    <span class="kwrd">char</span> * server_IP = NULL;
    
    <span class="kwrd">void</span> * talk_to_server(<span class="kwrd">void</span> * thread_num)
    {
        <span class="rem">//设置一个socket地址结构client_addr,代表客户机internet地址, 端口</span>
        <span class="kwrd">struct</span> sockaddr_in client_addr;
        bzero(&client_addr,<span class="kwrd">sizeof</span>(client_addr)); <span class="rem">//把一段内存区的内容全部设置为0</span>
        client_addr.sin_family = AF_INET;    <span class="rem">//internet协议族</span>
        client_addr.sin_addr.s_addr = htons(INADDR_ANY);<span class="rem">//INADDR_ANY表示自动获取本机地址</span>
        client_addr.sin_port = htons(0);    <span class="rem">//0表示让系统自动分配一个空闲端口</span>
        <span class="rem">//创建用于internet的流协议(TCP)socket,用client_socket代表客户机socket</span>
        <span class="kwrd">int</span> client_socket = socket(AF_INET,SOCK_STREAM,0);
        <span class="kwrd">if</span>( client_socket < 0)
        {
            printf(<span class="str">"Create Socket Failed!/n"</span>);
            exit(1);
        }
        <span class="rem">//把客户机的socket和客户机的socket地址结构联系起来</span>
        <span class="kwrd">if</span>( bind(client_socket,(<span class="kwrd">struct</span> sockaddr*)&client_addr,<span class="kwrd">sizeof</span>(client_addr)))
        {
            printf(<span class="str">"Client Bind Port Failed!/n"</span>); 
            exit(1);
        }
    
        <span class="rem">//设置一个socket地址结构server_addr,代表服务器的internet地址, 端口</span>
        <span class="kwrd">struct</span> sockaddr_in server_addr;
        bzero(&server_addr,<span class="kwrd">sizeof</span>(server_addr));
        server_addr.sin_family = AF_INET;
        <span class="kwrd">if</span>(inet_aton(server_IP,&server_addr.sin_addr) == 0) <span class="rem">//服务器的IP地址来自程序的参数</span>
        {
            printf(<span class="str">"Server IP Address Error!/n"</span>);
            exit(1);
        }
        server_addr.sin_port = htons(HELLO_WORLD_SERVER_PORT);
        socklen_t server_addr_length = <span class="kwrd">sizeof</span>(server_addr);
        <span class="rem">//向服务器发起连接,连接成功后client_socket代表了客户机和服务器的一个socket连接</span>
        <span class="kwrd">if</span>(connect(client_socket,(<span class="kwrd">struct</span> sockaddr*)&server_addr, server_addr_length) < 0)
        {
            printf(<span class="str">"Can Not Connect To %s!/n"</span>,server_IP);
            exit(1);
        }
    
        <span class="kwrd">char</span> buffer[BUFFER_SIZE];
        bzero(buffer,BUFFER_SIZE);
        <span class="rem">//从服务器接收数据到buffer中</span>
        <span class="kwrd">int</span> length = recv(client_socket,buffer,BUFFER_SIZE,0);
        <span class="kwrd">if</span>(length < 0)
        {
            printf(<span class="str">"Recieve Data From Server %s Failed!/n"</span>, server_IP);
            exit(1);
        }
        printf(<span class="str">"From Server %s :/t%s"</span>,server_IP,buffer);
    
        bzero(buffer,BUFFER_SIZE);
        sprintf(buffer,<span class="str">"Hello, World! From Client Thread NUM :/t%d/n"</span>,(<span class="kwrd">int</span>)thread_num);
        <span class="rem">//向服务器发送buffer中的数据</span>
        send(client_socket,buffer,BUFFER_SIZE,0);
        <span class="rem">//关闭socket</span>
        close(client_socket);
        pthread_exit(NULL);
    }
    
    <span class="kwrd">int</span> main(<span class="kwrd">int</span> argc, <span class="kwrd">char</span> **argv)
    {
        <span class="kwrd">if</span> (argc != 2)
        {
            printf(<span class="str">"Usage: ./%s ServerIPAddress/n"</span>,argv[0]);
            exit(1);
        }
        server_IP = argv[1];
        
        pthread_t child_thread;
        pthread_attr_t child_thread_attr;
        pthread_attr_init(&child_thread_attr);
        pthread_attr_setdetachstate(&child_thread_attr,PTHREAD_CREATE_DETACHED);
        <span class="kwrd">int</span> i=0;
        <span class="kwrd">for</span>(i=0; i<10000; i++)
        {
            <span class="kwrd">if</span>( pthread_create(&child_thread,&child_thread_attr,talk_to_server,    (<span class="kwrd">void</span> *)i) < 0 )
                printf(<span class="str">"pthread_create Failed : %s/n"</span>,strerror(errno));
        }
        <span class="kwrd">return</span> 0;
    }






