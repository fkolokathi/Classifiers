'''
loads a csv file as a dataset.
the file consists of number values, either integer of floating point, representing each feature
'''


def load_dataset(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()

    dataset = []
    for line in lines:
        attributes = line.split(sep=',')
        data = []
        for a in attributes:
            a.strip()
            try:
                attr = float(a)
            except ValueError:
                try:
                    attr = int(a)  # euxomai na ka
                except ValueError:
                    attr = a
            data.append(attr)
        dataset.append(data)
    return dataset


def get_feature_values(data):
    feature = [[]] * len(data[0])  # isws to teleutaio na einai to response...apla to agnoneis
    for d in data:
        for i in range(len(d)):
            if d[i] not in feature[i]:
                feature[i].append(d[i])
    return feature


'''
kanei to e3is: gia ka8e feature kai gia ka8e pi8ani timi tou feature a8roizei posa paradeigmata einai se ka8e katigoria
'''


def get_values_counts(data, feature_values, categories):
    '''
    categories ---> a list of the possible categories
    '''
    counter = []
    for feature in feature_values:
        counter.append(dict.fromkeys(feature, dict.fromkeys(categories, 0)))
    for d in data:
        for i in range(len(d) - 1):  # to d[-1] einai i apokrisi
            counter[i].get(d[i])[d[-1]] += 1
    return counter
