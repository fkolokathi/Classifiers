


#accuracy=(#correct_responses)/(#test_tuples)
def accuracy():
    correct_responses = 0
    total = 0
    file1 = open('test_result.txt')
    for t1 in file1:
        file2 = open('WeatherTraining.csv')
        i=1
        for t2 in file2:
            if i!=1:#dioti h prwth grammh tou weatherTraining periexei ta onomata twn attributes
                if t1==t2:
                    correct_responses += 1
            i=i+1
        total += 1
    if (total) == 0:
        raise ValueError("Empty testset!")
    return correct_responses / float(total)
    