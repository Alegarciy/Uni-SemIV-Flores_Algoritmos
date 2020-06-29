from abc import ABC, abstractmethod
class Chromosome(ABC):


    @abstractmethod
    def analyzeDistribution(self, flowerPartPixels, flowerPartImageInfo):
        pass

