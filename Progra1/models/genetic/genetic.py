from models.genetic.process.drawFlower import DrawFlower
from models.genetic.flowerParts.flowerPartConfig import FlowerPartConfig
from models.genetic.chromosome.chromosomeConfig import ChromosomeConfig
from models.genetic.algorithm.ga import GA
from matplotlib import pyplot as plt
class Genetic:

    def __init__(self):
        self.drawer = DrawFlower()
        self.flowerParts = {}
        self.GAs = {}

    def setGenetic(self, analazyedFlowerParts):
        self.flowerParts = analazyedFlowerParts.copy()


    def start(self, flowerPart, chromosome):
        if flowerPart in self.GAs:
            if self.GAs[flowerPart].isRunning():
                self.GAs[flowerPart].pause()
                self.GAs.pop(flowerPart)

            self.GAs[flowerPart] = GA(
                self.flowerParts[flowerPart][chromosome],
                flowerPart,
                100 #CAMBIAR ES SOLO DE PRUEBA
            )
            return "True"

        else:
            return "False"

    def pause(self, flowerPart):
        if flowerPart in self.GAs:
            self.GAs[flowerPart].pause()

    def draw(self):
        petal = self.flowerParts[FlowerPartConfig.PETAL]
        petalShape = petal.chromosomes[ChromosomeConfig.SHAPE]
        petalArea = petalShape.combinationOfAreas
        qPetals = petal.quantity
        #colors = ...
        colors = [50,50,255]
        petalDistance = petalShape.distance
        flower = self.drawer.drawFlower(petalArea, qPetals, colors, petalDistance)
        plt.imshow(flower)
        plt.show()
