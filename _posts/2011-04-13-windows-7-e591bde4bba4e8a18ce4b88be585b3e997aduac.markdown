---
author: ths
comments: true
date: 2011-04-13 03:45:00+00:00
layout: post
slug: windows-7-%e5%91%bd%e4%bb%a4%e8%a1%8c%e4%b8%8b%e5%85%b3%e9%97%aduac
title: windows 7 命令行下关闭UAC
wordpress_id: 610
categories:
- 折腾
tags:
- UAC
---

reg.exe ADD HKLMSOFTWAREMicrosoftWindowsCurrentVersionPoliciesSystem /v EnableLUA /t REG_DWORD /d 0 /f



