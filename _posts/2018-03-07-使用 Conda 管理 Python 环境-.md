---
published: false
---
## 使用 Conda 管理 Python 环境

Conda 可以方便的管理 Python 环境，可用于管理包依赖、解决多版本共存等等问题，我们使用的是 Miniconda。查看 [Miniconda 的下载地址](https://conda.io/miniconda.html)。安装方法请参考[该文档](https://conda.io/docs/user-guide/install/linux.html)。
Conda 的设计理念：Conda 将几乎所有的工具、第三方包都当做 package 对待，甚至包括 Python 和 Conda 自身！Conda 使用类似沙箱的机制来隔离不同的项目之间的环境。所以对一个新项目来说，我们首先需要新建环境。
### 环境管理
使用命令行新建环境
```bash
* 新建环境：
conda create --name myenv

* 新建环境是指定 Python 版本：
conda create -n myenv python=3.4

* 新建包含特定包的环境：
conda create -n myenv scipy
或者
conda create -n myenv python
conda install -n myenv scipy

* 新建环境包含特定包并制定特定版本：
conda create -n myenv scipy=0.15.0

* 新建包含多个包的环境：
conda create -n myenv python=3.4 scipy=0.15.0 astroid babel

* To automatically install pip or another program every time a new environment is created, add the default programs to the create_default_packages section of your .condarc configuration file. The default packages are installed every time you create a new environment. If you do not want the default packages installed in a particular environment, use the --no-default-packages flag:
conda create --no-default-packages -n myenv python
```

使用以下命令参考更多：
```markup
conda create --help
```

使用 environment.yml 文件创建环境
```bash
conda env create -f environment.yml
```

根据 environment.yml 更新环境
```bash
conda env update -f environment.yml
```

进入环境
```bash
source activate myenv
```

退出环境
```bash
source deactivate
```

克隆环境
```
conda create --name myclone --clone myenv
```

查看环境 package list
```
* 在环境内：
conda list

* 不在环境内：
conda list -n myenv
```

在环境中同样可以使用 pip：
```
conda install -n myenv pip
source
 activate myenv
pip <pip_subcommand>
```

删除环境
```
conda remove --name myenv --all
```

### environment.yml 文件
根据当前环境导出
```bash
conda env export > environment.yml
```
此时可以将创建的 environment.yml 文件 share 其他同学。

手动创建
我们也可以手动创建 environment.yml 文件。一个简单的例子：
```yaml
name: stats
dependencies:
  - numpy
  - pandas
```

一个复杂点的例子：
```yaml
name: stats2
channels:
  - javascript
dependencies:
  - python=3.4   # or 2.7
  - bokeh=0.9.2
  - numpy=1.9.*
  - nodejs=0.10.*
  - flask
  - pip:
    - Flask-Testing
```

既然有了 dependencies 为什么还用 pip 呢？我考虑可能是 pip 可以使用 github 或 url 的方式安装包，而将 url 直接写在 dependencies 中应该不行。

### 包管理
conda 的大部分命令跟 pip 类似，基本上有一下命令：
* search：搜索包
* install：安装包
* 使用 pip 安装包
* list：列出所有包
* update：更新包
* remove：删除包
