from abc import ABC, abstractmethod
from models.genetic.chromosome.chromosomeConfig import ChromosomeConfig
from models.genetic.chromosome.color import Color
from models.genetic.chromosome.shape import Shape


class FlowerPart(ABC):

    def __init__(self, _description):
        self.description = _description
        self.flowerPartPixels = []
        self.flowerPartImageInfo = []
        self.chromosomes = \
        {
            ChromosomeConfig.COLOR: Color(),
            ChromosomeConfig.SHAPE: Shape()
        }

    @abstractmethod
    def setFlowerPartImages(self, flowerImages): #Yo le paso las datos del voraz, y este obtiene los que ocupa
        pass

    @abstractmethod
    def analyzeChromosome(self, chromosome):
        pass

    #Getter
    def getChromosome(self, key):
        return self.chromosomes[key]
