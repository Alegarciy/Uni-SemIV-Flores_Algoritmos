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
        #Almacena las imagenes del contorno
        self.outline = Outline()
        self.outlineImages = []

        #Almacena las areas de la flor ya sea Petalo o centro
        self.flowersPartArea = []
        self.combinationOfAreas = []

        #Parametros para indicar el eje x o y vistos como si fueran filas o columnas
        self.I = 0
        self.J = 1

        #Index donde se alamacena la informacion del json y la imagen de una flor en una lista
        self.INFO = 1
        self.IMAGE = 0

        #Distancia del petalo o del centro
        self.distance = 0

        #Cantidad de pixeles de dicha flowerPart
        self.quantityPixels = 0

    #Aproxima la cantidad de pixeles que se necesitaran para dibujar la forma
    def setQuantityPixels(self):
        self.quantityPixels = max(self.combinationOfAreas)*self.distance

    #Corrige si la punta de un petalo quedó de forma plana
    def sharp(self, flowePartArea):
        minRow = min(flowePartArea)
        for row in range(int(minRow/4), minRow):
            flowePartArea.append(row)

    #Obtiene el area promedio
    def combineFlowerPartArea(self, flowersPartArea, flowerDescription):
        #Datos para el analisis y guardar las areas
        newFlowerPartArea = []
        areasLength = []
        self.distance = 0
        sumDistances = 0

        #Obtiene la distancia promedio
        for area in flowersPartArea:
            areasLength.append(len(area))
            sumDistances += len(area)
        self.distance = sumDistances/len(flowersPartArea)
        maxLength = max(areasLength)


        #Itera el numero de filas de la distancia maxima
        for row in range(0, maxLength - 1):
            areaOfRow = 0

            #Calcula la cantidad de pixels promedio para cada fila
            for area in flowersPartArea:
                if len(area) > 0:
                    if row > len(area) - 1:
                        areaOfRow += (area[-1])
                    else:
                        areaOfRow += (area[row])

            #Agrega la cantidad de pixeles promedio
            newFlowerPartArea.append(int(areaOfRow / len(flowersPartArea)))

        #Si se esta analizando el petalo corrige la forma de la punta
        if flowerDescription == FlowerPartConfig.PETAL:
            self.sharp(newFlowerPartArea)

        return newFlowerPartArea

    #Obtiene el area de una parte de la flor indicandole el punto de inicio y fin a analizar
    def flowerPartArea(self, image, initPos, endPos, increaseInAxis, axis):
        area = []

        #Define el eje principal del recorrido
        mainAxis = axis
        if(mainAxis == self.J):
            secondAxis = self.I
        else:
            secondAxis = self.J

        #print("INCREASE: " +str(increaseInAxis))
        for posMainAxis in range((initPos[mainAxis]), endPos[mainAxis], increaseInAxis):
            #Cantidad de pixeles en una fila
            pixelsInAxis = 0

            #A la derecha del punto inicial
            for posSecondnAxisR in range(initPos[secondAxis], endPos[secondAxis]):

                #Dependiendo sobre cual eje esta analizando cambia la posicion
                if mainAxis == self.I:
                    axisI = posMainAxis
                    axisJ = posSecondnAxisR
                else:
                    axisI = posSecondnAxisR
                    axisJ = posMainAxis

                #Si encuentra el limite del contorno termina de contar
                if np.all(image[axisI, axisJ][:3] == FlowerConfig.OUTLINE_COLOR):
                    break

                #Sino, sigue contando pixeles
                pixelsInAxis += 1
                image[axisI, axisJ] = FlowerConfig.HIGHLIGHT_COLOR

            #A la izquierda del punto inicial
            for posSecondnAxisL in range(initPos[secondAxis], (initPos[secondAxis] - (endPos[secondAxis] - initPos[secondAxis])), -1):

                #Dependiendo sobre cual eje esta analizando cambia la posicion
                if mainAxis == self.I:
                    axisI = posMainAxis
                    axisJ = posSecondnAxisL
                else:
                    axisI = posSecondnAxisL
                    axisJ = posMainAxis

                #Si encuentra el limite del contorno termina de contar
                if np.all(image[axisI, axisJ][:3] == FlowerConfig.OUTLINE_COLOR):
                    break

                # Sino, sigue contando pixeles
                pixelsInAxis += 1
                image[axisI, axisJ] = FlowerConfig.HIGHLIGHT_COLOR

            #Agrega los pixeles contados
            area.append(pixelsInAxis)

        return area

    #Define abstract method
    def analyzeDistribution(self, flowerPartPixels, flowerPartImageInfo, flowerDescription):

        #Establece las listas vacias
        self.outlineImages = []
        self.flowersPartArea = []

        #Itera sobre las flores que se van a analizar
        for flowerImageInfo in flowerPartImageInfo:

            #Imagen del contorno
            outlineImg = self.outline.outlineProcess(flowerImageInfo)
            self.outlineImages.append(outlineImg)

            #Area de la flor(Centro o petalo)
            self.flowersPartArea.append(self.flowerPartArea(
                outlineImg,
                flowerImageInfo[self.INFO][FlowerPartConfig.FLOWERPART_OUTLINE_INIT_POS],
                flowerImageInfo[self.INFO][FlowerPartConfig.FLOWERPART_OUTLINE_END_POS],
                flowerImageInfo[self.INFO][FlowerPartConfig.FLOWERPART_OUTLINE_INCREASE],
                flowerImageInfo[self.INFO][FlowerPartConfig.FLOWERPART_OUTLINE_AXIS]
            ))

        #Obtiene el promedio del area
        self.combinationOfAreas = self.combineFlowerPartArea(self.flowersPartArea, flowerDescription)
        #Crea estructura para mostrar informacion del proceso
        self.setAnalyzeInfo()
        #Obtiene la cantidad de pixeles necesaria par pintar la flor
        self.setQuantityPixels()

        return self.analyzeInfo

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

