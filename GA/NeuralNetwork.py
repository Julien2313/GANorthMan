from random import random

class NeuralNetwork:
    

    def mutate(self):
        print "tbd"

    def calculateOutputs(self):
        NN = iter(self.NN)
        next(NN)
        for layout in NN:
            for neuron in layout:
                print "oui"
                
        
    def setInput(self, inputs):
        self.NN[0] = array(inputs)

    def randomiseWeight(self):
        NN = iter(self.NN)
        lastLayout = next(NN)
        for layout in NN:
            for neuron in layout:
                neuron.weight = [] * len(lastLayout)
                for weight in neuron.weight:
                    weight = random() * self.maxWeight
                print neuron.weight
            lastLayout = layout


    def initNN(self):
        self.NN = [[Neuron()] * self.nbrInputs] + [[Neuron()] * self.nbrNeuronsPerHiddenLayer] * self.nbrLayers + [[Neuron()] * self.nbrOutputs]
        self.randomiseWeight()


    def __init__(self):
        self.nbrLayers                   =   2 #without input/ouput
        self.nbrInputs                   =   3
        self.nbrOutputs                  =   4
        self.nbrNeuronsPerHiddenLayer    =   self.nbrInputs * 2
        
        self.maxWeight                   =   2
        
        self.initNN()


class Neuron:
    def activateFunction(self):
        self.score = 1.0/(1+exp(-self.score));

    def __init__(self):
        self.state  =   0 #state is 1 or 0, activate or not
        self.weight =  [] #weight of last the neurons, between 0 and maxWeight
        self.score  =   0 #the actual state


