import math

import DataLoader
import adaboost


def training_results():
    train = 0.8
    test = 0.2

    data_file = 'dermatology.csv'
    dataset = DataLoader.load_dataset(filename=data_file)

    training_data = dataset[:math.floor(train * len(dataset))]
    test_data = dataset[math.floor(test * len(dataset)):]

    trained = adaboost.train(training_data, 50)

    def get_responses(data):
        responses = []
        for r in data:
            responses.append(r[-1])
        return responses

    train_metrics = get_metrics(get_results(get_responses(trained), get_responses(training_data)))
    test_metrics = get_metrics(get_results(get_responses(trained), get_responses(training_data)))

    print("*******Training data*******" + str_metrics(train_metrics))
    print("*******Test data*******" + str_metrics(test_metrics))


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
    returned = [[tp, fp], [tn, fn]]
    print(returned)
    return returned


'''
returns a list of the form [accuracy, precision, recall, f-measure]
'''


def get_metrics(results):
    tp = results[0][0]
    tn = results[1][0]
    fp = results[0][1]
    fn = results[1][1]

    metrics = []
    # accuracy
    metrics[0] = (tp + tn) / (tp + tn + fp + fn)
    # precision
    metrics[1] = tp / (tp + fp)
    # recall
    metrics[2] = tp / (tp + fn)
    # f-measure
    metrics[3] = (2 * metrics[1] * metrics[2]) / (metrics[1] + metrics[2])

    return metrics


def str_metrics(metrics):
    return 'accuracy: ' + metrics[0] + '\nprecision: ' + metrics[1] + '\nrecall: ' + metrics[2] + '\nf-measure: ' + \
           metrics[3]


if __name__ == "__main__":
    training_results()
