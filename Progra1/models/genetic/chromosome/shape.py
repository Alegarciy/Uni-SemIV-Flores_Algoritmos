from models.genetic.chromosome.Chromosome import Chromosome
from models.genetic.chromosome.analyzeInfoConfig import AnalyzeInfoConfig

from models.genetic.process.outline import Outline
from models.genetic.flowerParts.flowerPartConfig import FlowerPartConfig
from models.converter.flowerConfig import FlowerConfig
from matplotlib import pyplot as plt
import numpy as np

class Shape(Chromosome):
    def __init__(self):
        super().__init__()
        self.outline = Outline()
        self.outlineImages = []
        self.flowersPartArea = []
        self.combinationOfAreas = []
        self.I = 0
        self.J = 1
        self.INFO = 1
        self.IMAGE = 0
        self.distance = 0
        self.quantityPixels = 0

    def sharp(self, flowePartArea):
        minRow = min(flowePartArea)
        for row in range(int(minRow/4), minRow):
            flowePartArea.append(row)

    #Combina los valores del area en pixeles de cada parte de la flor para obtener el area promedio
    def combineFlowerPartArea(self, flowersPartArea, flowerDescription):
        newFlowerPartArea = []
        areasLength = []
        self.distance = 0
        sumDistances = 0
        for area in flowersPartArea:
            areasLength.append(len(area))
            sumDistances += len(area)

        self.distance = sumDistances/len(flowersPartArea)
        maxLength = max(areasLength)
        for row in range(0, maxLength - 1):
            areaOfRow = 0
            for area in flowersPartArea:
                if len(area) > 0:
                    if row > len(area) - 1:
                        areaOfRow += (area[-1])
                    else:
                        areaOfRow += (area[row])

            newFlowerPartArea.append(int(areaOfRow / len(flowersPartArea)))
        if flowerDescription == FlowerPartConfig.PETAL:
            print("SHARP de " + flowerDescription)
            self.sharp(newFlowerPartArea)

        return newFlowerPartArea

    #Obtiene el area de una parte de la flor indicandole el punto de inicio y fin a analizar
    def flowerPartArea(self, image, initPos, endPos, increaseInAxis, axis):
        area = []

        mainAxis = axis
        if(mainAxis == self.J):
            secondAxis = self.I
        else:
            secondAxis = self.J

        #print("INCREASE: " +str(increaseInAxis))
        for posMainAxis in range((initPos[mainAxis]), endPos[mainAxis], increaseInAxis):
            pixelsInAxis = 0
            for posSecondnAxisR in range(initPos[secondAxis], endPos[secondAxis]):

                if mainAxis == self.I:
                    axisI = posMainAxis
                    axisJ = posSecondnAxisR
                else:
                    axisI = posSecondnAxisR
                    axisJ = posMainAxis

                if np.all(image[axisI, axisJ][:3] == FlowerConfig.OUTLINE_COLOR):
                    break
                pixelsInAxis += 1
                image[axisI, axisJ] = FlowerConfig.HIGHLIGHT_COLOR

            for posSecondnAxisL in range(initPos[secondAxis], (initPos[secondAxis] - (endPos[secondAxis] - initPos[secondAxis])), -1):

                if mainAxis == self.I:
                    axisI = posMainAxis
                    axisJ = posSecondnAxisL
                else:
                    axisI = posSecondnAxisL
                    axisJ = posMainAxis

                if np.all(image[axisI, axisJ][:3] == FlowerConfig.OUTLINE_COLOR):
                    break
                pixelsInAxis += 1
                image[axisI, axisJ] = FlowerConfig.HIGHLIGHT_COLOR

            area.append(pixelsInAxis)

        return area

    #Define abstract method
    def analyzeDistribution(self, flowerPartPixels, flowerPartImageInfo, flowerDescription):
        self.outlineImages = []
        self.flowersPartArea = []

        for flowerImageInfo in flowerPartImageInfo:
            outlineImg = self.outline.outlineProcess(flowerImageInfo)
            self.outlineImages.append(outlineImg)
            self.flowersPartArea.append(self.flowerPartArea(
                outlineImg,
                flowerImageInfo[self.INFO][FlowerPartConfig.FLOWERPART_OUTLINE_INIT_POS],
                flowerImageInfo[self.INFO][FlowerPartConfig.FLOWERPART_OUTLINE_END_POS],
                flowerImageInfo[self.INFO][FlowerPartConfig.FLOWERPART_OUTLINE_INCREASE],
                flowerImageInfo[self.INFO][FlowerPartConfig.FLOWERPART_OUTLINE_AXIS]
            ))

            self.combinationOfAreas = self.combineFlowerPartArea(self.flowersPartArea, flowerDescription)

        self.setAnalyzeInfo()
        self.setQuantityPixels()
        return self.analyzeInfo

    #Aproxima la cantidad de pixeles que se necesitaran para dibujar la forma
    def setQuantityPixels(self):
        self.quantityPixels = max(self.combinationOfAreas)*self.distance

    def getQuantityPixels(self):
        return self.quantityPixels

    #Representacion del proceso realizado
    def setAnalyzeInfo(self):
        images = []
        index = 1
        for outlineImage in self.outlineImages:
            images.append([outlineImage, "Forma "+str(index)])
            index += 1

        self.analyzeInfo[AnalyzeInfoConfig.DESCRIPTION] = "Forma del area del "
        self.analyzeInfo[AnalyzeInfoConfig.IMAGES] = images

