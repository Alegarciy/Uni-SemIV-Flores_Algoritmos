import random
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt

class DrawFlower:
    def __init__(self):
        self.I = 0
        self.J = 1
        self.randomRotationRange = [-10, 10]
        self.randomPositionRange = [-10, 10]
        self.margin = 25
    
    def drawPetal(self, petalArea, canvas, position, colors):
        center = [int(canvas.shape[self.I] / 2), int(canvas.shape[self.J] / 2)]

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
        return canvas

    def drawFlowerPetals(self, petalArea, qPetals, colors, petalDistance):
        canvasSize = int((petalDistance+self.margin)*2)
        canvas = np.zeros([canvasSize, canvasSize, 3], dtype=np.uint8)
        rotation = 360 / qPetals
        posI = int((canvasSize/2) - petalDistance) + random.randint(self.randomPositionRange[self.I], self.randomPositionRange[self.J])
        posJ = int(canvasSize/2) + random.randint(self.randomPositionRange[self.I], self.randomPositionRange[self.J])

        for i in range(0, qPetals):
            self.drawPetal(petalArea, canvas, [posI, posJ], colors)
            incertidumbre = random.randint(self.randomRotationRange[self.I], self.randomRotationRange[self.J])
            canvas = ndimage.rotate(canvas, rotation + incertidumbre, reshape=False)

        plt.imshow(canvas)
        plt.show()
        return canvas


    def drawFlower(self, petalArea, qPetals, colors, petalDistance):
        return self.drawFlowerPetals(petalArea, qPetals, colors, petalDistance)