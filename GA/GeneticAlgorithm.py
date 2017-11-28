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

    def mutateChild(self):
        print "tbd"

    @staticmethod
    def reproductionCouple(NN1, NN2):
        print "tbd"

    #Everything about reproduction
    #-----------------------------

    def evaluatePop(self):
        print "tbd"


    
    def __init__(self):
        self.sizePop            =   1
        self.nbrReproductions   =    10
        self.nbrMutations       =    10
        self.pop                =   []
        for x in xrange(0, self.sizePop):
            self.pop.append(NeuralNetwork())
    
        #set GA parameters
        
GA = GeneticAlgorithm()
GA.pop[0].setInputs([1,1,1])
GA.pop[0].calculateOutputs()
GA.pop[0].printNN()
GA.pop[0].mutate(1)
GA.pop[0].printNN()
