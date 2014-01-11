---
author: ths
comments: true
date: 2010-12-27 08:42:00+00:00
layout: post
slug: '%e8%ae%be%e7%bd%aewinform%e7%a8%8b%e5%ba%8f%e5%bc%80%e6%9c%ba%e8%87%aa%e5%8a%a8%e5%90%af%e5%8a%a8'
title: 设置winform程序开机自动启动
wordpress_id: 416
categories:
- 分享
- 技术
tags:
- winform
- 开机自启动
---

/// <summary>  
/// 设置开机自动启用  
/// </summary>  
private void SetAutoStart()  
{  
try  
{  
string regPath = "SOFTWAREMicrosoftWindowsCurrentVersionRun";  
string path = Application.ExecutablePath.ToLower(); //将当前程序起动路径  
string name = Path.GetFileName(path); //获得应用程序名称  
var regKey = Microsoft.Win32.Registry.LocalMachine.OpenSubKey(regPath, true);  
if (regKey == null) regKey = Microsoft.Win32.Registry.LocalMachine.CreateSubKey(regPath);  
regKey.SetValue(name, path);  
}catch{ }  
}



