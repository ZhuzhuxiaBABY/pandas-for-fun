'''
Name: Jiahui Zhu
Date: 6/12/2019
'''
from numpy import *
from AprioriSimple import *
from AprioriComplete import *

def generateRules(L, supportData, minConf=0.7):  # supportData is a dict coming from scanD
    bigRuleList = []
    for i in range(1, len(L)):  # only get the sets with two or more items
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]
            if (i > 1):
                rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)
            else:
                calcConf(freqSet, H1, supportData, bigRuleList, minConf)
    return bigRuleList


def calcConf(freqSet, H, supportData, brl, minConf=0.7):
    prunedH = []  # create new list to return
    for conseq in H:
        conf = supportData[freqSet] / supportData[freqSet - conseq]  # calc confidence
        if conf >= minConf:
            print(freqSet - conseq, '-->', conseq, 'conf:', conf)
            brl.append((freqSet - conseq, conseq, conf))
            prunedH.append(conseq)
    return prunedH


def rulesFromConseq(freqSet, H, supportData, brl, minConf=0.7):
    m = len(H[0])
    if (len(freqSet) > (m + 1)):  # try further merging
        Hmp1 = aprioriGen(H, m + 1)  # create Hm+1 new candidates
        Hmp1 = calcConf(freqSet, Hmp1, supportData, brl, minConf)
        if (len(Hmp1) > 1):  # need at least two sets to merge
            rulesFromConseq(freqSet, Hmp1, supportData, brl, minConf)

if __name__ =='__main__':
    dataSet = loadDataSet()
    L1,suppData=apriori(dataSet,minSupport=0.5)
    rules=generateRules(L1,suppData,minConf=0.7)
    print(rules);print('\n')
    rules1=generateRules(L1,suppData,minConf=0.5)
    print(rules1)
