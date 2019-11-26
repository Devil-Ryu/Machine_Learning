# -*- coding: utf-8 -*-
"""
@Author:    Liu Yu
@Contact:   974529965@qq.com
@Date:      2019/11/26 19:36
"""
import argparse
import pandas as pd
import numpy as np
from CART import createTree, loadDataSet
from treePlotter import createPlot

# 配置CMD调用参数
parser = argparse.ArgumentParser()
parser.description = "This function is used to create CART decision tree and plot it"
parser.add_argument("-d", "--dir", help="dir=input the directory of the data",
                    default="./data/loan.xlsx", type=str)
parser.add_argument("-p", "--plot", help="input 1 to plot the tree, others not",
                    default=1, type=int)
args = parser.parse_args()
print("Data directory: {}\nPlot option:{}".format(args.dir, args.plot))

# 测试样例
# dataSet, labels = loadDataSet(args.dir)
dataSet, labels = loadDataSet("../C45/data/lenses.xlsx")
myTree = createTree(dataSet, labels)
print("The decision tree is as bellow:\n", myTree)
if args.plot == 1:
    createPlot(myTree)