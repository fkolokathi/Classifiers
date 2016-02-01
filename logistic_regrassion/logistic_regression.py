import math


class Logistic_Regression(object):
    # constants

    # sta8era gia ton periorismo twn varwn w
    k = 0.1

    # mikri sta8era tou kanona enimerwsis varwn
    n = 0.01
    '''
    loads a csv file as a dataset.
    the file consists of number values, either integer of floating point, representing each feature
    '''

    def load_dataset(self, filename):
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        # 8ewrw oti pairnw csv arxeia sta opoia ka8e paradeigma vrisketai se diaforetiki grammi
        # kai oti t paradeigmata apotelountai apo katigorikes idiotites
        # epipleon ola ta paradeigmata exoun ton idio ari8mo idiotitwn ek twn opoiwn i teleutaia einai i apokrisi


        # dimiourgw enan pinaka pinakwn me tis pi8anes times ka8e attribute.
        # parallila dimiourgw kai t dianismata twn paradeigmatwn.
        dataset = []
        for line in lines:
            attributes = line.split(sep=',')
            data = []
            for a in attributes:
                a.strip()
                a = float(a) if '.' in a else int(a)  # euxomai na kanei apla tn douleia tou <3
                data.append(a)

            dataset.append(data)

        return dataset

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
            prod += x[i] * w[i + 1]

        return prod

    @staticmethod
    def train(self, filename):

        dataset = self.load_dataset(filename)

        num_of_features = len(dataset[0])
        w = [1 / num_of_features] * (num_of_features + 1)
        k = 0.1  # prepei na ginei ki auto sta8era
        n = 0.01  # prepe na to valw ws sta8era e3w apo tn sinartisi

        l = 0

        while l - s < 0:
            l = s
            self.w = w
            s = 0
            for x in dataset:

                if x[-1] == 1:
                    s += math.log2(self.positive(self.product(w, x)))
                else:
                    s += math.log2(self.negative(self.product(w, x)))

                w[0] += n * (x[-1] - self.positive(self.product(w, x)) - 2 * k * w[0])
                for i in range(1, len(w)):
                    w[i] += n * (x[i] * (x[-1] - self.positive(self.product(w, x))) - 2 * k * w[i])

                    # Prosoxi!!! eite to dianisma x  periexei eite oxi to pedio ts swstis apokrisis to product(w,x) to agnoei

    @staticmethod
    def response(self, x):
        if self.positive(self.product(self.w, x)) >= 0.5:  # kata simvasi to 0.5 to 8ewrw entos twn oriwn
            return 1
        else:
            return 0

    @staticmethod
    def response_all(self, data_file):
        data = self.load_dataset(data_file)
        responses = []
        for d in data:
            responses.append(self.response(d))

        return responses

    def positive(self, k):
        return 1.0 / (1.0 + math.exp(-1.0 * k))

    def negative(self, k):
        return math.exp(-1.0 * k) / (1.0 + math.exp(-1.0 * k))


def training_results():
    training_data_file = ''
    Logistic_Regression.train(training_data_file)

    test_data_file = ''
    responses = Logistic_Regression.response_all(test_data_file)


if __name__ == "__main__":
    training_results()
