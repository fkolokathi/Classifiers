import main
import Id3_train
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D
import pylab as py
import math

#accuracy=(#correct_responses)/(#test_tuples) or (tp + tn)/(tp + tn + fp + fn)
def accuracy():
    correct_responses = 0
    total = 0
    file1 = open('test_result.csv')
    lines1=file1.readlines()
    file2 = open('validation_data.csv')
    lines2=file2.readlines()
    length=len(lines2)
    i=0
    while (i<length):
        if lines1[i].rstrip('\n')==lines2[i].rstrip('\n'):
            correct_responses += 1
        i+=1
        total+=1
    if (total) == 0:
        raise ValueError("Empty testset!")
    return correct_responses / float(total)



#This function calculates the values of tp(true positive),fp(false positive) and fn(false negative) for a particular response.This response
#represents the positive value.Depending on truepos_inst,falsepos_inst and falseneg_inst values of each test instance,we increase the values of tp,fp,fn 
def metric_parameters(response):
    truepos_inst=0
    falsepos_inst=0
    falseneg_inst=0
    file1 = open('test_result.csv')
    lines1=file1.readlines()
    file2 = open('validation_data.csv')
    lines2=file2.readlines()
    length=len(lines2)
    i=0
    list=[]
    while (i<length):
        trainbody=lines2[i].rsplit(',', 1)[0]
        traincategory=lines2[i].rsplit(',', 1)[1]
        testbody=lines1[i].rsplit(',', 1)[0]
        testcategory=lines1[i].rsplit(',', 1)[1]
        if testbody==trainbody and testcategory.rstrip('\n')==traincategory.rstrip('\n'):
            if testcategory.rstrip('\n')==response:
                truepos_inst+=1
        elif testbody==trainbody and testcategory.rstrip('\n')!=traincategory.rstrip('\n'):
            if testcategory.rstrip('\n')==response:
                falsepos_inst+=1
            elif traincategory.rstrip('\n')==response:
                falseneg_inst+=1
        i=i+1
    list.append(truepos_inst)
    list.append(falsepos_inst)
    list.append(falseneg_inst)
    return list

#precision=tp/(tp+fp)
def precision(response):
    list=metric_parameters(response)
    if (list[0]+list[1])==0:
        raise ValueError("You cannot calculate precision because of its zero denominator!")   
    return list[0]/(list[0]+list[1])    

#recall=tp/(tp+fn)
def recall(response):    
    list=metric_parameters(response) 
    if (list[0]+list[2])==0:
        raise ValueError("You cannot calculate recall because of its zero denominator!")          
    return list[0]/(list[0]+list[2])

#f-measure=(2*precision*recall)/(precision+recall)
def f_measure(response):
    pr=precision(response)
    rec=recall(response)
    if (pr+rec)==0:
        raise ValueError("You cannot calculate f-measure because of its zero denominator!") 
    return (2*pr*rec)/(pr+rec)


def plot():
    x=[]#each element of x has a rate of training data
    y_accuracy=[]
    y_precision=[]
    y_recall=[]
    y_fmeasure=[]
    y_error_rate=[]
    rate=0.1
    while rate<=0.9:
        main.validation(rate)
        Id3_train.test()
        x.append((1-rate)*100)
        acc=accuracy()
        y_accuracy.append(acc*100)
        y_precision.append(precision("1")*100)
        y_recall.append(recall("1")*100)
        y_fmeasure.append(f_measure("1")*100)
        y_error_rate.append((1-acc)*100)
        rate=rate+0.1
    plt.subplot(1,1,1)
    plt.xlabel('% of training data')
    plt.ylabel('% for each metric')
    plt.xlim(0.0, 100.0)
    plt.ylim(0.0, 100.0)
    plt.plot(x,y_accuracy,'g',label='accuracy')
    plt.plot(x,y_precision,'b',label='precision')
    plt.plot(x,y_recall,'m',label='recall')
    plt.plot(x,y_fmeasure,'k',label='f-measure')
    plt.plot(x,y_error_rate,'r',label='error rate')
    plt.legend(bbox_to_anchor=[1.0, 0.5], loc='right',prop={'size':10}, borderaxespad=0.)
    #plt.legend(bbox_to_anchor=(1.05, 1), loc=2,prop={'size':10}, borderaxespad=0.)
    plt.show()
    