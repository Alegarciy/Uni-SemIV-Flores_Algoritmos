from models.genetic.algorithm.GAConfig import GAConfig
class GA:
    def __init__(self, chromosome, flowerPart, poblationSize):
        self.__chromosome = chromosome
        self.__flowerPart = flowerPart
        self.__poblationSize = poblationSize
        self.__mutationRate = GAConfig.MUTATION_RATE

        self.__poblation = []
        self.__mutations = 0
        self.__generation = 0
        self.__isRunning = False
        self.__started = False

    def run(self):
        self.__isRunning = True
        self.__started = True
        while(self.__isRunning):
            print("I am running" + self.__flowerPart)
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

    def getPoblation(self):
        return self.__poblation