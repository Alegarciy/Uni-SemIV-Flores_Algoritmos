from models.genetic.algorithm.GAConfig import GAConfig
from models.genetic.algorithm.population import Population
class GA:
    def __init__(self, chromosome, flowerPart, populationSize):
        self.__chromosome = chromosome
        self.__flowerPart = flowerPart
        self.__populationSize = populationSize
        self.__mutationRate = GAConfig.MUTATION_RATE

        self.__population = None #Population obj
        self.__mutations = 0
        self.__generation = 0
        self.__isRunning = False
        self.__started = False

    def run(self):
        self.__isRunning = True
        self.__started = True
        #while(self.__isRunning):
        print("I am running" + self.__flowerPart)
        populationTemp = Population()
        populationTemp.generatePopulation(25)
        populationTemp.printPopulation()
            #select
            #cross-over
            #mutate
            #evaluate

    def isRunning(self):
        return self.__isRunning

    def isStarted(self):
        return self.__started

    def pause(self):
        self.__isRunning = not self.__isRunning

    def getPopulation(self):
        return self.__population

    #Analyze individual fitness and store it
    def defineFitnessPopulation(self):
        pass