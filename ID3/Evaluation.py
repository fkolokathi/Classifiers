# accuracy=(#correct_responses)/(#test_tuples) or (tp + tn)/(tp + tn + fp + fn)
def accuracy():
    correct_responses = 0
    total = 0
    file1 = open('test_result.csv')
    lines1 = file1.readlines()
    file2 = open('validation_data.csv')
    lines2 = file2.readlines()
    length = len(lines2)
    i = 0
    while (i < length):
        if lines1[i].rstrip('\n') == lines2[i].rstrip('\n'):
            correct_responses += 1
        i += 1
        total += 1
    if (total) == 0:
        raise ValueError("Empty testset!")
    return correct_responses / float(total)


# This function calculates the values of tp(true positive),fp(false positive) and fn(false negative) for a particular response.This response
# represents the positive value.Depending on truepos_inst,falsepos_inst and falseneg_inst values of each test instance,we increase the values of tp,fp,fn
def metric_parameters(response):
    truepos_inst = 0
    falsepos_inst = 0
    falseneg_inst = 0
    file1 = open('test_result.csv')
    lines1 = file1.readlines()
    file2 = open('validation_data.csv')
    lines2 = file2.readlines()
    length = len(lines2)
    i = 0
    list = []
    while (i < length):
        trainbody = lines2[i].rsplit(',', 1)[0]
        traincategory = lines2[i].rsplit(',', 1)[1]
        testbody = lines1[i].rsplit(',', 1)[0]
        testcategory = lines1[i].rsplit(',', 1)[1]
        # print (i)
        # print (testcategory.rstrip('\n'))
        # print (traincategory.rstrip('\n'))
        if testbody == trainbody and testcategory.rstrip('\n') == traincategory.rstrip('\n'):
            if testcategory.rstrip('\n') == response:
                # print ("tp")
                # print (i)
                truepos_inst += 1
        elif testbody == trainbody and testcategory.rstrip('\n') != traincategory.rstrip('\n'):
            if testcategory.rstrip('\n') == response:
                # print ("fp")
                # print (i)
                falsepos_inst += 1
            elif traincategory.rstrip('\n') == response:
                # print ("fn")
                # print (i)
                falseneg_inst += 1
        i = i + 1
    list.append(truepos_inst)
    list.append(falsepos_inst)
    list.append(falseneg_inst)
    return list


# precision=tp/(tp+fp)
def precision(response):
    list = metric_parameters(response)
    if (list[0] + list[1]) == 0:
        raise ValueError("You cannot calculate precision because of its zero denominator!")
    return list[0] / (list[0] + list[1])


# recall=tp/(tp+fn)
def recall(response):
    list = metric_parameters(response)
    if (list[0] + list[2]) == 0:
        raise ValueError("You cannot calculate recall because of its zero denominator!")
    return list[0] / (list[0] + list[2])


# f-measure=(2*precision*recall)/(precision+recall)
def f_measure(response):
    pr = precision(response)
    rec = recall(response)
    if (pr + rec) == 0:
        raise ValueError("You cannot calculate f-measure because of its zero denominator!")
    return (2 * pr * rec) / (pr + rec)
