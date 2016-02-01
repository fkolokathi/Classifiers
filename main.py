import math

import Evaluation
import Id3


class Node:
    value = ""
    children = []

    def __init__(self, v, dictionary):
        self.setValue(v)
        self.genChildren(dictionary)

    def __str__(self):
        return str(self.value)

    def setValue(self, v):
        self.value = v

    def genChildren(self, dictionary):
        if (isinstance(dictionary, dict)):
            self.children = list(dictionary.keys())


# This function seperates tha data in 90% training data(WeatherTraining.csv) and in 10% validation data(validation_data.csv).
def validation():
    f = open('training_data.csv', 'r')
    lines = f.readlines()
    validationlines = math.modf(len(lines) * 0.4)[1]
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
    f3 = open('WeatherTraining.csv', 'w')
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


def train():
    file = open('WeatherTraining.csv')
    goal = "play"  # name of goal
    data = []
    for line in file:
        line = line.strip("\r\n")
        data.append(
            line.split(','))  # to data periexei upolistes opou h kathemia periexei ta values kathe grammhs tou file
    attributes_names = data[
        0]  # H prwth grammh tou file periexei ta onomata twn attributes.---------->Ta exw ektypwsei pairnei ta onomata twn attributes mia xara
    data.remove(
        attributes_names)  # afairesh ths prwths grammhs pou periexei ta onomata twn attiributes mias kai den tha xreiastoun kata to training
    # Run ID3
    tree = Id3.id3(data, attributes_names, goal)
    return tree


def attributes_names():  # ------->Kai edw swsta tha ta pairnei.einai akrivws to idio me panw
    file = open('WeatherTraining.csv')
    goal = "class"  # name of goal
    data = []
    for line in file:
        line = line.strip("\r\n")
        data.append(
            line.split(','))  # to data periexei upolistes opou h kathemia periexei ta values kathe grammhs tou file
    attributes_names = data[0]
    return attributes_names


def test():
    o = open("D:/python_projects/Classifiers/test_result.txt", 'w', newline="\r\n")
    data = []
    tree = train()
    attributes = attributes_names()
    f = open('for_test.csv')
    for line in f:
        line = line.strip("\r\n")
        data.append(
            (line.split(',')))  # to data periexei upolistes opou h kathemia periexei ta values kathe grammhs tou file
    ###########################################
    count = 0
    for entry in data:
        count += 1
        dictionary = tree.copy()
        result = ""
        while (isinstance(dictionary, dict)):
            root = Node(list(dictionary.keys())[0], dictionary[list(dictionary.keys())[0]])
            dictionary = dictionary[list(dictionary.keys())[0]]
            index = attributes.index(root.value)
            val = entry[index]
            if val in list(dictionary.keys()):
                child = Node(val, dictionary[val])
                result = dictionary[val]
                dictionary = dictionary[val]
            else:
                print("can't process input %s" % count)
                result = "?"
                break
        print("entry%s = %s" % (count, result))
        lis = entry
        lis.pop()  # the last element of list entry is " " because of the last comma that every tuple has (sunny,cool,high,TRUE,) in weather.csv file
        lis.append(result)
        length = len(lis) - 1
        i = 0
        for item in lis:
            if i == 0:
                o.write(item)
                i = i + 1
            elif i != 0 and i != length:
                o.write(',' + item)
                i = i + 1
            else:  # last item(response)
                o.write(',' + item)
        o.write('\n')
    o.close()


# NA THUMITHW NA XWRISW TA VALIDATION ME TA TRAIN KATA 0.1
if __name__ == '__main__':
    validation()
    test()
    print(Evaluation.accuracy())
    print(Evaluation.precision("yes"))
    print(Evaluation.recall("yes"))
    print(Evaluation.f_measure("yes"))
