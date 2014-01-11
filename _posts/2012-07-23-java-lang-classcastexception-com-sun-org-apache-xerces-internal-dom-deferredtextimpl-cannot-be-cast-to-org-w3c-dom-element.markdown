---
author: ths
comments: true
date: 2012-07-23 11:29:00+00:00
layout: post
slug: java-lang-classcastexception-com-sun-org-apache-xerces-internal-dom-deferredtextimpl-cannot-be-cast-to-org-w3c-dom-element
title: 'java.lang.ClassCastException: com.sun.org.apache.xerces.internal.dom.DeferredTextImpl
  cannot be cast to org.w3c.dom.Element'
wordpress_id: 825
categories:
- 技术
tags:
- xml
---

在处理xml时遇到如下错误:java.lang.ClassCastException: com.sun.org.apache.xerces.internal.dom.DeferredTextImpl cannot be cast to org.w3c.dom.Element




    
    
    xml文档
    
    <?xml version=<span class="str">"1.0"</span> encoding=<span class="str">"GB2312"</span> ?>
    <PhoneInfo>
        <Brand name=<span class="str">"联想"</span>>
            <Type name=<span class="str">"A60"</span>></Type>
        </Brand>
        <Brand name=<span class="str">"苹果"</span>>
            <Type name=<span class="str">"iphone4"</span>></Type>
            <Type name=<span class="str">"iphone5"</span>></Type>
        </Brand>
    </PhoneInfo>
    
    
    
    DOM解析文档
    
    import javax.xml.parsers.DocumentBuilder;
    import javax.xml.parsers.DocumentBuilderFactory;
    
    
    import org.w3c.dom.Document;
    import org.w3c.dom.Element;
    import org.w3c.dom.Node;
    import org.w3c.dom.NodeList;
    
    
    
    <span class="kwrd">public</span> <span class="kwrd">class</span> MyTest {
        <span class="kwrd">public</span> <span class="kwrd">static</span> <span class="kwrd">void</span> main(String[] args) {
            <span class="kwrd">try</span>{
                DocumentBuilderFactory dbf=DocumentBuilderFactory.newInstance();
                DocumentBuilder db=dbf.newDocumentBuilder();
                Document doc=db.parse(<span class="str">"src/收藏信息.xml"</span>);
                NodeList brandlList=doc.getElementsByTagName(<span class="str">"Brand"</span>);
                
                <span class="kwrd">for</span>(<span class="kwrd">int</span> i=0;i<brandlList.getLength();i++){
                    Node brand =brandlList.item(i);
                    Element element=(Element)brand;
                    String attrValue=element.getAttribute(<span class="str">"name"</span>);
                    NodeList types=element.getChildNodes();
                    <span class="kwrd">for</span>(<span class="kwrd">int</span> j=0;j<types.getLength();j++){
                        Element typeElement=((Element)types.item(j));
                        String type=typeElement.getAttribute(<span class="str">"name"</span>);
                    }
                }
            }<span class="kwrd">catch</span>(Exception e){
                e.printStackTrace();
            }
        }
    }





改为如下即可(红色部分):








    
    
    xml文档
    
    <?xml version=<span class="str">"1.0"</span> encoding=<span class="str">"GB2312"</span> ?>
    <PhoneInfo>
        <Brand name=<span class="str">"联想"</span>>
            <Type name=<span class="str">"A60"</span>></Type>
        </Brand>
        <Brand name=<span class="str">"苹果"</span>>
            <Type name=<span class="str">"iphone4"</span>></Type>
            <Type name=<span class="str">"iphone5"</span>></Type>
        </Brand>
    </PhoneInfo>
    
    
    
    DOM解析文档
    
    import javax.xml.parsers.DocumentBuilder;
    import javax.xml.parsers.DocumentBuilderFactory;
    
    
    import org.w3c.dom.Document;
    import org.w3c.dom.Element;
    import org.w3c.dom.Node;
    import org.w3c.dom.NodeList;
    
    
    
    <span class="kwrd">public</span> <span class="kwrd">class</span> MyTest {
        <span class="kwrd">public</span> <span class="kwrd">static</span> <span class="kwrd">void</span> main(String[] args) {
            <span class="kwrd">try</span>{
                DocumentBuilderFactory dbf=DocumentBuilderFactory.newInstance();
                DocumentBuilder db=dbf.newDocumentBuilder();
                Document doc=db.parse(<span class="str">"src/收藏信息.xml"</span>);
                NodeList brandlList=doc.getElementsByTagName(<span class="str">"Brand"</span>);
                
                <span class="kwrd">for</span>(<span class="kwrd">int</span> i=0;i<brandlList.getLength();i++){
                    Node brand =brandlList.item(i);
                    Element element=(Element)brand;
                    String attrValue=element.getAttribute(<span class="str">"name"</span>);
                    NodeList types=element.getChildNodes();
                    <span class="kwrd">for</span>(<span class="kwrd">int</span> j=0;j<types.getLength();j++){     <span class="rem">//判断子节点是否为Element</span>            <font color="#ff0000"><span class="kwrd"><font color="#ff0000">if</font></span>(types.items(j) instanceof Element){</font>
                            Element typeElement=((Element)types.item(j));
                            String type=typeElement.getAttribute(<span class="str">"name"</span>);
                        <font color="#ff0000">}</font>
                    }
                }
            }<span class="kwrd">catch</span>(Exception e){
                e.printStackTrace();
            }
        }
    }



















