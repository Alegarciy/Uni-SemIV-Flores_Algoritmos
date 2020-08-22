import random
import math
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt
from models.genetic.chromosome.chromosomeConfig import ChromosomeConfig
from models.genetic.process.drawFlowerConfig import DrawFlowerConfig

class DrawFlower:

    def __init__(self):
        self.I = 0
        self.J = 1
        self.randomRotationRange = [-5, 5]
        self.randomPositionRange = [-5, 5]

    #Agrega un petalo a una imagen
    def drawPetal(self, petalArea, canvas, position, colors):
        #Se ordena las filas de menor a mayor
        petalArea.sort()
        #Posicion central de la imagen
        center = [int(canvas.shape[self.I] / 2), int(canvas.shape[self.J] / 2)]

        #posicion inicial en el eje y (filas)
        Iy = position[self.I]

        # Pinta el numero de pixeles de cada fila
        for size in petalArea:
            area = int(size / 2)
            Ix = position[self.J]

            #Pinta del centro a la derecha
            for xr in range(1, area):
                canvas[Iy, (Ix + xr)] = colors[
                    random.randint(0, len(colors) - 1)]

            #Pinta del centro a la izquiera
            for xl in range(1, Ix - (Ix + area), -1):
                canvas[Iy, (Ix + xl)] = colors[
                    random.randint(0, len(colors) - 1)]

            #Siguiente fila
            Iy += 1

        #Si aun no ha llegado al centro sigue pintando
        if Iy < center[self.I]:

            #Pinta las filas en reversa
            index = -1
            for y in range(Iy, int(center[self.I])):
                if index < len(petalArea) * -1:
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
        #Angulo de rotacion por petalo
        rotation = 360 / qPetals

        #Posicion inicial en eje Y (Fila)
        #PosI = Posicion centro menos la distance del petalo ,mas numero aleatorio de pixeles
        posI = int((canvasSize/2) - petalDistance) + \
               random.randint(self.randomPositionRange[self.I], self.randomPositionRange[self.J])

        #Posicion inicial ene el eje X (Columna)
        #PosJ = Posicion centro mas numeoro aleatorio de pixeles
        posJ = int(canvasSize/2) + \
               random.randint(self.randomPositionRange[self.I], self.randomPositionRange[self.J])

        #Numeor de petalos a pintar
        for i in range(0, qPetals):
            #Dibuja el petalo
            self.drawPetal(petalArea, canvas, [posI, posJ], colors)
            #Angulo aleatorio
            randomAngle = random.randint(self.randomRotationRange[self.I], self.randomRotationRange[self.J])
            #Rota la imagen dado un angulo de rotacion
            canvas = ndimage.rotate(canvas, rotation + randomAngle, reshape=False)

        return canvas

    #Dibuja el centro de una flor
    def drawCenter(self, flowerCenterArea, colors, canvas, canvasSize):
        #Area que se debe pintar
        flowerCenterAreaCopy = flowerCenterArea.copy()

        #Centro de la imagen
        canvasCenter = [int(canvas.shape[self.I] / 2), int(canvas.shape[self.J] / 2)]

        #Distancia del petalo
        distance = canvasSize/DrawFlowerConfig.CANVAS_MULTIPLY_SIZE-DrawFlowerConfig.MARGIN

        #Distancia ideal del centro
        distanciaIdeal = distance * DrawFlowerConfig.CENTER_DISTANCE_PROPORTION

        #Disminucion que se debe aplicar
        disminucionAlto = 0

        #Si la distancia del centro es mayor a la distancia ideal
        #Se establece una disminucion
        if len(flowerCenterAreaCopy) > distanciaIdeal:
            disminucionAlto = \
                int(((len(flowerCenterAreaCopy)-distanciaIdeal)/len(flowerCenterArea))*100)

        #Recorre todas las filas del area del centro
        indexSize=0
        while(indexSize < len(flowerCenterAreaCopy)):

            #Disminuye de forma proporcional al tamaño del petalo la cantidad de pixeles de la fila
            flowerCenterAreaCopy[indexSize] = \
                int(((flowerCenterAreaCopy[indexSize]/distance)*distance * DrawFlowerConfig.CENTER_DISTANCE_PROPORTION))

            #Si se establecion una disminucion del alto.
            #Se toma un numero random
            #Disminucion del alto es una probabilidad de disminucion de una fila
            #Disminuir le alto es eliminar ciertas filas
            if disminucionAlto > 1 and random.randint(0, 100) < disminucionAlto:
                del flowerCenterAreaCopy[indexSize]
            else:
                indexSize += 1

        #Posicion inicial para pintar el centro
        flowerCenterSize = len(flowerCenterAreaCopy)
        initPosition = [int(canvasCenter[self.I]-flowerCenterSize), canvasCenter[self.J]]

        #Pinta la primera mitad del centro
        #Itera cada fila del area del centro
        Iy = initPosition[self.I]
        for size in flowerCenterAreaCopy:
            area = int(size / 2)

            #Pinta del centro a la derecha
            Ix = initPosition[self.J]
            for xr in range(1, area):
                canvas[Iy, (Ix + xr)] = colors[
                    random.randint(0, len(colors) - 1)]

            #Pinta del centro a la izquierda
            for xl in range(1, Ix - (Ix + area), -1):
                canvas[Iy, (Ix + xl)] = colors[
                    random.randint(0, len(colors) - 1)]

            Iy += 1

        #Pinta la otra mitad del centro
        flowerCenterAreaCopy.sort(reverse=True)
        for size in flowerCenterAreaCopy:
            area = int(size / 2)

            #Pinta del centro a ala derecha
            Ix = initPosition[self.J]
            for xr in range(1, area):
                canvas[Iy, (Ix + xr)] = colors[
                    random.randint(0, len(colors) - 1)]

            #Pinta del centro a la izquierda
            for xl in range(1, Ix - (Ix + area), -1):
                canvas[Iy, (Ix + xl)] = colors[
                    random.randint(0, len(colors) - 1)]

            Iy += 1

        return canvas

    #Dibuja la flor
    def drawFlower(self, petal, petalColors, center, centerColors):
        petalShape = petal.chromosomes[ChromosomeConfig.SHAPE]
        canvasSize = int((petalShape.distance+DrawFlowerConfig.MARGIN)*DrawFlowerConfig.CANVAS_MULTIPLY_SIZE)
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