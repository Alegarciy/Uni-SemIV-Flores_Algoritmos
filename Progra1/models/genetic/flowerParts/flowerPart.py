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
    #Se define en cada clase los datos de la flor que le sean necesarios
    def setFlowerPartImages(self, flowerImages):
        pass

    @abstractmethod
    #Analiza de forma sistematica el cromosoma que se le indique como argumento
    def analyzeChromosome(self, chromosome):
        pass

    #Getter
    def getChromosome(self, key):
        return self.chromosomes[key]
