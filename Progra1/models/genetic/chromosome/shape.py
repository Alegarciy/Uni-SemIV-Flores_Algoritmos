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

    #Combina los valores del area en pixeles de cada parte de la flor para obtener el area promedio
    def combineFlowerPartArea(self, flowersPartArea):
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
                if row > len(area) - 1:
                    areaOfRow += (area[-1])
                else:
                    areaOfRow += (area[row])

            newFlowerPartArea.append(int(areaOfRow / len(flowersPartArea)))

        return newFlowerPartArea

    #Obtiene el area de una parte de la flor indicandole el punto de inicio y fin a analizar
    def flowerPartArea(self, image, initPos, endPos, increaseInY):
        area = []
        #print("INCREASE: " +str(increaseInY))
        for y in range((initPos[self.I]), endPos[self.I], increaseInY):
            pixelsInY = 0
            #print("entro y")
            for xr in range(initPos[self.J], endPos[self.J]):
                if np.all(image[y, xr][:3] == FlowerConfig.OUTLINE_COLOR):
                    break
                pixelsInY += 1
                image[y, xr] = FlowerConfig.HIGHLIGHT_COLOR
                #print("entro xr")

            for xl in range(initPos[self.J], (initPos[self.J] - (endPos[self.J] - initPos[self.J])), -1):
                if np.all(image[y, xl][:3] == FlowerConfig.OUTLINE_COLOR):
                    break
                pixelsInY += 1
                image[y, xl] = FlowerConfig.HIGHLIGHT_COLOR
                #print("entro xl")

            area.append(pixelsInY)


        return area

    #Define abstract method
    def analyzeDistribution(self, flowerPartPixels, flowerPartImageInfo):
        self.outlineImages = []
        self.flowersPartArea = []

        for flowerImageInfo in flowerPartImageInfo:
            outlineImg = self.outline.outlineProcess(flowerImageInfo)
            self.outlineImages.append(outlineImg)
            self.flowersPartArea.append(self.flowerPartArea(
                outlineImg,
                flowerImageInfo[self.INFO][FlowerPartConfig.FLOWERPART_OUTLINE_INIT_POS],
                flowerImageInfo[self.INFO][FlowerPartConfig.FLOWERPART_OUTLINE_END_POS],
                flowerImageInfo[self.INFO][FlowerPartConfig.FLOWERPART_OUTLINE_INCREASEY]))

            self.combinationOfAreas = self.combineFlowerPartArea(self.flowersPartArea)

        self.setAnalyzeInfo()
        return self.analyzeInfo

    def setAnalyzeInfo(self):
        images = []
        index = 1
        for outlineImage in self.outlineImages:
            images.append([outlineImage, "Forma "+str(index)])
            index += 1

        self.analyzeInfo[AnalyzeInfoConfig.DESCRIPTION] = "Forma del area del "
        self.analyzeInfo[AnalyzeInfoConfig.IMAGES] = images

