---
author: ths
comments: false
date: 2011-10-08 07:24:00+00:00
layout: post
slug: java%e5%88%a9%e7%94%a8xml-rpc%e5%8d%8f%e8%ae%ae%e6%93%8d%e4%bd%9cwordpress%e5%8d%9a%e5%ae%a2
title: Java利用xml-rpc协议操作wordpress博客
wordpress_id: 681
categories:
- 技术
tags:
- wordpress
- xml-rpc
---

<





p>wordpress遵循xml-rpc协议，如果在wordpress中打开rpc协议，那么你就可以利用工具或者程序发表文章。





<





p>wordpress官方rpc协议文档：[http://codex.wordpress.org/XML-RPC_wp](http://codex.wordpress.org/XML-RPC_wp)





<





p>metaWeblog协议文档：[http://www.xmlrpc.com/metaWeblogApi](http://www.xmlrpc.com/metaWeblogApi)





<





p>本文参考文档：[http://www.ibm.com/developerworks/cn/xml/x-metablog/](http://www.ibm.com/developerworks/cn/xml/x-metablog/)





<





p>发表博客代码：





<





p>public static void post(String title, String content) {  
try {  
// Set up XML-RPC connection to server  
String domain = "wangjun.easymorse.com";// 你网站的域名  
XmlRpcClientConfigImpl config = new XmlRpcClientConfigImpl();  
config.setServerURL(new URL("http://" + domain + "/xmlrpc.php"));  
XmlRpcClient client = new XmlRpcClient();  
client.setConfig(config);  
Map post = new HashMap();  
post.put("title", title);// 标题  
post.put("mt_keywords", "java");// 标签  
Object[] categories = new Object[] { "计算机" };// 分类  
post.put("categories", categories);  
post.put("description", content);// 内容  
Object[] params = new Object[] { "1", "username", "password",post,true }; // 1代表正式发布，0代表草稿  
String ob = (String) client.execute("metaWeblog.newPost", params);  
System.out.println("Created with blogid " + ob);  
} catch (Exception e) {  
System.out.println(" UnCreated " + e.getMessage());  
}  
}  
public static void main(String[] args) {  
PostBlog.post("发布测试博客","测试成功");  
}





<





p>得到分类列表代码：





<





p>public static void getBlogCategories() {  
try{  
String domain = "wangjun.easymorse.com";//你网站的域名  
XmlRpcClientConfigImpl config = new XmlRpcClientConfigImpl();  
config.setServerURL(new URL("http://"+domain+"/xmlrpc.php"));  
XmlRpcClient client = new XmlRpcClient();  
client.setConfig(config);  
Object[] params = new Object[] {"技术分享", "username", "password" };  
// 得到分类列表  
Object[] ob=(Object[])client.execute("metaWeblog.getCategories", params);  
System.out.println("分类列表："+ob.length+","+ob[1]);  
}catch (Exception e) {  
System.out.println(" UnCreated "+e.getMessage());  
}  
}  
public static void main(String[] args) {  
GetBlogCategories.getBlogCategories();  
}





<





p>得到已经发表的博客文章代码：





public static void post() {  
try{  
String domain = "wangjun.easymorse.com";//你网站的域名  
XmlRpcClientConfigImpl config = new XmlRpcClientConfigImpl();  
config.setServerURL(new URL("http://"+domain+"/xmlrpc.php"));  
XmlRpcClient client = new XmlRpcClient();  
client.setConfig(config);  
Object[] params = new Object[] {"485", "wangjun", "password",10};  
Object[] ob=(Object[])client.execute("metaWeblog.getRecentPosts", params);  
System.out.println("得到博客 " + ob[7]);  
}catch (Exception e) {  
System.out.println(" UnCreated "+e.getMessage());  
}  
}  
public static void main(String[] args) {  
GetBlog.post();  
} 



