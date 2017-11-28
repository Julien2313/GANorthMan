from random import random
import math

class NeuralNetwork:
    
    def mutate(self, nbrMutates):
        for x in xrange(0, nbrMutates):
            newWeight       = random() * 2 - 1
            layout          = random() * (len(self.NN) - 1) + 1
            neuronToMutate  = len(self.NN[layout])
            weightToMutate  = len(self.NN[layout][neuron].weight)
            
            self.NN[layout][neuronToMutate].weight[weightToMutate] = newWeight
            

    def calculateOutputs(self):
        NN = iter(self.NN)
        lastLayout = next(NN)
        for layout in NN:
            for neuron in layout:
                neuron.allWeight = 0
                for x in xrange(0, len(lastLayout)):
                    if lastLayout[x].state == 1:
                        neuron.allWeight = neuron.allWeight + neuron.weight[x]
                neuron.activateFunction()
                
            lastLayout = layout
                
        
    def setInputs(self, inputs):
        for numInput in xrange(0, self.nbrInputs):
            self.NN[0][numInput].state = inputs[numInput]

    def randomiseWeight(self):
        NN = iter(self.NN)
        lastLayout = next(NN)
        for layout in NN:
            for neuron in layout:
                for x in xrange(0, len(lastLayout)):
                    neuron.weight.append(random() * self.maxWeight - self.maxWeight/2)
            lastLayout = layout

    def printNN(self):
        for layout in self.NN:
            for neuron in layout:
                print neuron.weight, neuron.score, neuron.allWeight, ", ", neuron.state
            print ""

    def initNN(self):
        self.NN = []
        self.NN.append([])
        #init input
        for x in xrange(0, self.nbrInputs):
            self.NN[0].append(Neuron())
        
        #init hiden layers
        for x in xrange(0, self.nbrHidenLayers):
            self.NN.append([])
            for y in xrange(0, self.nbrNeuronsPerHiddenLayer):
                self.NN[x+1].append(Neuron())
                
        #init ouput
        self.NN.append([])
        for x in xrange(0, self.nbrOutputs):
            self.NN[self.nbrHidenLayers + 1].append(Neuron())

        self.randomiseWeight()


    def __init__(self):
        self.nbrHidenLayers              =   2 #without input/ouput
        self.nbrInputs                   =   3
        self.nbrOutputs                  =   4
        self.nbrNeuronsPerHiddenLayer    =   self.nbrInputs * 2
        
        self.maxWeight                   =   2

        self.initNN()


class Neuron:
    def activateFunction(self):
        self.score = 1.0/(1+math.exp(-self.allWeight))
        
        if self.score > 0.5:
            self.state = 1
        else:
            self.State = 0

    def __init__(self):
        self.state  =   0 #state is 1 or 0, activate or not
        self.weight =  [] #weight of last the neurons, between 0 and maxWeight
        self.allWeight =  0
        self.score  =   0 #the score of the activate function


