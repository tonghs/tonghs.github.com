---
published: true
---
## git merge 和 rebase 区别
git merge 和 rebase 都是将一个分支的变更并入另一个分支，只是方式不一样。假设我们的代码库是这样的：

![image.png | center | 832x494](https://lark-assets-prod.oss-cn-hangzhou.aliyuncs.com/2018/png/f3b23df7-71f3-4663-86cd-da518d44cc71.png)
##### Merge
```
git checkout feature
git merge master
```

执行上面的命令后，会得到下面的结果：

![image.png | center | 832x521](https://lark-assets-prod.oss-cn-hangzhou.aliyuncs.com/2018/png/99914f75-f280-4c76-88af-1ab31869f749.png)

##### Rebase
```
git checkout feature
git rebase master
```

执行上面命令后，会得到如下结果：
[  
](http://wiki.tonghs.com/?attachment_id=188)
![image.png | center | 832x518](https://lark-assets-prod.oss-cn-hangzhou.aliyuncs.com/2018/png/652b5265-a374-4036-a99f-434480e8f82f.png)
