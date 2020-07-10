from models.genetic.process.drawFlower import DrawFlower
from models.genetic.flowerParts.flowerPartConfig import FlowerPartConfig
from models.genetic.chromosome.chromosomeConfig import ChromosomeConfig
from models.genetic.algorithm.ga import GA
from matplotlib import pyplot as plt
from models.plotModelDrawer import PlotModelDrawer
import numpy as np
class Genetic:

    def __init__(self):
        self.drawer = DrawFlower()
        self.flowerParts = {}
        self.GAs = {} # GA obj

    def setGenetic(self, analazyedFlowerParts):
        self.flowerParts = analazyedFlowerParts.copy()

    def start(self, flowerPart, chromosome):
        if flowerPart in self.flowerParts: #self.GAs
            
            #if not exists create key
            if flowerPart in self.GAs:
                if self.GAs[flowerPart].isRunning():
                    self.GAs[flowerPart].pause()
                    self.GAs.pop(flowerPart)


            self.GAs[flowerPart] = GA(
                self.flowerParts[flowerPart].getChromosome(chromosome),
                flowerPart,
                self.flowerParts[flowerPart].getChromosome(ChromosomeConfig.SHAPE).getQuantityPixels() #Population size
            )

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

    def drawProgress(self, flowerPartKey):
        if flowerPartKey in self.GAs and self.GAs[flowerPartKey].isStarted():
            colors = self.GAs[flowerPartKey].getColors()
            flowerPart = self.flowerParts[flowerPartKey]
            flowerPartShape = flowerPart.chromosomes[ChromosomeConfig.SHAPE]
            canvasSize = int((flowerPartShape.distance) * 3)
            canvas = np.zeros([canvasSize, canvasSize, 3], dtype=np.uint8)
            position = [int(canvasSize/2), int(canvasSize/2)]

            if flowerPartKey == FlowerPartConfig.PETAL:
                self.drawer.drawPetal(
                    flowerPartShape.combinationOfAreas,
                    canvas,
                    position,
                    colors
                )

            elif flowerPartKey == FlowerPartConfig.CENTER:
                canvas = self.drawer.drawCenter(
                    flowerPartShape.combinationOfAreas,
                    colors,
                    canvas,
                    canvasSize
                )

            images = []
            images.append(PlotModelDrawer.draw(canvas, "Colores"))
            plotModel = PlotModelDrawer.createMarkup(images, "", "")
            return plotModel

    def getGeneticInfo(self, flowerPart):

        ga = self.GAs[flowerPart]
        mutations = "Mutaciones: " + str(ga.getMutationsInfo())
        mutationRate = "Prob. de mutacion: " + str(round(ga.getMutationRate(), 2)) + "%"
        deadRate = "Rango de muerte: " + str(ga.getDeadRate()) + "%"
        generation = "Generacion: " + str(ga.getGeneration())
        populationSize = "Población: " + str(ga.getPopulationSize())
        fitnessAverage = "Fitness: " + str(ga.getFitnessAverage())

        plotModel = PlotModelDrawer.createInfoMarkup(
            [generation, populationSize, fitnessAverage, mutationRate, mutations, deadRate],
            "geneticInfo"
        )

        return plotModel

    def modifyMutationRate(self, flowerPart, mutationValue):
        if flowerPart in self.GAs and self.GAs[flowerPart].isStarted():
            self.GAs[flowerPart].setMutationValue(mutationValue)
            return "True"
        else:
            return "False"

    def drawFlower(self):
        petal = self.flowerParts[FlowerPartConfig.PETAL]
        center = self.flowerParts[FlowerPartConfig.CENTER]

        #Los colores se obtienen del gentico
        petalColors = self.GAs[FlowerPartConfig.PETAL].getColors()
        centerColors = self.GAs[FlowerPartConfig.CENTER].getColors()

        flower = self.drawer.drawFlower(petal, petalColors, center, centerColors)
        base64Image = [PlotModelDrawer.draw(flower, "Nueva flor")]
        plotModel = PlotModelDrawer.createMarkup(base64Image, "", "")

        return plotModel
