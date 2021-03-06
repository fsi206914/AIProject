"""
    Collection of collaborative filtering techniques:
"""
from __future__ import division
class dict_hash:

    def __init__(self, input_n, label):
        self.nValue = input_n
        self.the_whole = self.nValue*self.nValue*2
        self.Bidict=dict()
        self.Bidict={'A':{}, 'B':{}}
        if label == 'A':
            self.Utility = self.Utility_A
        else:
            self.Utility = self.Utility_B


    def checkDuplicate(self, Rlist, label):
        Dict = self.Bidict[label]
        Index = 0
        for x in range(self.nValue):
            Index += Rlist[2*x]*Rlist[2*x+1]
            Index += Rlist[2*x]

        if Dict.has_key(Index):
            value = Dict[Index]
            for k in value:
                x = 0
                for x in range(self.nValue*2):
                    if not k[x] == Rlist[x]:
                        break
                if x == self.nValue*2 -1:
                    return True

            return False;
        else:
            self.Bidict[label][Index] = []
            return False;

    def append(self, Rlist, label):

        Index = 0
        for x in range(self.nValue):
            Index += Rlist[2*x]*Rlist[2*x+1]
            Index += Rlist[2*x]

        newList = list(Rlist)
        self.Bidict[label][Index].append(newList)

    def delete(self, Rlist, label):

        Index = 0
        for x in range(self.nValue):
            Index += Rlist[2*x]*Rlist[2*x+1]
            Index += Rlist[2*x]

        self.Bidict[label][Index].remove(Rlist)

    def Utility_A(self, RList):
        cal = 0
        for i in range(self.nValue):
            cal += RList[i]
        if(cal==0):
            return 0
        elif cal==self.the_whole:
            return 1
        else:
            return cal/self.the_whole

    def Utility_B(self, RList):
        cal = 0
        for i in range(self.nValue):
            cal += RList[i]
        if(cal==0):
            return 1
        elif cal==self.the_whole:
            return 0
        else:
            return 1-cal/self.the_whole

    def printDictHash(self):

        print self.Bidict
