from random import random
import math
from PIL import Image, ImageDraw

class NeuralNetwork:

    def drawNN(self):

        gapX = 250
        gapY = 200

        nbrNeuronsMax = max(self.nbrNeuronsPerHiddenLayer, self.nbrOutputs, self.nbrInputs)
        sizeX = len(self.NN)  * gapX + 100
        sizeY = nbrNeuronsMax * gapY + 100
        im = Image.new('RGB',(sizeX, sizeY), (255,255,255))
        pix = im.load()
        draw = ImageDraw.Draw(im)
        
        x = 20
        for layout in self.NN:
            y = 20
            for neuron in layout:
                espace = nbrNeuronsMax * 1.0 / len(layout)
                y = y + espace / 2.0
                if neuron.state:
                    draw.ellipse((x, y, 80 + x, 80 + y), fill = 'blue', outline ='blue')
                else:
                    draw.ellipse((x, y, 80 + x, 80 + y), fill = 'white', outline ='blue')
                #for weights in neuron.weight:

                y = y + gapY * espace
            x = x + gapX

                
        im.save('NN.png')

    def mutate(self, nbrMutates):
        for x in xrange(0, nbrMutates):
            newWeight       = random() * 2 - 1
            layout          = int(random() * (len(self.NN) - 1) + 1)
            neuronToMutate  = int(random() * len(self.NN[layout]))
            weightToMutate  = int(random() * len(self.NN[layout][neuronToMutate].weight))

            print "Nombre de couches :", len(self.NN), ", on choisi celle la : ", layout, ".\nCe layout a ", len(self.NN[layout]), " neurones."
            print "On choisi ce neurone : ", neuronToMutate, ", ce neurone a ", len(self.NN[layout][neuronToMutate].weight), " de neurones fils."
            print "On mute celui la : ", weightToMutate
            
            self.NN[layout][neuronToMutate].weight[weightToMutate] = newWeight

    def calculateOutputs(self):
        NN = iter(self.NN)
        lastLayout = next(NN)
        for layout in NN:
            for neuron in layout:
                neuron.allWeight = 0
                for x in xrange(0, len(lastLayout)):
                    if lastLayout[x].state:
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
        self.nbrHidenLayers              =   5 #without input/ouput
        self.nbrInputs                   =   5
        self.nbrOutputs                  =   4
        self.nbrNeuronsPerHiddenLayer    =   self.nbrInputs * 2
        
        self.maxWeight                   =   2

        self.initNN()


class Neuron:
    def activateFunction(self):
        self.score = 1.0/(1+math.exp(-self.allWeight))
        
        if self.score > 0.5:
            self.state = True
        else:
            self.State = False

    def __init__(self):
        self.state  =   False #state is 1 or 0, activate or not
        self.weight =  [] #weight of last the neurons, between 0 and maxWeight
        self.allWeight =  0
        self.score  =   0 #the score of the activate function


