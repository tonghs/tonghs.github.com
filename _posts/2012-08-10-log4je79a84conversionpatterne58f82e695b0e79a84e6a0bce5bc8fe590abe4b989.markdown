---
author: ths
comments: true
date: 2012-08-10 06:51:00+00:00
layout: post
slug: log4j%e7%9a%84conversionpattern%e5%8f%82%e6%95%b0%e7%9a%84%e6%a0%bc%e5%bc%8f%e5%90%ab%e4%b9%89
title: log4j的ConversionPattern参数的格式含义
wordpress_id: 859
categories:
- 技术
tags:
- ConversionPattern
- log4j
---

ConversionPattern参数的格式含义  
格式名 含义  
%c 输出日志信息所属的类的全名  
%d 输出日志时间点的日期或时间，默认格式为ISO8601，也可以在其后指定格式，比如：%d{yyy-MM-dd HH:mm:ss }，输出类似：2002-10-18- 22：10：28  
%f 输出日志信息所属的类的类名  
%l 输出日志事件的发生位置，即输出日志信息的语句处于它所在的类的第几行  
%m 输出代码中指定的信息，如log(message)中的message  
%n 输出一个回车换行符，Windows平台为“rn”，Unix平台为“n”  
%p 输出优先级，即DEBUG，INFO，WARN，ERROR，FATAL。如果是调用debug()输出的，则为DEBUG，依此类推  
%r 输出自应用启动到输出该日志信息所耗费的毫秒数  
%t 输出产生该日志事件的线程名 





#1 定义了两个输出端  
log4j.rootLogger = INFO, A1, A2,A3 





#2 定义A1输出到控制器  
log4j.appender.A1 = org.apache.log4j.ConsoleAppender  
#3 定义A1的布局模式为PatternLayout  
log4j.appender.A1.layout = org.apache.log4j.PatternLayout  
#4 定义A1的输出格式  
log4j.appender.A1.layout.ConversionPattern = %-4r [%t] %-5p %c - %m%n 





#5 定义A2输出到文件  
log4j.appender.A2 = org.apache.log4j.RollingFileAppender  
#6 定义A2要输出到哪一个文件  
log4j.appender.A2.File = F:nepalonclassesexample3.log  
#7 定义A2的输出文件的最大长度  
log4j.appender.A2.MaxFileSize = 1KB  
#8 定义A2的备份文件数  
log4j.appender.A2.MaxBackupIndex = 3  
#9 定义A2的布局模式为PatternLayout  
log4j.appender.A2.layout = org.apache.log4j.PatternLayout  
#10 定义A2的输出格式  
log4j.appender.A2.layout.ConversionPattern = %d{yyyy-MM-dd hh:mm:ss}:%p %t %c - %m%n



