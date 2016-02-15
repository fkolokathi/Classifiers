import Id3_train
import Evaluation
import math


#This function seperates tha data in 90% training data(training_data.csv) and in 10% validation data(validation_data.csv). 
def validation(rate):
    f=open('dermatology.csv','r')
    lines=f.readlines()
    validationlines = math.modf(len(lines)*rate)[1]
    saved =lines
    f1=open('validation_data.csv', 'w')
    f2= open('for_test.csv', 'w')#this file does not contain the response attribute of each instance
    list1=lines[(len(lines)-int(validationlines)):len(lines)]
    i=0
    for l1 in list1:
        i=i+1
        if i==len(list1):
            f1.writelines(l1.rstrip('\n'))
            f2.writelines(l1.rsplit(',', 1)[0]+',')
        else:
            f1.writelines(l1)
            f2.writelines(l1.rsplit(',', 1)[0]+','+'\n')
    f3=open('training_data.csv','w')
    list2=saved[0:(len(lines)-int(validationlines))]
    j=0
    for l2 in list2:
        j=j+1
        if j==len(list2):
            f3.writelines(l2.rstrip('\n'))
        else:
            f3.writelines(l2)
    f1.close()
    f2.close()
    f3.close()



if __name__ == '__main__':
    validation(0.1)
    print ("Id3 algorithm performance(90%-training data,10%-validation data): \n")
    Id3_train.test()
    print ("Accuracy: %f" % Evaluation.accuracy())
    print ("Precision: %f" % Evaluation.precision("1"))
    print ("Recall: %f" % Evaluation.recall("1"))
    print ("F-measure: %f" % Evaluation.f_measure("1"))
    Evaluation.plot()
    print ("-----------------------------------------------")