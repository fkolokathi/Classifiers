import math


# This function finds the most common value for the goal attribute.
# data is a list with sublists each of which contain a turple,attributes is a list,goal is the name of
# the target attribute
def goal_majority(data, attributes, goal):
    dictionary = {}
    pos = attributes.index(goal)
    for turple in data:
        if turple[pos] in dictionary:
            dictionary[turple[pos]] += 1
        else:
            dictionary[turple[pos]] = 1
    max = 0
    maxkey = ""
    for key in dictionary:
        if dictionary[key] > max:
            max = dictionary[key]
            maxkey = key
    return maxkey


# This function takes all the values of a given attribute from the data.
# data is a list with sublists each of which contain a turple,attributes is a list,attribute is given attribute
def get_attribute_values(data, attributes, attribute):
    values = []
    pos = attributes.index(attribute)
    for turple in data:
        if turple[pos] not in values:
            values.append(turple[pos])
    return values


# This function calculates the entropy.
# data is a list with sublists each of which contain a turple,attributes is a list,goal is the name of
# the target attribute
def entropy(data, attributes, goal):
    dictionary = {}
    pos = attributes.index(goal)
    entropy = 0
    for turple in data:
        if turple[pos] in dictionary:
            dictionary[turple[pos]] += 1
        else:
            dictionary[turple[pos]] = 1
    for frequency in dictionary.values():
        p = frequency / len(data)
        entropy += p * math.log(p, 2)  # H(C)=-sumc(P(C=c)*log(P(c=c))
    entropy = -entropy
    return entropy


# This function calculates the information gain for a given attribute.
# data is a list with sublists each of which contain a turple,attributes is a list,goal is the name of the
# target attribute,
# attribute is the given attribute for which IG is calculated
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
        value_entropy = entropy(data2, attributes,
                                goal)  # H(C/X=x)=-sumcP(C=c/X=x)*log(P(C=c/X=x)),x has a particular value here
        p = dictionary[key] / sum(dictionary.values())  # P(X=x)
        subsetEntropy += p * value_entropy  # sumx(P(X=x)*H(C/X=x))
    ig = entropy(data, attributes, goal) - subsetEntropy  # IG=H(C) - sumx(P(X=x)*H(C/X=x))
    return ig


# This functions return the attribute with the maximum information gain
# data is a list with sublists each of which contain a turple,attributes is a list,goal is the name of the target
# attribute
def best_attribute(data, attributes, goal):
    best = attributes[0]
    max = 0
    for attr in attributes:
        if attr != attributes[-1]:
            new = information_gain(data, attributes, goal, attr)
            if new > max:
                best = attr
                max = new
    return best


# This function returns a list which contains sublists each of which contains the turple in which best=value.
# Each sublist also does not contain the best attribute data is a list with sublists each of which contains a turple,
# attributes is a list,best is the given attribute with max information gain,value is a value of best attribute
def get_node_examples(data, attributes, best, value):
    list = []
    pos = attributes.index(best)
    for turple in data:
        if turple[pos] == value:
            newlist = []
            # add value if it is not in best column
            for i in range(0, len(turple)):
                if i != pos:
                    newlist.append(turple[i])
            list.append(newlist)
    return list


# ID3 algorithm
# data is a list with sublists each of which contain a turple,attributes is a list with the names of the attributes,
# goal is the name of the target attribute
def id3(data, attributes, goal):
    data = data[:]
    default = goal_majority(data, attributes, goal)  # plurarity value
    values = []
    values = get_attribute_values(data, attributes, goal)
    if (len(data) == 0) or (len(attributes) - 1) <= 0:  # attributes may conatin only the goal item
        return default
    elif len(values) == 1:  # check if all data belong to one goal value
        return values[0]
    # elif values.count(values[0])==len(values):
    #    return vals[0]
    else:
        best = best_attribute(data, attributes, goal)  # name
        tree = {best: {}}
        for v in get_attribute_values(data, attributes, best):
            examples = get_node_examples(data, attributes, best, v)
            newAttr = attributes[:]
            newAttr.remove(best)
            subtree = id3(examples, newAttr, goal)
            # Add the new subtree to the empty dictionary object in our new
            # tree/node we just created.
            tree[best][
                v] = subtree  # Me to tree[best] pairnoume to eswteriko {} dhladh ena dictionary.Gia na prosthesoume ena
            #  stoixeio v se ayto kanoume tree[best][v]
            # Me tis sunexeis anadromes tha ftiaxtei arxika ena dictionary pou mesa tha exei eswteriko dictionary
            # sto opoio ta keys tha einai ta padia tou root ktl.
            # Sto paradeigma twn diafaneiwn sel 15 to antistoixo dictionary tha einai:
            # {eisodhma: {upshlo: {pantremenos:{nai:dwse,oxi:mh dwseis}} ,xamhlo:mh dwseis} }
        return tree
