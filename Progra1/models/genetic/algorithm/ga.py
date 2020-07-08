from models.genetic.algorithm.GAConfig import GAConfig
import random
from models.genetic.algorithm.population import Population
from models.genetic.algorithm.individual import Individual
import time
class GA:
    def __init__(self, chromosome, flowerPart, populationSize):
        self.__chromosome = chromosome
        self.__flowerPart = flowerPart
        self.__populationSize = int(populationSize)
        self.__mutationRate = GAConfig.MUTATION_RATE
        self.__deadRate = 30  #Variable?

        #Init Population
        self.__population = Population() #Population obj
        self.__population.generatePopulation(self.__populationSize)

        self.__isRunning = False
        self.__started = False


        self.__mutations = 0
        self.__generation = 1
        self.__fitnessAverage = 0

        self.__colors = [[0, 0, 0]]

    def run(self):
        self.__isRunning = True
        self.__started = True
        while True:
            while(self.__isRunning):
                time.sleep(0.01)
                print(" ** GENERATION #" + str(self.__generation) +"  "+ str(self.__populationSize)+ " **")
                self.__fitnessAverage = self.calcFitness()
                self.selectPopulation()
                self.reproduce()
                self.__generation += 1

            time.sleep(1)

    def calcFitness(self):
        print("--FITNESS--")
        print("Fittest: ")
        print(str(self.__chromosome.getDominantColor()))
        sumOfFitness = 0
        tempColors = []
        for individual in self.__population.individuals:
            fitnessValue, color = self.__chromosome.fitness(individual)
            sumOfFitness += fitnessValue
            tempColors.append(color)

        self.__colors.clear()
        self.__colors = tempColors.copy()
        return sumOfFitness/self.__populationSize

    def selectPopulation(self):
        self.__population.purgePopulation(self.__deadRate)

    def reproduce(self):
        quantityIndividuals = len(self.__population.individuals)
        quanityOffspring = int(self.__populationSize - quantityIndividuals)
        offspringList = []
        print("--REPRODUCE--")
        for offSpringNumber in range(0, quanityOffspring):
            #print("NEW OFFSPRING")
            parent1 = self.__population.getIndividual(
                random.randint(0, quantityIndividuals-1)
            )
            parent2 = self.__population.getIndividual(
                random.randint(0, quantityIndividuals-1)
            )

            #Reproducir
            offspring = self.crossover(parent1, parent2)
            #Mutar
            self.mutate(offspring)
            #Add
            offspringList.append(offspring)

        #Merge population with offsprings
        self.__population.addOffsprings(offspringList)


    def mutate(self, ind):
        if random.randint(1, 100) < self.__mutationRate:
            bit = random.randint(0, GAConfig.GENES_LENGTH-1)
            if ind.genes[bit] == 0:
                ind.genes[bit] = 1
            elif ind.genes[bit] == 1:
                ind.genes[bit] = 0
            self.__mutations += 1
            #print("MUTACION en " + str(bit))
            #print(ind.genes)

    def crossover(self, parent1, parent2):
        bitP1 = random.randint(0, GAConfig.GENES_LENGTH)
        bitP2 = random.randint(0, GAConfig.GENES_LENGTH)
        offspring = Individual(parent1)
        if bitP1 <= bitP2:
            offspring.genes[bitP1:bitP2] = parent2.genes[bitP1:bitP2]
        else:
            offspring.genes[bitP2:bitP1] = parent2.genes[bitP2:bitP1]

        #print("Parent1: ")
        #print(parent1.genes)
        #print("Parent2: ")
        #print(parent2.genes)
        #print("Offspring: crossover" + str(bitP1) + " - " + str(bitP2))
        #print(offspring.genes)
        #print(" ")
        return offspring

    def getColors(self):
        return self.__colors.copy()

    def isRunning(self):
        return self.__isRunning

    def isStarted(self):
        return self.__started

    def pause(self):
        self.__isRunning = not self.__isRunning

    def getPopulation(self):
        return self.__population


    def getMutationsInfo(self):
        return self.__mutations

    def getFitnessAverage(self):
        return 100 - self.__fitnessAverage

    def getDeadRate(self):
        return self.__deadRate

    def getGeneration(self):
        return self.__generation

    def getPopulationSize(self):
        return self.__populationSize

    def getMutationRate(self):
        return self.__mutationRate

