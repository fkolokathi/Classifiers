import math

from logistic_regrassion.Loader import Loader


class Logistic_Regression(object):

    def _init_(self):
        self.n = 0.01
    '''
    with w, x be vectors it computes w*x.
    however because of the specific problem the computation performed is:
    x[0]*w[1] + x[1]*w[2] +...+ x[-2]*w[-1]
    ---> w[0] is always multiplied by 1
    ---> x[-1] is the response and therefore is not used for the calculations
    '''
    def product(self, w, x):

        prod = w[0]
        for i in range(len(x)):
            prod += x[i]*w[i+1]

        return prod

    def train(self, dataset, k = 0.1):

        num_of_features = len(dataset[0])
        w = [1/num_of_features]*(num_of_features + 1)

        l = 0

        while l-s < 0:
            l = s
            self.w = w
            s = 0
            for  x in dataset:

                if x[-1] == 1:
                    s += math.log2(self.positive(self.product(self.w,x)))
                else:
                    s+= math.log2(self.negative(self.product(self.w,x)))

                w[0] += self.n*(x[-1] - self.positive(self.product(self.w,x)) -2*k*w[0])
                for i in range(1,len(w)):
                    w[i] += self.n*(x[i]*(x[-1] - self.positive(self.product(self.w,x))) -2*k*w[i])

# Prosoxi!!! eite to dianisma x  periexei eite oxi to pedio ts swstis apokrisis to product(w,x) to agnoei
    def response(self, x):
        if self.positive(self.product(self.w, x)) >= 0.5: # kata simvasi to 0.5 to 8ewrw entos twn oriwn
            return 1
        else:
            return 0

    def response_all(self, data):
        responses = []
        for d in data:
            responses.append(self.response(d))

        return responses

    def positive(self, x):
        return 1.0/(1.0+math.exp(-1.0*x))

    def negative(self, x):
        return math.exp(-1.0*x)/(1.0+math.exp(-1.0*x))

