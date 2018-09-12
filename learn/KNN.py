import numpy as np
from math import sqrt
import operator as opt


def test_data(dataset):
    maxVals = dataset.max(axis=0)
    minVals = dataset.min(axis=0)
    ranges = maxVals-minVals
    retdata = (dataset - minVals)/ranges
    return retdata, ranges, minVals


def knn(dataset, labels, test_data, k):
    distSquareMat = (dataset - test_data)**2
    distSquareSums = distSquareMat.sum(axis=1)
    distances = distSquareMat ** 0.5
    sortedindices = distances.argsort()
    indices = sortedindices[:k]
    labelCount = {}
    for i in range(indices.shape[0]):
        label = labels[i]
        labelCount[label] = labelCount.get(label, 0)+1
    sortedCount = sorted(labelCount.items(), key=opt.itemgetter(1), reverse=True)
    return sortedCount[0][0]


if __name__ == "__main__":
    dataset = np.array([[2, 3], [6, 8]])
    test_dataSet, ranges, minVals = test_data(dataset)
    labels = ["a", "b"]
    test_Data = np.array([3.9, 5.5])
    normtest_data = (test_Data - minVals) / ranges
    result = knn(test_dataSet, labels, normtest_data, 1)
    print(result)


