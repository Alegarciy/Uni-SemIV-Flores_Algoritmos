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

    def run(self):
        self.__isRunning = True
        while(self.__isRunning):
            print("I am running" + self.__flowerPart)

    def isRunning(self):
        return self.__isRunning

    def pause(self):
        self.__isRunning = not self.__isRunning

    def getPoblation(self):
        return self.__poblation