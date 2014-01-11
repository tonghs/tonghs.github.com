---
author: ths
comments: true
date: 2013-11-11 13:28:00+00:00
layout: post
slug: extjs-gridpanle-%e5%8d%95%e5%85%83%e6%a0%bc%e6%b7%bb%e5%8a%a0tooltip
title: Extjs GridPanel 单元格添加tooltip
wordpress_id: 1283
categories:
- 技术
tags:
- Extjs
- tooltip
---

先看代码：




    
    <code>// Init the singleton.  Any tag-based quick tips will start working.
    Ext.tip.QuickTipManager.init();
    
    Ext.widget('grid', {
        title: 'Users',
        store: {
            fields: ['name', 'email', 'comment'],
            data: [
                { 'name': 'Lisa', 'email': 'lisa@simpsons.com', 'comment': 'some comment' },
                { 'name': 'Bart', 'email': 'bart@simpsons.com', 'comment': 'comment' },
                { 'name': 'Homer', 'email': 'home@simpsons.com', 'comment': 'some very long comment' },
                { 'name': 'Marge', 'email': 'marge@simpsons.com', 'comment': 'some very very very very long comment' }
            ]
        },
        columns: [
            { header: 'Name', dataIndex: 'name', width: 100 },
            { header: 'Email', dataIndex: 'email', width: 150 },
            {
                header: 'comment',
                dataIndex: 'comment',
                flex: 1,
                renderer: function (value, meta, record) {
                    var max = 15;
                    meta.tdAttr = 'data-qtip="' + value + '"';
                    return value.length < max ? value : value.substring(0, max - 3) + '...';
                }
            }
        ],
        width: 400,
        renderTo: 'output'
    });
    </code>





把renderer方法封装到util中发现不好用，再回头看代码发现少写了一行，就是第一行，QuickTipManager的初始化代码。



