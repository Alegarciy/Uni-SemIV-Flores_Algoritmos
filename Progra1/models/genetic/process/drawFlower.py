import random
import math
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt
from models.genetic.chromosome.chromosomeConfig import ChromosomeConfig

class DrawFlower:
    def __init__(self):
        self.I = 0
        self.J = 1
        self.randomRotationRange = [-10, 10]
        self.randomPositionRange = [-10, 10]
        self.margin = 25

    #Agrega un petalo  dado un su tamaño a una imagen
    def drawPetal(self, petalArea, canvas, position, colors):
        petalArea.sort()
        center = [int(canvas.shape[self.I] / 2), int(canvas.shape[self.J] / 2)]

        #Pinta el numero de pixeles de cada fila
        Iy = position[self.I]
        for size in petalArea:
            area = int(size / 2)

            Ix = position[self.J]
            for xr in range(1, area):
                canvas[Iy, (Ix + xr)] = colors[
                    random.randint(0, len(colors) - 1)]

            for xl in range(1, Ix - (Ix + area), -1):
                canvas[Iy, (Ix + xl)] = colors[
                    random.randint(0, len(colors) - 1)]

            Iy += 1

        #Si aun no ha llegado al centro sigue pintando
        if (Iy < center[self.I]):
            index = -1
            for y in range(Iy, int(center[self.I])):
                if (index < len(petalArea) * -1):
                    break

                area = int(petalArea[index] / 2)
                Ix = position[self.J]
                for xr in range(1, area):
                    canvas[Iy, (Ix + xr)] = colors[random.randint(0, len(colors) - 1)]

                for xl in range(1, Ix - (Ix + area), -1):
                    canvas[Iy, (Ix + xl)] = colors[random.randint(0, len(colors) - 1)]

                Iy += 1
                index -= 1

    #Dibuja el conjunto de petalos de la flor
    def drawFlowerPetals(self, petalArea, qPetals, colors, petalDistance, canvas, canvasSize):
        rotation = 360 / qPetals
        posI = int((canvasSize/2) - petalDistance) + random.randint(self.randomPositionRange[self.I], self.randomPositionRange[self.J])
        posJ = int(canvasSize/2) + random.randint(self.randomPositionRange[self.I], self.randomPositionRange[self.J])

        for i in range(0, qPetals):
            self.drawPetal(petalArea, canvas, [posI, posJ], colors)
            incertidumbre = random.randint(self.randomRotationRange[self.I], self.randomRotationRange[self.J])
            canvas = ndimage.rotate(canvas, rotation + incertidumbre, reshape=False)

        return canvas

    #Dibuja el centro de una flor
    def drawCenter(self, flowerCenterArea, colors, canvas, canvasSize):
        #((petalShape.distance+self.margin)*3)
        flowerCenterAreaCopy = flowerCenterArea.copy()
        canvasCenter = [int(canvasSize/2), int(canvasSize/2)]
        flowerCenterSize = len(flowerCenterAreaCopy)
        initPosition = [int(canvasCenter[self.I]-flowerCenterSize/2), canvasCenter[self.J]]
        disminucionAlto = 0
        distance = canvasSize/3-self.margin
        distanciaIdeal = distance * 0.3
        if len(flowerCenterAreaCopy) > distanciaIdeal:
            disminucionAlto = int(((len(flowerCenterAreaCopy)-distanciaIdeal)/len(flowerCenterArea))*100)
            print(str(disminucionAlto))

        indexSize=0
        while(indexSize < len(flowerCenterAreaCopy)-1):
            flowerCenterAreaCopy[indexSize] = int(((flowerCenterAreaCopy[indexSize]/distance)*distance * 0.3))
            if disminucionAlto > 1 and random.randint(0, 100) < disminucionAlto:
                del flowerCenterAreaCopy[indexSize]
            else:
                indexSize += 1

        Iy = initPosition[self.I]
        for size in flowerCenterAreaCopy:
            area = int(size / 2)

            Ix = initPosition[self.J]
            for xr in range(1, area):
                canvas[Iy, (Ix + xr)] = colors[
                    random.randint(0, len(colors) - 1)]

            for xl in range(1, Ix - (Ix + area), -1):
                canvas[Iy, (Ix + xl)] = colors[
                    random.randint(0, len(colors) - 1)]

            Iy += 1

        flowerCenterAreaCopy.sort(reverse=True)
        for size in flowerCenterAreaCopy:
            area = int(size / 2)

            Ix = initPosition[self.J]
            for xr in range(1, area):
                canvas[Iy, (Ix + xr)] = colors[
                    random.randint(0, len(colors) - 1)]

            for xl in range(1, Ix - (Ix + area), -1):
                canvas[Iy, (Ix + xl)] = colors[
                    random.randint(0, len(colors) - 1)]

            Iy += 1

        return canvas

    #Dibuja la flor
    def drawFlower(self, petal, petalColors, center, centerColors):
        petalShape = petal.chromosomes[ChromosomeConfig.SHAPE]
        canvasSize = int((petalShape.distance+self.margin)*3)
        canvas = np.zeros([canvasSize, canvasSize, 3], dtype=np.uint8)

        #LLama a dibujar los petalos
        canvas = self.drawFlowerPetals(
            petalShape.combinationOfAreas,
            petal.quantity,
            petalColors,
            petalShape.distance,
            canvas,
            canvasSize
        )

        #Llama a dibujar el centro
        centerShape = center.chromosomes[ChromosomeConfig.SHAPE]
        canvas = self.drawCenter(
            centerShape.combinationOfAreas,
            centerColors,
            canvas,
            canvasSize
        )

        return canvas