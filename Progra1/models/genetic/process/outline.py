from models.genetic.chromosome.Chromosome import Chromosome
from models.genetic.flowerParts.flowerPartConfig import FlowerPartConfig
from models.converter.flowerConfig import FlowerConfig
from matplotlib import pyplot as plt

import numpy as np

class Outline:

    def __init__(self):
        self.INFO = 1
        self.IMAGE = 0
        self.I = 0
        self.J = 1

    #Verifica que el pixel este dentro del area requerida
    def isInflowerPart(self, i, j, info):
        minI = info[FlowerPartConfig.PIXEL_CENTRAL][self.I] - info[FlowerPartConfig.FLOWERPART_LIMIT][self.I]
        maxI = info[FlowerPartConfig.PIXEL_CENTRAL][self.I] + info[FlowerPartConfig.FLOWERPART_LIMIT][self.I]
        minJ = info[FlowerPartConfig.PIXEL_CENTRAL][self.J] - info[FlowerPartConfig.FLOWERPART_LIMIT][self.J]
        maxJ = info[FlowerPartConfig.PIXEL_CENTRAL][self.J] + info[FlowerPartConfig.FLOWERPART_LIMIT][self.J]

        return (minI < i < maxI and minJ < j < maxJ)

    #Crea la imagne del contorno
    def outlineProcess(self, flowerImageInfo):
        info = flowerImageInfo[self.INFO]
        flowerPart = flowerImageInfo[self.IMAGE]
        size_i = flowerPart.shape[0]
        size_j = flowerPart.shape[1]
        outlineImage = np.zeros([size_i, size_j, 3], dtype=np.uint8)

        for i in range(0, size_i - 1):
            for j in range(0, size_j - 1):
                if(self.isInflowerPart(i,j,info) and np.all(flowerPart[i,j] != FlowerConfig.BACKGROUND_COLOR)):
                    if ((i - 1 >= 0 and np.all(flowerPart[i - 1, j] == FlowerConfig.BACKGROUND_COLOR)) or
                        (i + 1 <= size_i and np.all(flowerPart[i + 1, j] == FlowerConfig.BACKGROUND_COLOR)) or
                        (j - 1 >= 0 and np.all(flowerPart[i, j-1] == FlowerConfig.BACKGROUND_COLOR)) or
                        (j + 1 <= size_j and np.all(flowerPart[i, j+1] == FlowerConfig.BACKGROUND_COLOR))):
                            outlineImage[i, j] = FlowerConfig.OUTLINE_COLOR
        return outlineImage
