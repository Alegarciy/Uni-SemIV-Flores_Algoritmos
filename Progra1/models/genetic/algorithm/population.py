from models.genetic.algorithm.individual import Individual
from operator import attrgetter

class Population:

    def __init__(self):
        self.individuals = [] #obj Individual List 

    #Generate inicial population
    def generatePopulation(self, popSize):
        for i in range(0,popSize):
            self.individuals.append(Individual())
    
    #Sort population by fitness
    def sortPopulation(self):
        self.individuals = sorted(self.individuals, key=attrgetter('fitness'))

    #Simple test print
    def printPopulation(self):
        individualNum = 0
        for individual in self.individuals:
            print('INDIVIDUAL NUMBER #',individualNum)
            print('Individual genes: ', individual.getGene())
            print('Individual fitness: ', individual.getFitness())
            individualNum += 1
