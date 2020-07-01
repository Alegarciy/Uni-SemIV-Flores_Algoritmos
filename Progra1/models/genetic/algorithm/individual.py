from models.genetic.algorithm import GAConfig
import random
class individual:

    def __init__(self):
        self.fitness = 0
        self.genes = []
        self.geneLength = GAConfig.GENES_LENGTH
        self.createIndividual()

    def createIndividual(self):

        for i in range(0, self.geneLength):
            self.genes.append(random.randint(0, 1))
