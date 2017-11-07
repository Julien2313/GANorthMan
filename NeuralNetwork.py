class NeuralNetwork:
    

    def mutate(self):
        print "tbd"

    def calculateOutputs(self):
        print "tbd"

    def setInput(self, inputs):
        self.NN[0] = array(inputs)
    
    def __init__(self):
        self.nbrLayers                   =   20 #without input/ouput
        self.nbrInputs                   =   10
        self.nbrOutputs                  =   10
        self.nbrNeuronsPerHiddenLayer    =   nbrInputs * 10
        
        self.maxWeight                   =   2

        self.NN = [Neuron()] * self.nbrInputs + [[Neuron()] * self.nbrNeuronsPerHiddenLayer]*self.nbrLayers + [Neuron()] * self.nbrOutputs



class Neuron:
    def activateFunction(self):
        self.score = 1.0/(1+exp(-score));

    def __init__(self):
        self.state  =   0 #state is 1 or 0, activate or not
        self.weight  =   0 #weight of the neuron, between 0 and maxWeight


