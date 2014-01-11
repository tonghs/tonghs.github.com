---
author: ths
comments: true
date: 2012-10-29 06:37:00+00:00
layout: post
slug: microsoft-office-interop-word-document-doc-new-microsoft-office-interop-word-document-%e6%8a%9b%e5%87%ba%e5%bc%82%e5%b8%b8%ef%bc%9f
title: Microsoft.Office.Interop.Word.Document doc = new Microsoft.Office.Interop.Word.Document();
  抛出异常？
wordpress_id: 950
categories:
- 技术
tags:
- c
- word
---

程序执行到这个的时候老是会抛出异常： 





Microsoft.Office.Interop.Word.Document doc = new Microsoft.Office.Interop.Word.Document(); 抛出异常？ 





+ ex {"从 IClassFactory 为 CLSID 为 {00020906-0000-0000-C000-000000000046} 的 COM 组件创建实例失败，原因是出现以下错误: 8001010a。"} System.Exception {System.Runtime.InteropServices.COMException} 





Please try this code:




    
    Word.Application oWord = new Word.Application();
    Word.Document oDoc = oWord.Documents.Add();



