from abc import ABC, abstractmethod
from models.genetic.chromosome.analyzeInfoConfig import AnalyzeInfoConfig
class Chromosome(ABC):

    def __init__(self):
        self.analyzeInfo = {
            AnalyzeInfoConfig.DESCRIPTION: "",
            AnalyzeInfoConfig.IMAGES: []
        }

    @abstractmethod
    def analyzeDistribution(self, flowerPartPixels, flowerPartImageInfo, flowerDescription):
        pass
