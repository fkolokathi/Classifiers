import math
from copy import deepcopy

import DataLoader


def train(dataset, file, iterNum):
    data = DataLoader.load_dataset(file)
    adaboost(data, decision_stump, iterNum)


def decision_stump(dataset, weights):
    features = DataLoader.transpose(dataset)

    def class_inspect(data=features):
        classes = []
        for f in data[-1]:
            if f not in classes:
                classes.append(f)
        if len(classes) > 2:
            mean = sum(classes) / len(classes)
            for c in range(0, len(data[-1])):
                if data[-1][c] < mean:
                    data[-1][c] = 0
                else:
                    data[-1][c] = 1
                    # if responses are not binary, we "binarize" them, because this is binary decision stump
                    # this is done by classifying the multiple classes into two clusters

    def split(data, pos):  # a simple mean split
        mean = sum(data[pos]) / len(data[pos])
        for i in range(data[pos]):
            if i < mean:
                data[pos][-1] = 0
            else:
                data[pos][-1] = 1
        return data

    class_inspect(features)
    heaviest, position = weighted_majority(features[-1], weights)
    split_t = split(deepcopy(features), position)
    return DataLoader.transpose(split_t)


def adaboost(data, L, M):
    # data: xi training examples with the proper yi response
    # data[i] array of i-th example, data[i][-1] response of i-th example
    # L: a weak learning algorithm (decision stump)
    # M: number of iterations
    w = []  # vector of the weights of examples
    N = len(data)
    w = [1. / N] * N  # initialize all the weights as 1/N
    h = []  # vector to insert M hypotheses we learn
    z = []  # vector to insert the weights of the M hypotheses

    # algorithm
    for m in range(1, M):
        h[m] = L(data, w)  # learn a new hypothesis (new commission member)
        error = 0
        for j in range(N):
            # calculate the total error of the new hypothesis
            # the sum of w weights of the examples is 1
            if h[m][j][-1] != data[j][-1]:
                error += w[j]
        for j in range(N):
            # for error < 0.5, the weight of the correctly classified examples decreases
            if h[m][j][-1] == data[j][-1]:
                if error == 1:  # avoid division by 0
                    error += 0.000000001
                w[j] *= error / (1. - error)
        w = normalize(w)  # so that the sum is 1 again
        z[m] = math.log((1. - error) / error)  # give more weight to the good hypothesis
    # this log is a natural log
    return weighted_majority(h, z)


def normalize(weights):
    # a simple normalization function that divides each weight by the total sum
    # leading to a final sum of 1
    S = sum(weights)
    newW = [w / S for w in weights]
    return newW


def weighted_majority(hypos, weights):
    i = 0
    max = hypos[i]
    maxw = weights[i]
    for i in range(1, len(hypos)):
        if weights[i] > maxw:
            maxw = weights[i]
            max = hypos[i]
    return max, i - 1


if __name__ == '__main__':
    pass
    # TODO test, validation, metrics
