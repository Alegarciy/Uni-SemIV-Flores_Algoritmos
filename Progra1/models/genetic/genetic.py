from models.genetic.process.drawFlower import DrawFlower
from models.genetic.flowerParts.flowerPartConfig import FlowerPartConfig
from models.genetic.chromosome.chromosomeConfig import ChromosomeConfig
from matplotlib import pyplot as plt
class Genetic:
    def __init__(self):
        self.drawer = DrawFlower()
        self.flowerParts = None

    def setGenetic(self, analazyedFlowerParts):
        self.flowerParts = analazyedFlowerParts

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
