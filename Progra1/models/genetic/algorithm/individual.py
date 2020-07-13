from models.genetic.algorithm.GAConfig import GAConfig
import random
class Individual:

    def __init__(self, parent=None):
        self.fitness = 0 #updated with chromosome fitness
        self.genes = []
        self.geneLength = GAConfig.GENES_LENGTH

        #Si el individuo se crea como offsrping
        #Toma los genes del padre
        if not parent:
            self.createIndividual()
        else:
            self.genes = parent.genes.copy()

    def createIndividual(self):
        for i in range(0, self.geneLength):
            self.genes.append(random.randint(0, 1))

    #Setter

    def setFitness(self, value):
        self.fitness = value

    #Getter

    def getGene(self):
        return self.genes

    def getFitness(self):
        return self.fitness
    
    def getIntValue(self):
        exp = self.geneLength - 1
        res = 0
        for digit in self.genes:
            res += digit * (2 ** exp)
            exp -= 1
        return res



