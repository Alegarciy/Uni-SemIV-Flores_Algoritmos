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
        if flowerPart in self.GAs and self.GAs[flowerPart].isStarted():
            self.GAs[flowerPart].pause()
            return "True"
        else:
            return "False"

    def draw(self):
        petal = self.flowerParts[FlowerPartConfig.PETAL]
        center = self.flowerParts[FlowerPartConfig.CENTER]

        #Los colores se obtienen del gentico
        petalColors = [255, 0, 0]
        centerColors = [0, 0, 255]

        flower = self.drawer.drawFlower(petal, petalColors, center, centerColors)

        plt.imshow(flower)
        plt.show()
