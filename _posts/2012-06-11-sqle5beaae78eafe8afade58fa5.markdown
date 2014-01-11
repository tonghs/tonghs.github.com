---
author: ths
comments: true
date: 2012-06-11 06:57:00+00:00
layout: post
slug: sql%e5%be%aa%e7%8e%af%e8%af%ad%e5%8f%a5
title: sql循环语句
wordpress_id: 807
categories:
- 技术
tags:
- sql
- 循环
---

<span class="kwrd">declare</span> @i <span class="kwrd">int</span>
    <span class="kwrd">set</span> @i=1
    <span class="kwrd">while</span> @i<30
    <span class="kwrd">begin</span>
    insert <span class="kwrd">into</span> test (userid) <span class="kwrd">values</span>(@i)
    <span class="kwrd">set</span> @i=@i+1
    <span class="kwrd">end</span>
    
    -------------<span class="rem">--</span>
    
    <span class="kwrd">while</span> 条件
    <span class="kwrd">begin</span>
    执行操作
    <span class="kwrd">set</span> @i=@i+1
    end





WHILE  
设置重复执行 SQL 语句或语句块的条件。只要指定的条件为真，就重复执行语句。可以使用 BREAK 和 CONTINUE 关键字在循环内部控制 WHILE 循环中语句的执行。






语法  
WHILE Boolean_expression  
{ sql_statement | statement_block }  
[ BREAK ]  
{ sql_statement | statement_block }  
[ CONTINUE ]






参数  
Boolean_expression






返回 TRUE 或 FALSE 的表达式。如果布尔表达式中含有 SELECT 语句，必须用圆括号将 SELECT 语句括起来。






{sql_statement | statement_block}






Transact-SQL 语句或用语句块定义的语句分组。若要定义语句块，请使用控制流关键字 BEGIN 和 END。






BREAK






导致从最内层的 WHILE 循环中退出。将执行出现在 END 关键字后面的任何语句，END 关键字为循环结束标记。






CONTINUE






使 WHILE 循环重新开始执行，忽略 CONTINUE 关键字后的任何语句。






注释  
如果嵌套了两个或多个 WHILE 循环，内层的 BREAK 将导致退出到下一个外层循环。首先运行内层循环结束之后的所有语句，然后下一个外层循环重新开始执行。






示例  
A. 在嵌套的 IF...ELSE 和 WHILE 中使用 BREAK 和 CONTINUE  
在下例中，如果平均价格少于 $30，WHILE 循环就将价格加倍，然后选择最高价。如果最高价少于或等于 $50，WHILE 循环重新启动并再次将价格加倍。该循环不断地将价格加倍直到最高价格超过 $50，然后退出 WHILE 循环并打印一条消息。
    
    <span class="kwrd">USE</span> pubs
    <span class="kwrd">GO</span>
    <span class="kwrd">WHILE</span> (<span class="kwrd">SELECT</span> <span class="kwrd">AVG</span>(price) <span class="kwrd">FROM</span> titles) < $30
    <span class="kwrd">BEGIN</span>
        <span class="kwrd">UPDATE</span> titles
           <span class="kwrd">SET</span> price = price * 2
        <span class="kwrd">SELECT</span> <span class="kwrd">MAX</span>(price) <span class="kwrd">FROM</span> titles
        <span class="kwrd">IF</span> (<span class="kwrd">SELECT</span> <span class="kwrd">MAX</span>(price) <span class="kwrd">FROM</span> titles) > $50
           <span class="kwrd">BREAK</span>
        <span class="kwrd">ELSE</span>
           <span class="kwrd">CONTINUE</span>
    <span class="kwrd">END</span>
    <span class="kwrd">PRINT</span> <span class="str">'Too much for the market to bear'</span>










B. 在带有游标的过程中使用 WHILE  
以下的 WHILE 结构是名为 count_all_rows 过程中的一部分。下例中，该 WHILE 结构测试用于游标的函数 @@FETCH_STATUS 的返回值。因为 @@FETCH_STATUS 可能返回 –2、-1 或 0，所以，所有的情况都应进行测试。如果某一行在开始执行此存储过程以后从游标结果中删除，将跳过该行。成功提取 (0) 后将执行 BEGIN...END 循环内部的 SELECT 语句。




    
    <span class="kwrd">USE</span> pubs
    <span class="kwrd">DECLARE</span> tnames_cursor <span class="kwrd">CURSOR</span>
    <span class="kwrd">FOR</span>
        <span class="kwrd">SELECT</span> TABLE_NAME 
        <span class="kwrd">FROM</span> INFORMATION_SCHEMA.TABLES
    <span class="kwrd">OPEN</span> tnames_cursor
    <span class="kwrd">DECLARE</span> @tablename sysname
    --<span class="kwrd">SET</span> @tablename = <span class="str">'authors'</span>
    <span class="kwrd">FETCH</span> <span class="kwrd">NEXT</span> <span class="kwrd">FROM</span> tnames_cursor <span class="kwrd">INTO</span> @tablename
    <span class="kwrd">WHILE</span> (@@FETCH_STATUS <> -1)
    <span class="kwrd">BEGIN</span>
        <span class="kwrd">IF</span> (@@FETCH_STATUS <> -2)
        <span class="kwrd">BEGIN</span>    
           <span class="kwrd">SELECT</span> @tablename = RTRIM(@tablename) 
           <span class="kwrd">EXEC</span> (<span class="str">'SELECT '</span><span class="str">''</span> + @tablename + <span class="str">''</span><span class="str">' = count(*) FROM '</span> 
                 + @tablename )
           <span class="kwrd">PRINT</span> <span class="str">' '</span>
       <span class="kwrd">END</span>
        <span class="kwrd">FETCH</span> <span class="kwrd">NEXT</span> <span class="kwrd">FROM</span> tnames_cursor <span class="kwrd">INTO</span> @tablename
    <span class="kwrd">END</span>
    <span class="kwrd">CLOSE</span> tnames_cursor
    <span class="kwrd">DEALLOCATE</span> tnames_cursor
    
    











