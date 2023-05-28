# pattern

西北工业大学 模式识别与机器学习大作业

初始化时将数据集 `dataset.rar`放入项目根目录，随后运行 `scripts/init.sh` 即可，会完成数据集的解压和归类

在项目根目录下运行下述指令：

```shell
chmod +x scripts/init.sh
scripts/init.sh
```

运行环境依靠 `requirements.txt`配置即可，通过pip可以完成配置

```shell
pip install requirements.txt
```


## renewjson.py

将json文件名中含有有空格的删除空格进行重命名

实现查找DDH和normal下labels中的json文件是否存在问题(有无多标签、少标签、重复标签),忽略normal下labels中的json文件有部分FHL和FHR标签不是circle的情况

将FHL和FHR的circle类型转化为point类型,只保留圆心的坐标数据,第二个点坐标数据无用

将json中类型为polygon的单点转化为point类型

将更新后的json文件保存在labels_new中，并将错误的json文件删除

## jsontrans.py

实现将DDH和normal下labels_new中的json文件转化成mask图片和viz图片,供神经网络输入数据使用

生成的临时文件夹temp1和temp2无用，可删除

由于要生成较多的mask图片,因此运行时间较长
