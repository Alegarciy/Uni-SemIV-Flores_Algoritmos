from models.genetic.algorithm.GAConfig import GAConfig
import random
class Individual:

    def __init__(self):
        self.fitness = 0 #updated with chromosome fitness
        self.genes = []
        self.geneLength = GAConfig.GENES_LENGTH
        self.createIndividual()

    def createIndividual(self):

        for i in range(0, self.geneLength):
            self.genes.append(random.randint(0, 1))

    #Setter

    def setFitness(self, value):
        self.fitness = value

    #Getter

    def getGene(self):
        return self.genes
    
    def getIntValue(self):
        exp = self.geneLength - 1
        res = 0
        for digit in self.genes:
            res += digit * (2 ** exp)
            exp -= 1
        return res



