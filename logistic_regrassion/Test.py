# Dimaki Georgia 3130052
# Kolokathi Fotini 3090088
# Papatheodorou Dimitris 3130162
#########################################################

import math

from DataLoader import *
from logistic_regrassion.logistic_regression import LogisticRegression
from IG import  *

'''
a function used only to compute the metrics of the performance of logistic regression algorithm
'''
def training_results():

    best_attrs = ff()
    # witch percentage of data will take each set of data used for training, validation and testing of the algorithm
    train = 0.4
    validate = 0.3
    test = 0.3
    k_best = math.floor(0.7*len(best_attrs))

    lg = LogisticRegression()

    data_file = 'dermatology.csv'
    dtst = load_dataset(filename=data_file)

    dataset = [[]]*(len(dtst)-1)
    print(dataset)

    the_best = best_attrs[: k_best]
    print(the_best)

    for j in range(1,len(dtst)):
        for i in range(len(dtst[0])):
            if dtst[0][i] in the_best:
                dataset[j-1].append(dtst[j][i])
       #print(dataset[j-1])

    #print(dataset)

    # dataset = dataset[1:]
    # splitting the data
    training_data = dataset[:math.floor(train * len(dataset))]
    validation_data = dataset[math.floor(train * len(dataset)): math.floor(train * len(dataset)) + math.floor(validate * len(dataset))]
    test_data = dataset[ math.floor(train * len(dataset)) + math.floor(validate * len(dataset)):]

    # creating the array of validation_data responses
    z = []
    for d in validation_data:
        z.append(d[-1])

    # computing the best k using the performance of the algorithm with each value of k
    k = [0, 1, 3]
    max_ac = 0
    best = 0
    for i in range(len(k)):
        lg.train(training_data, k[i])
        metrics = get_metrics(get_results(lg.response_all(validation_data), z))
        if metrics[0] > max_ac:
            max_ac = metrics[0]
            best = i
    print ("here")

    lg.train(dataset=training_data, k=k[best])

    # creating the array of test_data responses
    y = []
    for d in test_data:
        y.append(d[-1])

    # creating the array of training_data responses
    x = []
    for d in training_data:
        x.append(d[-1])

    # computing the measures both on training data end on test data
    measures_for_train = get_metrics(get_results(lg.response_all(training_data), x))
    measures_for_test = get_metrics(get_results(lg.response_all(test_data), y))

    print("*******Training data*******\n" + str_metrics(measures_for_train))
    print("*******Test data*******\n" + str_metrics(measures_for_test))


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

    metrics = [0,0,0,0]
    # accuracy
    metrics[0] = (tp + tn) / (tp + tn + fp + fn)
    # precision
    try:
        metrics[1] = tp / (tp + fp)
    except ZeroDivisionError as z:
        metrics[1] = 'inf'
    # recall
    try:
        metrics[2] = tp / (tp + fn)
    except ZeroDivisionError as z:
        metrics[2] = 'inf'
    # f-measure
    try:
        if metrics[1] == 'inf' or metrics[2] == 'inf':
            metrics[3] == 'NA'
        else:
            metrics[3] = (2 * metrics[1] * metrics[2]) / (metrics[1] + metrics[2])
    except ZeroDivisionError as z:
        metrics = 'inf'

    return metrics

# prints the metrics
def str_metrics(metrics):
    return 'accuracy: ' + str(metrics[0]) + '\nprecision: ' + str(metrics[1]) + '\nrecall: ' + str(metrics[2]) + '\nf-measure: ' + \
           str(metrics[3])


if __name__ == "__main__":
    training_results()
