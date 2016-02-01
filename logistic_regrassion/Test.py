from logistic_regrassion.logistic_regression import Logistic_Regression
from logistic_regrassion.Loader import Loader
import math

def training_results():

    train = 0.6
    validate = 0.2
    test = 0.2

    lg = Logistic_Regression()

    data_file = 'deramtology.csv'
    dataset = Loader.load_dataset(filename=data_file)

    training_data = dataset[:math.floor(train*len(dataset)) ]

    validating_data = dataset[math.floor(train*len(dataset)) : math.floor(validate*len(dataset))]

    test_data = dataset[math.floor(validate*len(dataset)) :]

    y = []
    for d in test_data:
        y.append(d[-1])


    lg.train(dataset=training_data)


    test_data = Loader.load_dataset(filename=test_data_file)
    responses = lg.response_all(data=test_data)

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

    return [[tp, fp],[tn, fn]]



if __name__ == "__main__":
    training_results()