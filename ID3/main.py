import math

import ID3.Evaluation as Evaluation
import ID3.Id3_train as Id3_train


# This function separates tha data in 90% training data(WeatherTraining.csv) and in 10%
#  validation data(validation_data.csv).
def validation():
    f = open('dermatology.csv', 'r')
    lines = f.readlines()
    validationlines = math.modf(len(lines) * 0.1)[1]
    saved = lines
    f1 = open('validation_data.csv', 'w')
    f2 = open('for_test.csv', 'w')  # this file does not contain the response attribute of each instance
    list1 = lines[(len(lines) - int(validationlines)):len(lines)]
    i = 0
    for l1 in list1:
        i = i + 1
        if i == len(list1):
            f1.writelines(l1.rstrip('\n'))
            f2.writelines(l1.rsplit(',', 1)[0] + ',')
        else:
            f1.writelines(l1)
            f2.writelines(l1.rsplit(',', 1)[0] + ',' + '\n')
    f3 = open('training_data.csv', 'w')
    list2 = saved[0:(len(lines) - int(validationlines))]
    j = 0
    for l2 in list2:
        j = j + 1
        if j == len(list2):
            f3.writelines(l2.rstrip('\n'))
        else:
            f3.writelines(l2)
    f1.close()
    f2.close()
    f3.close()


# NA THUMITHW NA XWRISW TA VALIDATION ME TA TRAIN KATA 0.1
if __name__ == '__main__':
    validation()
    print("Id3 algorithm performance: \n")
    Id3_train.test()
    print("Accuracy: %f" % Evaluation.accuracy())
    print("Precision: %f" % Evaluation.precision("1"))
    print("Recall: %f" % Evaluation.recall("1"))
    print("F-measure: %f" % Evaluation.f_measure("1"))
    print("-----------------------------------------------")
