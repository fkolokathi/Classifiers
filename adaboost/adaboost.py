import math

import Loader


def train(dataset, file):
    data = Loader.load_dataset(file)



def adaboost(dataset, L, M):
    # dataset: tuples of xi training examples with the proper yi response
    # L: basic learning algorithm
    # M: number of iterations
    w = []  # vector of the weights of examples
    N = len(dataset.get_examples)
    w = [1. / N] * N  # initilize all the weights as 1/N
    h = []  # vector to insert M hypotheses we learn
    z = []  # vector to insert the weights of the M hypotheses

    # algorithm
    for m in range(1, M):
        h[m] = L(dataset, w)  # learn a new hypothesis (new commission member)
        error = 0
        for j in range(N):
            # calculate the total error of the new hypothesis
            # the sum of w weights of the examples is 1
            if h[m].predict(dataset[j]) != dataset[j]:
                error += w[j]
        for j in range(N):
            # for error < 0.5, the weight of the correctly classified examples decreases
            if h[m].predict(dataset[j]) == dataset[j]:
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
    views = dict()
    for v, w in zip(hypos, weights):
        views[v] += w
    return max(views.keys(), key=views.get)


class Hypothesis:
    def predict(example):
        pass
