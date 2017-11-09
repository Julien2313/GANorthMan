#thought for NN

from NeuralNetwork import NeuralNetwork

class GeneticAlgorithm:
    
    #Everything about init
    def initializePop(self):
        print "tbd"


    #Everything about init
    #-----------------------------
    #Everything about reproduction
    def reproductionPop(self):
        print "tbd"

    def chooseCoupleParents(self):
        print "tbd"

    def mutatePop(self):
        print "tbd"

    @staticmethod
    def reproductionCouple(NN1, NN2):
        print "tbd"

    #Everything about reproduction
    #-----------------------------

    def evaluatePop(self):
        print "tbd"


    
    def __init__(self):
        self.sizePop            =   100
        self.nbrReproductions   =    10
        self.nbrMutations       =    10
        self.pop                =   [NeuralNetwork()] * self.sizePop
    
        #set GA parameters
        
GA = GeneticAlgorithm()
print "test"
