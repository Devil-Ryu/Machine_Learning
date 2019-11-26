# -*- coding: utf-8 -*-
"""
@Author:    Liu Yu
@Contact:   974529965@qq.com
@Date:      2019/11/19 16:41
"""
import pandas as pd
import numpy as np
import operator

def loadDataSet(filename):
    """
    加载数据集
    :param filename: 文件路径及名称
    :return: dataSet,labels
    """
    df = pd.read_excel(filename)
    data = [list(item) for item in np.array(df)]
    labels = list(df.keys()[:-1])
    return data, labels

def calGini(dataSet):
    """
    计算基尼不纯度
    :param dataSet: 数据集
    :return: 香农熵
    """
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        # label为最后一列
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    giniImpurity = 1
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        giniImpurity -= prob * prob
    return giniImpurity

def splitDataSet(dataSet, feature, value):
    """
    二分划分数据集
    :param dataSet:数据集
    :param feature:特征列索引
    :param value:特征值
    :return:划分的数据集
    """
    # 判断数值类型为离散型还是连续型
    if isinstance(dataSet[0][feature], str):  # 若为离散型(即为字符)
        mat0 = [item for item in dataSet if item[feature] == value]
        mat1 = [item for item in dataSet if item[feature] != value]
        return mat0, mat1
    else:
        mat0 = [item for item in dataSet if item[feature] <= value]
        mat1 = [item for item in dataSet if item[feature] > value]
        return mat0, mat1

def chooseBestFeatureToSplit(dataSet):
    """
    选择用于分割数据集的最好的特征
    :param dataSet: 数据集
    :return: 最好的特征的序号
    """
    numFeatures = len(dataSet[0]) - 1
    baseGini = calGini(dataSet)
    bestGiniGain = 0.0
    bestFeature = - 1
    bestValue = 0
    for i in range(numFeatures):  # 遍历每一个特征列
        featList = [example[i] for example in dataSet]  # 第i个特征列
        if isinstance(featList[0], str):  # 判断该特征列是否为离散型
            uniqueVals = set(featList)  # 若为离散型,求该特征列的特征值集合
        else:  # 若为连续型
            sortedFeat = sorted(featList)
            uniqueVals = np.mean([[sortedFeat[i], sortedFeat[i + 1]] for i in range(len(sortedFeat) - 1)],
                                 axis=1)  # 找到经过排序后的连续型变量的相邻中点
            uniqueVals = set(uniqueVals)
        for value in uniqueVals:
            mat0, mat1 = splitDataSet(dataSet, i, value)
            prob0 = len(mat0) / float(len(dataSet))
            prob1 = len(mat1) / float(len(dataSet))
            newGini = prob0 * calGini(mat0) + prob1 * calGini(mat1)
            GiniGain = baseGini - newGini
            if GiniGain > bestGiniGain:
                bestGiniGain = GiniGain
                bestFeature = i
                bestValue = value
    return bestFeature, bestValue

def majorityCnt(classList):
    """
    特征不够的时候选择票数最多的一类
    :param classList: 类的列表
    :return: 标签
    """
    classCount = {}
    for vote in classList:
        classCount[vote] = classCount.get(vote, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def createTree(dataSet, labels):
    """
    构造决策树
    :param dataSet: 数据集
    :param labels: 标签
    :return: 决策树（字典）
    """
    classList = [example[-1] for example in dataSet]  # 查看数据集类别多少
    if classList.count(classList[0]) == len(classList):  # 若数据集都为同一类
        return classList[0]
    if labels.count(None) == len(labels):  # 当特征值不够的时候则投票
        return majorityCnt(classList)
    bestFeat, bestVal = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    labels[bestFeat] = None
    myTree = {}
    myTree["spFeat"] = bestFeatLabel
    myTree["spVal"] = bestVal
    lSet, rSet, = splitDataSet(dataSet, bestFeat, bestVal)
    myTree["left"] = createTree(lSet, labels)
    myTree["right"] = createTree(rSet, labels)
    return myTree


if __name__ == '__main__':
    filename = "./data/loan.xlsx"
    dataSet, labels = loadDataSet(filename)
    print(dataSet)
    print(labels)
    myTree = createTree(dataSet, labels)
    print(myTree)
