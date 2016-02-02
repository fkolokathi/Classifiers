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


def train():
    file = open('training_data.csv')
    goal = "Class"  # name of goal
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
    file = open('training_data.csv')
    goal = "Class"  # name of goal
    data = []
    for line in file:
        line = line.strip("\r\n")
        data.append(
            line.split(','))  # to data periexei upolistes opou h kathemia periexei ta values kathe grammhs tou file
    attributes_names = data[0]
    return attributes_names


def test():
    o = open("D:/python_projects/Classifiers/test_result.csv", 'w', newline="\r\n")
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
                # print ("can't process input %s" % count)
                result = "?"
                break
        # print ("entry%s = %s" % (count, result))
        lis = entry
        lis.pop()  #the last element of list entry is " " because of the last comma that every tuple has (sunny,cool,high,TRUE,) in weather.csv file
        lis.append(result)
        length=len(lis) - 1
        i= 0
        for item in lis:
            if i==0:
                o.write(item)
                i = i + 1
            elif i != 0 and i != length:
                o.write(',' + item)
                i = i + 1
            else:  # last item(response)
                o.write(',' + item)
        o.write('\n')
   o.close()
