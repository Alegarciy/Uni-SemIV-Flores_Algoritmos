from abc import ABC, abstractmethod
class Chromosome(ABC):

    def __init__(self):
        self.chromosomeDistribution = {} #Tabla de distribucion

    @abstractmethod
    def fitness(self):
        pass

    @abstractmethod
    def analyzeDistribution(self, flowerPartsImages): #Crear la tabla de distribucion
        pass

