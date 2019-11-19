## 简介

这项工程用于重现决策树中的ID3算法，在此处主要介绍该程序的环境和文件解释，以及怎样使用该程序处理数据。若是对原理感兴趣[点击这里]( https://blog.csdn.net/qq_39736559/article/details/103009243 )查看相关算法原理。

## 环境

- python3.7
- numpy
- matplotlib
- pandas
- math
- operator
- argparse

## 文件解释

- **ID3.py**：存放ID3的主要算法的文件，使用其中的`CreateTree()`函数可构建决策树

- **treePlotter.py**：存放绘制决策树程序的文件，使用其中的`CreatePlot()`函数可绘制决策树

- **tree_test.py**：功能性文件，可在命令行中运行以运行决策树实例以及绘制图形

## 数据集

1. **DATASET**: Database for fitting contact lenses
2. **Number of Instances**: 24
3. **Number of Attributes**: 4 (all nominal)
4. **Attribute Information**: 3 Classes
   -  the patient should be fitted with hard contact lenses,
   -  the patient should be fitted with soft contact lenses,
   -  the patient should not be fitted with contact lenses.

1. **age of the patient**: (1) young, (2) pre-presbyopic, (3) presbyopic
2. **spectacle prescription**: (1) myope, (2) hypermetrope
3. **astigmatic**:   (1) no, (2) yes
4. **tear production rate**: (1) reduced, (2) normal

## 文件用法
首先克隆项目并进入到**tree_test.py**所在文件夹，在此处打开cmd，若要测试已有的数据集则输入
```python
python tree_test.py
```

若要测试自己的数据集，则输入

```python
python tree_test.py -d="your dir of dataset"
```

