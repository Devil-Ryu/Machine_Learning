# -*- coding: utf-8 -*-
"""
@Author:    Liu Yu
@Contact:   974529965@qq.com
@Date:      2019/11/11 10:33
"""
import argparse
import pandas as pd
import numpy as np
from ID3 import createTree
from treePlotter import createPlot


parser = argparse.ArgumentParser()
parser.description = "This function is used to create ID3 decision tree and plot it"
parser.add_argument("-d", "--dir", help="dir=input the directory of the data",
                    default="./data/lenses.xlsx", type=str)
parser.add_argument("-p", "--plot", help="input 1 to plot the tree, others not",
                    default=1, type=int)
args = parser.parse_args()
print("Data directory: {}\nPlot option:{}".format(args.dir, args.plot))
df = pd.read_excel(args.dir)
dataSet = [list(item) for item in np.array(df)]
labels = list(np.array(df.keys()[:-1]))
myTree = createTree(dataSet, labels)
print("The decision tree is as bellow:\n", myTree)
if args.plot == 1:
    createPlot(myTree)