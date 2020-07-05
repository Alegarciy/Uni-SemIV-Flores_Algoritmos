from abc import ABC, abstractmethod
from models.genetic.chromosome.Chromosome import Chromosome

class GeneticChromosome(Chromosome):

    def __init__(self):
        super().__init__()
        self.chromosomeDistribution = {}  # Tabla de distribucion

    @abstractmethod
    def fitness(self, individual):
        pass