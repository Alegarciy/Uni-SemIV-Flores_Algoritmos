from models.genetic.process.drawFlower import DrawFlower
from models.genetic.flowerParts.flowerPartConfig import FlowerPartConfig
from models.genetic.chromosome.chromosomeConfig import ChromosomeConfig
from models.genetic.algorithm.ga import GA
from matplotlib import pyplot as plt
class Genetic:

    def __init__(self):
        self.drawer = DrawFlower()
        self.flowerParts = {}
        self.GAs = {} # GA obj

    def setGenetic(self, analazyedFlowerParts):
        self.flowerParts = analazyedFlowerParts.copy()


    def start(self, flowerPart, chromosome):
        print('MA A XIIIII')
        if flowerPart in self.flowerParts: #self.GAs
            
            #if not exists create key
            if flowerPart not in self.GAs:
                    self.GAs[flowerPart] = GA(
                    self.flowerParts[flowerPart].getChromosome(chromosome),
                    flowerPart,
                    100 #CAMBIAR ES SOLO DE PRUEBA
                )

            #Start run()
            if self.GAs[flowerPart].isRunning():
                self.GAs[flowerPart].pause()
                self.GAs.pop(flowerPart)

            #Start new GA
            self.GAs[flowerPart] = GA(
                self.flowerParts[flowerPart].getChromosome(chromosome),
                flowerPart,
                100 #CAMBIAR ES SOLO DE PRUEBA
            )

            print("QUE E SOOOOO")
            self.GAs[flowerPart].run()
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
        petalShape = petal.chromosomes[ChromosomeConfig.SHAPE]
        petalArea = petalShape.combinationOfAreas
        qPetals = petal.quantity
        #colors = ...
        colors = [50,50,255]
        petalDistance = petalShape.distance
        flower = self.drawer.drawFlower(petalArea, qPetals, colors, petalDistance)
        plt.imshow(flower)
        plt.show()
