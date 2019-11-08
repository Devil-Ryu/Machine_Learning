from math import log
import operator
import os
# os.environ["PATH"] += os.pathsep + 'D:/graphviz-2.38/bin'

def calShannoEnt(dataSet):
    """
    计算香农熵
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
    shannoEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannoEnt -= prob * log(prob, 2)
    return shannoEnt

def splitDataSet(dataSet, axis, value):
    """
    划分数据集
    :param dataSet:待划分数据集
    :param axis: 划分数据集的特征
    :param value: 需返回的特征的值
    :return:
    """
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    """
    选择用于分割数据集的最好的特征
    :param dataSet: 数据集
    :return: 最好的特征的序号
    """
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calShannoEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = - 1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calShannoEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

def majorityCnt(classList):
    """
    特征不够的时候选择票数最多的一类
    :param classList: 类的列表
    :return: 标签
    """
    classCount = {}
    for vote in classList:
        classCount[vote] += classCount.get(vote, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def createTree(dataSet, labels):
    """
    构造决策树
    :param dataSet: 数据集
    :param labels: 标签
    :return: 决策树（字典）
    """
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree

def storeTree(inputTree, filename):
    """
    储存树
    :param inputTree: 决策树(字典)
    :param filename: 保存的文件名称
    :return: 无返回
    """
    import pickle
    fw = open(filename, 'wb')
    pickle.dump(inputTree, fw)
    fw.close()
    print("Decision tree has been stored into file '%s'" % filename)

def grabTree(filename):
    import pickle
    fr = open(filename, 'rb')
    return pickle.load(fr)

if __name__ == '__main__':
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    myTree = createTree(dataSet, labels)
    print(myTree)

    # 测试储存分类器
    storeTree(myTree, "myTree.txt")
    newTree = grabTree("myTree.txt")
    print(newTree)