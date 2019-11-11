# -*- coding: utf-8 -*-
"""
@Author:    Liu Yu
@Contact:   974529965@qq.com
@Date:      2019/11/11 10:33
"""
import pandas as pd
import numpy as np
from ID3 import createTree
from treePlotter import createPlot

df = pd.read_excel("./data/lenses.xlsx")
dataSet = [list(item) for item in np.array(df)]
labels = list(np.array(df.keys()[:-1]))
myTree = createTree(dataSet, labels)
print(dataSet, type(dataSet))
print(labels, type(labels))
print(myTree)
createPlot(myTree)