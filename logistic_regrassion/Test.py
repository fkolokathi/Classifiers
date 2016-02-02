import math

from logistic_regrassion.Loader import Loader
from logistic_regrassion.logistic_regression import LogisticRegression


def training_results():
    train = 0.6
    validate = 0.2
    test = 0.2

    lg = LogisticRegression()

    data_file = 'dermatology.csv'
    dataset = Loader.load_dataset(filename=data_file)
    print(dataset)
    training_data = dataset[:math.floor(train * len(dataset)) ]

    validating_data = dataset[math.floor(train * len(dataset)): math.floor(validate * len(dataset))]

    test_data = dataset[math.floor(validate * len(dataset)):]

    z = []
    for d in validating_data:
        z.append(d[-1])

    k = [0, 1, 5, 10]
    max_ac = 0
    best = 0
    for i in range(len(k)):
        lg.train(training_data, k[i])
        metrics = get_metrics(get_results(lg.response_all(validating_data), z))
        if metrics[0] > max_ac:
            max_ac = metrics[0]
            best = i


    lg.train(dataset=training_data, k = k[best])

    y = []
    for d in test_data:
        y.append(d[-1])

    lg.train(dataset=training_data)
    x = []
    for d in training_data:
        x.append(d[-1])

    measures_for_train  = get_metrics(get_results(lg.response_all(training_data), x))
    measures_for_test = get_metrics(get_results(lg.response_all(test_data), y))

    print("*******Training data*******"+str_metrics(measures_for_train))
    print("*******Test data*******"+str_metrics(measures_for_test))


'''
return an array of the form
+---------+
| tp | fp |
+----+----+
| tn | fn |
+---------+

cr ----> correct response
r  ----> response
'''


def get_results(cr, r):

    tp = 0
    fp = 0
    tn = 0
    fn = 0

    for i in range(len(cr)):
        if cr[i] == 1:
            if r[i] == 1:
                tp += 1
            else:
                fn += 1
        else:
            if r[i] == 0:
                tn += 1
            else:
                fp += 1

    return [[tp, fp], [tn, fn]]

'''
returns a list of the form [accuracy, precision, recall, f-measure]
'''

def get_metrics(results):

    tp = results[0][0]
    tn = results[1][0]
    fp = results[0][1]
    fn = results[1][1]

    # accuracy
    metrics[0] = (tp + tn)/(tp + tn + fp + fn)
    # precision
    metrics[1] = tp/(tp+fp)
    # recall
    metrics[2] = tp/(tp+fn)
    # f-measure
    metrics[3] = (2*mertics[1]*metrics[2])/(metrics[1]+metrics[2])

    return metrics

def str_metrics(metrics):
    return 'accuracy: '+metrics[0]+'\nprecision: '+metrics[1]+'\nrecall: '+metrics[2]+'\nf-measure: '+metrics[3]


if __name__ == "__main__":
    training_results()
