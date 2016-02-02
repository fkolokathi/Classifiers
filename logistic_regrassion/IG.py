# Dimaki Georgia 3130052
# Kolokathi Fotini 3090088
# Papatheodorou Dimitris 3130162
#########################################################

# This function calculates the information gain for a given attribute.
# data is a list with sublists each of which contain a turple,attributes is a list,goal is the name of the
# target attribute,
# attribute is the given attribute for which IG is calculated
import math
def information_gain(data, attributes, goal, attribute):
    dictionary = {}
    pos = attributes.index(attribute)
    data2 = []
    subsetEntropy = 0
    for turple in data:
        if turple[pos] in dictionary:
            dictionary[turple[pos]] += 1
        else:
            dictionary[turple[pos]] = 1
    for key in dictionary.keys():
        for entry in data:
            if entry[pos] == key:
                data2.append(entry)
        value_entropy = entropy(data2, attributes,goal)  # H(C/X=x)=-sumcP(C=c/X=x)*log(P(C=c/X=x)),x has a particular value here
        p = dictionary[key] / sum(dictionary.values())  # P(X=x)
        subsetEntropy += p * value_entropy  # sumx(P(X=x)*H(C/X=x))
    ig = entropy(data, attributes, goal) - subsetEntropy  # IG=H(C) - sumx(P(X=x)*H(C/X=x))
    return ig

#This function calculates the entropy.
#data is a list with sublists each of which contain a turple,attributes is a list,goal is the name of the target attribute
def entropy(data,attributes,goal):
    dictionary={}
    pos = attributes.index(goal)
    entropy=0
    for turple in data:
        if turple[pos] in dictionary:
            dictionary[turple[pos]] +=1
        else:
            dictionary[turple[pos]] =1
    for frequency in dictionary.values():
        p= frequency/len(data)
        entropy += p * math.log(p,2)#H(C)=-sumc(P(C=c)*log(P(c=c))
    entropy=-entropy
    return entropy


# This functions return the attribute with the maximum information gain
# data is a list with sublists each of which contain a turple,attributes is a list,goal is the name of the target
# attribute
def best_attribute(data, attributes, goal):
    if attributes == []:
        return ''
    best = attributes[0]
    max = 0
    for attr in attributes:
        if attr != attributes[-1]:
            new = information_gain(data, attributes, goal, attr)
            if new > max:
                best = attr
                max = new
    return best


def attributes_names():
   file = open('dermatology.csv')
   goal = "Class"#name of goal
   data=[]
   for line in file:
        line = line.strip("\r\n")
        data.append(line.split(','))#to data periexei upolistes opou h kathemia periexei ta values kathe grammhs tou file
   attributes_names = data[0]
   return attributes_names

#This function takes all the values of a given attribute from the data.
#data is a list with sublists each of which contain a turple,attributes is a list,attribute is given attribute
def get_attribute_values(data,attributes,attribute):
    values=[]
    if attribute == '':
        return  values
    pos=attributes.index(attribute)
    for turple in data:
        if turple[pos] not in values:
            values.append(turple[pos])
    return values

#This function returns a list which contains sublists each of which contains the turple in which best=value.Each sublist also does not contain the best attribute
#data is a list with sublists each of which contains a turple,attributes is a list,best is the given attribute with max information gain,value is a value of best attribute
def get_node_examples(data,attributes,best,value):
  list=[]
  pos= attributes.index(best)
  for turple in data:
       if (turple[pos] == value):
           newlist=[]
           #add value if it is not in best column
           for i in range(0,len(turple)):
                if(i != pos):
                    newlist.append(turple[i])
           list.append(newlist)
  return list


def df(attributes,goal,data,list):
    best=best_attribute(data,attributes,goal)
    list.append(best)
    for v in get_attribute_values(data,attributes,best):
        examples = get_node_examples(data,attributes,best,v)
        newAttr = attributes[:]
        newAttr.remove(best)
        df(newAttr,goal,examples,list)
    return list

def ff():

    goal="Class"
    attributes=attributes_names()
    file = open('dermatology.csv')
    data=[]
    for line in file:
        line = line.strip("\r\n")
        data.append(line.split(','))#to data periexei upolistes opou h kathemia periexei ta values kathe grammhs tou file
    attr_names = data[0]#H prwth grammh tou file periexei ta onomata twn attributes.
    data.remove(attr_names)#afairesh ths prwths grammhs pou periexei ta onomata twn attiributes mias kai den tha xreiastoun kata to training
    list=[]
    li=df(attributes,goal,data,list)
    return li