### 使用说明
仓库的中的文件夹是一些我自己常用的eclipse插件。

* 插件的存放目录结构

```
repo-|
     |-pluginName-|
                  |-eclipse-|
                            |-features
                            |-plugins
```

pluginName可以随便命名(用英文和下划线)，后面的eclipse和features、plugins目录要按照规则存放

* 运行命令，生成link文件

```
rm *.link
python build.py
```

* 将link文件拷贝到eclipse的dropins目录下(如果eclipse已经启动，重启eclipse)

### 插件地址
[SVN for eclipse](http://subclipse.tigris.org/servlets/ProjectProcess;jsessionid=E34869251B061FB6FE5772223F76CF1F?pageID=p4wYuA)

