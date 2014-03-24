---
layout: post
title: Mercurial 使用记录
---
平时用 git，公司用 Mercurial，其实两者用法相同点很多，不同点也有不少。

最近使用 Mercurial 有几点记录如下：

* 代码回滚

	hg revert -r 8 –all 将所有代码库中的文件回滚到版本8的状态
	
	hg revert -r 8 filename 将代码库中的某个文件回滚到版本8的状态
	
* 删除和添加
	
	hg addremove 
	
	该命令在你手动的对大量文件进行操作的时候会显得很方便。改变文件结构然后再运行 hg addremove 命令让 Mercurial 来识别你做了哪些改变。