import math


def adaboost(examples, L, M):
    # examples: a tuple of xi training examples with the proper yi response
    # L: basic learning algorithm
    # M: number of iterations
    w = []  # vector of the weights of examples
    N = len(examples)
    for i in range(N):  # initiliaze all the weights as 1/N
        w.append(1. / N)
    h = []  # vector to insert M hypotheses we learn
    z = []  # vector to insert the weights of the M hypotheses

    # algorithm
    for m in range(1, M):
        h[m] = L(examples, w)  # learn a new hypothesis (new commission member)
        error = 0
        for j in range(N):
            # calculate the total error of the new hypothesis
            # the sum of w weights of the examples is 1
            if h[m].get_response(examples[j][0]) != examples[j][1]:
                error += w[j]
        for j in range(N):
            # for error < 0.5, the weight of the correctly classified examples decreases
            if h[m].get_response(examples[j][0]) == examples[j][1]:
                w[j] = w[j] * error / (1 - error)
        w = normalize(w)  # so that the sum is 1 again
        z[m] = math.log((1 - error) / error)  # give more weight to the good hypothesis
    # this log is a natural log
    return weighted_majority(h, z)


def normalize(weights):
    # a simple normalization function that divides each weight by the total sum
    # leading to a final sum of 1
    S = sum(weights)
    newW = [w / S for w in weights]
    return newW


def weighted_majority(hypos, weights):
    views = [h * w for h, w in zip(hypos, weights)]  # a vector of votes for each hypothesis
    return max(views)


class Hypothesis:
    def get_response(example):
        pass
