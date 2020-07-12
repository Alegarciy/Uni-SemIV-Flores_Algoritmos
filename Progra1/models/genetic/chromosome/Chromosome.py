from abc import ABC, abstractmethod
from models.genetic.chromosome.analyzeInfoConfig import AnalyzeInfoConfig
class Chromosome(ABC):

    def __init__(self):
        #Estructura que almacena informacion e imagenes para mostrar al usuario
        #El proceso realizado
        self.analyzeInfo = {
            AnalyzeInfoConfig.DESCRIPTION: "",
            AnalyzeInfoConfig.IMAGES: []
        }

    @abstractmethod
    #En la definicion del metodo se indica como analizar de forma sistematica dicho cromosoma
    def analyzeDistribution(self, flowerPartPixels, flowerPartImageInfo, flowerDescription):
        pass
