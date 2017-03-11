import numpy as np
from pylab import *
from numpy import *

def resultSort(result):
    sorting = {}
    for key, value in result.items():
        if value in sorting:
            sorting[value].append(key)
        else:
            sorting[value] = [key]
    return sorting


def confusion_matrix(actual_result, test_result, categories):

    if(len(actual_result) != len(test_result)):
        print ("the length of actual result is different from the length of test result.")
        return
    actual = resultSort(actual_result)
    test = resultSort(test_result)
    category_length = len(categories)

    confusion_matrix = np.zeros([category_length,category_length])

    for x in range(len(categories)):
        if categories[x] in test:
            for y in range(len(categories)):
                if categories[y] in actual:
                    intersection = np.intersect1d(test[categories[x]], actual[categories[y]])
                    confusion_matrix[y][x] = intersection.size

    return confusion_matrix

# the data layout is "{category: {TP: 0, FP: 0, FN: 0, TN: 0}}"
def category_data(actual_result, test_result, categories, beta = 1):

    matrix = confusion_matrix(actual_result, test_result, categories)
    total = len(actual_result)
    result = {}

    for i in range(len(categories)):
        TP = matrix[i][i]
        FP = np.sum(matrix[:][i]) - TP
        FN = np.sum(matrix[i][:]) - TP
        TN = total - TP - FP - FN
        F1Score = (1 + beta * beta) * TP / ((1 + beta * beta) * TP + beta * beta * FN + FP)
        result[categories[i]] = {"TP":TP, "FP":FP, "FN":FN, "TN":TN, "F1Score": F1Score}

    return result