# Dimaki Georgia 3130052
# Kolokathi Fotini 3090088
# Papatheodorou Dimitris 3130162
#########################################################
import math


class LogisticRegression:

    '''
    n ---> the constant used for the stochastic gradient descent
    w ---> the weights calculated during training
    '''
    def __init__(self):
        self.n = 0.001
        self.w = [0] # pointless assignment

    '''
    with w, x be vectors it computes w*x.
    however because of the specific problem the computation performed is:
    x[0]*w[1] + x[1]*w[2] +...+ x[-2]*w[-1]
    ---> w[0] is always multiplied by 1
    ---> x[-1] is the response and therefore is not used for the calculations
    (however it can work both on data that contain the correct response and with those that don't)
    '''

    def product(self, w, x):
        prod = w[0]
        for i in range(1,len(w)):
            prod += x[i-1] * w[i]

        return prod

    '''
    trains the logistic regression on specific dataset with specific penalty constant k for the weights
    '''
    def train(self, dataset, k=0.1):
        print("in train w = "+str(self.w))
        num_of_features = len(dataset[0])
        w = [1 / num_of_features] * (num_of_features)
        l = -float("Inf")
        s = 0
        iteration = 1

        while abs(l-s) > 0.05 or iteration <= 2:
            l = s
            self.w = w
            print("here w = "+str(self.w))
            s = 0
            for x in dataset:
                if x[-1] == 1:
                    s += math.log2(self.positive(self.product(self.w, x)))
                else:
                    try:
                        s += math.log2(self.negative(self.product(self.w, x)))
                    except ValueError:
                        s += -float("Inf")

                w[0] += self.n * (x[-1] - self.positive(self.product(self.w, x)) - 2 * k * w[0])
                for i in range(1, len(w)):
                    w[i] += self.n * (x[i-1] * (x[-1] - self.positive(self.product(self.w, x))) - 2 * k * w[i])
            print("abs " +str(abs(l-s))+" l = "+str(l)+" s = "+str(s))
            if s != l:
                iteration += 1
        print("out train "+str(iteration))

    '''
    classifies the data x
    '''
    def response(self, x):
        if self.positive(self.product(self.w, x)) >= 0.5:
            result = 1
        else:
            result = 0
        return result

    '''
    classifies all data in the 'data' array
    '''
    def response_all(self, data):
        responses = []
        for d in data:
            responses.append(self.response(d))
        return responses

    '''
    it computes the probability that the category of x is the positive category (1)
    '''
    def positive(self, x):
        return 1.0 / (1.0 + math.exp(-1.0 * x))

    '''
    it computes the probability that the category of x is the negative category (0)
    '''
    def negative(self, x):
        return 1.0 - self.positive(x)
