---
author: ths
comments: true
date: 2012-05-17 09:19:00+00:00
layout: post
slug: sql-server-%e8%a1%a8%e7%bb%93%e6%9e%84%e5%af%bc%e5%87%ba%e5%88%b0excel
title: sql server 表结构导出到excel
wordpress_id: 754
categories:
- 技术
tags:
- sql
- 表结构导出
---

SELECT  
        表名       = <span style="color: #0000ff">case</span> when a.colorder=1 then d.name <span style="color: #0000ff">else</span> '' end,   
        表说明     = <span style="color: #0000ff">case</span> when a.colorder=1 then isnull(f.<span style="color: #0000ff">value</span>,'') <span style="color: #0000ff">else</span> '' end,   
        -- 字段序号   = a.colorder,   
        字段名     = a.name,   
        标识       = <span style="color: #0000ff">case</span> when COLUMNPROPERTY( a.id,a.name,'IsIdentity')=1 then '√'<span style="color: #0000ff">else</span> '' end,   
        主键       = <span style="color: #0000ff">case</span> when exists(SELECT 1 FROM sysobjects where xtype='PK' and parent_obj=a.id and name <span style="color: #0000ff">in</span> (   
                         SELECT name FROM sysindexes WHERE indid <span style="color: #0000ff">in</span>( SELECT indid FROM sysindexkeys WHERE id = a.id AND colid=a.colid))) then '√' <span style="color: #0000ff">else</span> '' end,   
        类型       = b.name,   
        占用字节数 = a.length,   
        长度       = COLUMNPROPERTY(a.id,a.name,'PRECISION'),   
        小数位数   = isnull(COLUMNPROPERTY(a.id,a.name,'Scale'),0),   
        允许空     = <span style="color: #0000ff">case</span> when a.isnullable=1 then '√'<span style="color: #0000ff">else</span> '' end,   
        默认值     = isnull(e.text,''),   
        字段说明   = isnull(g.[<span style="color: #0000ff">value</span>],'')   
    FROM  
        syscolumns a   
    left join  
        systypes b   
    on  
        a.xusertype=b.xusertype   
    inner join  
        sysobjects d   
    on  
        a.id=d.id  and d.xtype='U' and  d.name<>'dtproperties'   
    left join  
        syscomments e   
    on  
        a.cdefault=e.id   
    left join  
    sys.extended_properties   g   
    on  
        a.id=G.major_id and a.colid=g.minor_id   
    left join  
      
    sys.extended_properties f   
    on  
        d.id=f.major_id and f.minor_id=0   
    -- where d.name='C_PARTY_SPREADER'    --如果只查询指定表,加上此条件   
    order by  
        a.id,a.colorder  





代码效果：![sql server 表结构 导出 到excel - Abbey·dawn - Abbey·dawn](http://img693.ph.126.net/IU9DuqesdNuaCIxyah-QYg==/2811372067387320047.png)



