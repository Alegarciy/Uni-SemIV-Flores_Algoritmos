from abc import ABC, abstractmethod
from models.genetic.chromosome.chromosomeConfig import ChromosomeConfig
from models.genetic.chromosome.color import Color

class FlowerPart(ABC):

    def __init__(self):
        self.flowerPartImages = []
        self.chromosomes = \
        {
            ChromosomeConfig.COLOR: Color()
        }

    @abstractmethod
    def setFlowerPartImages(self, flowerImages): #Yo le paso las datos del voraz, y este obtiene los que ocupa
        pass

    @abstractmethod
    def analyzeChromosome(self, chromosome):
        pass
