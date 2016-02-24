---
published: true
title: VBoxManage 常用命令
tagline: VBoxManage
layout: post
---


### 常用命令
```
VBoxManage list vms
VBoxManage clonevm ubuntu_15.05 --name new_vm_name --register
VBoxManage showvminfo ac_jira
VBoxManage export ubuntu_15.04 -o ubuntu_15.04_base.ova
VBoxManage import ubuntu_15.04_base.ova
VBoxManage clonevm ubuntu_15.04 --name ac_jira --register
VBoxManage unregistervm ubuntu_15.04_jira --delete
VBoxManage modifyvm "Windows XP" --memory 2048
```

### 端口映射
```
VBoxManage modifyvm "ac_gitlab" --natpf1 "ssh,tcp,,2205,,22"
VBoxManage modifyvm "ac_gitlab" --natpf1 delete ssh
```

### 快照
```
VBoxManage snapshot ac_jira take ac_jira_init
```
