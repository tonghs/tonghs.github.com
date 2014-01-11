---
author: ths
comments: true
date: 2011-04-08 07:46:00+00:00
layout: post
slug: sql%e8%af%ad%e5%8f%a5%e5%88%86%e9%a1%b5%ef%bc%88sqlserver%ef%bc%89
title: SQL语句分页（SQLServer）
wordpress_id: 603
categories:
- 技术
tags:
- sql
- 分页
---

<





p>**方法一：**





<





p>SELECT TOP 页大小 _  
FROM table1  
WHERE id NOT IN  
(  
SELECT TOP 页大小_(页数-1) id FROM table1 ORDER BY id  
)  
ORDER BY id





<





p>**方法二：**





<





p>SELECT TOP 页大小 _  
FROM table1  
WHERE id >  
(  
SELECT ISNULL(MAX(id),0)   
FROM  
(  
SELECT TOP 页大小_(页数-1) id FROM table1 ORDER BY id  
) A  
)  
ORDER BY id





<





p>**方法三：**SQL 2005可以这样用：





<





p>SELECT TOP 页大小 _  
FROM  
(  
SELECT ROW_NUMBER() OVER (ORDER BY id) AS RowNumber,_ FROM table1  
) A  
WHERE RowNumber > 页大小*(页数-1)





分类: [SQL Server](http://www.cnblogs.com/lijun198504/category/153181.html), [access](http://www.cnblogs.com/lijun198504/category/166346.html)



