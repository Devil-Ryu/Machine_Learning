# -*- coding: utf-8 -*-
"""
@Author:    Liu Yu
@Contact:   974529965@qq.com
@Date:      2019/11/5 17:47
"""
from graphviz import Digraph

def plotTree(inTree):
    if isinstance(inTree, dict):  # 如果输入为字典即树
        firstStr = inTree["spFeat"]
        splitValue = inTree["spVal"]
        leftTree = inTree["left"]
        rightTree = inTree["right"]
        rootNodeNumber = createPlot.nodeNum  # 从结点编号中获取树节点编号
        createPlot.graph.node(name="%s" % rootNodeNumber, label=firstStr, fontname="FangSong", shape="box")  # 创建树结点
        createPlot.nodeNum += 1  # 创造结点后，节点编号加一
        lLabel = ""
        rLabel = ""
        if isinstance(splitValue, str):
            lLabel = splitValue
            rLabel = "not "+splitValue
        else:
            lLabel = "<={}".format(splitValue)
            rLabel = ">{} ".format(splitValue)
        createPlot.graph.edge("%s" % rootNodeNumber, plotTree(leftTree), label=lLabel)  # 连接左子树
        createPlot.graph.edge("%s" % rootNodeNumber, plotTree(rightTree), label=rLabel)  # 连接右子树
        return str(rootNodeNumber)
    else:
        leafNodeNumber = createPlot.nodeNum
        createPlot.graph.node(name="%s" % leafNodeNumber, label=inTree, fontname="FangSong")  # 创建叶结点
        createPlot.nodeNum += 1
        return str(leafNodeNumber)

def createPlot(inTree):
    createPlot.graph = Digraph()
    createPlot.nodeNum = 0
    plotTree(inTree)
    createPlot.graph.view(filename="myTree")


if __name__ == '__main__':
    from CART import *
    filename = "./data/loan.xlsx"
    dataSet, labels = loadDataSet(filename)
    print(dataSet)
    myTree = createTree(dataSet, labels)
    print(myTree)
    createPlot(myTree)
