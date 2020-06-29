from models.genetic.flowerParts.petal import Petal
from models.genetic.flowerParts.center import Center
from models.genetic.chromosome.chromosomeConfig import ChromosomeConfig
from models.genetic.flowerParts.flowerPartConfig import FlowerPartConfig


class ImageAnalyzer:

    def __init__(self):
        self.__userImages = None
        self.__flowerParts = {}
        self.__flowerPartToAnalyze = None
        self.__chromosomeToAnalyze = ""
        self.__colorDistribution = {}
        self.__totalPixels = 0

    def getUserImages(self):
        return self.__userImages

    def setAnalyzer(self, userImages): #Reinicia los datos
        self.__userImages = userImages
        petal = Petal()
        petal.setFlowerPartImages(userImages)
        center = Center()
        center.setFlowerPartImages(userImages)

        self.__flowerParts = \
        {
            FlowerPartConfig.PETAL: petal,
            FlowerPartConfig.CENTER: center
        }

    def setFlowerPartToAnalyze(self, FLOWERPART):
        self.__flowerPartToAnalyze = self.__flowerParts[FLOWERPART]

    def setChromosomeToAnalyze(self, CHROMOSOME):
        self.__chromosomeToAnalyze = CHROMOSOME

    def analyze(self):
        self.__flowerPartToAnalyze.analyzeChromosome(self.__chromosomeToAnalyze)

    def getFlowerParts(self):
        return self.__flowerParts
