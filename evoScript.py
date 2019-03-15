""" 
IMPORT PACKAGES 
"""
import math
import random

""" 
GLOBAL VALUES
"""
dartBoardTarget = 0
dartBoardRadius = 10
popSize = 3
turnOver = 0.1 # Fraction of population that is replace each generation

"""
CALCULATED GLOBALS
"""
turnOverNum = int(popSize*turnOver)


""" 
DEFINE CLASSES 
"""
def isValid(xval):
        if not (isinstance(xval,int) or isinstance(xval,float)):
            return False
        elif (xval < dartBoardTarget) or (xval > dartBoardRadius):
            return False
        else:
            return True

class trait(object):
    val = None
    __lBound = dartBoardTarget
    __uBound = dartBoardRadius
    def __init__(self, xval=None):
        # Need to apply exceptions so that traits with invalid values and bounds can not be made
        if xval == None:
            self.val = (self.__uBound-self.__lBound)*random.random()
        elif isValid(xval):
            self.val = xval
        else:
            print('Invalid trait value. __init__ failed.')
    def setVal(self,xval):
        if isValid(xval):
            self.val = xval
        else:
            print('Invalid trait value. setVal failed.')
    def getlBound(self):
        return self.__lBound
    def getuBound(self):
        return self.__uBound
    def __repr__(self):
        return '(%.2f < %.2f < %.2f)' %(self.__lBound, self.val, self.__uBound)

class individual(object):
    trait1 = None
    __successMetric = None
    def __init__(self, xtrait1=None):
        if xtrait1 == None:
            self.trait1 = trait()
        else:
            self.trait1 = xtrait1
    def evalSuccess(self):
        """ Calls a simulation routine to evaluate an individual's successfullness and assign a value to successMetric """
        x = self.trait1.val
        X = self.trait1.getuBound()
        self.__successMetric = (X-x)/X
    def getSuccessMet(self):
        return self.__successMetric
    def __repr__(self):
        traitRep = self.trait1.__repr__()
        traitRep = ''.join([ch for ch in traitRep if ch != ')'])
        return traitRep + ' | %.6s)' %(self.__successMetric)

class population(object):
    individuals = []
    def __init__(self,xsize=0):
        if xsize > 0:
            for i in range(0,xsize):
                individual1 = individual()
                self.individuals.append(individual1)
        else:
            pass

""" 
SCRIPT BODY 
"""

myPop =  population(popSize)
for indiv in myPop.individuals:
    indiv.evalSuccess()
for i in range(turnOverNum):
    indiv1, indiv2 = random.choices(myPop.individuals, k=2)
    print(indiv1, indiv2)