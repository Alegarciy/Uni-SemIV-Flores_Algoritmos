from models.genetic.flowerParts.flowerPart import FlowerPart
from models.genetic.flowerParts.flowerPartConfig import FlowerPartConfig
from models.converter.flowerConfig import FlowerConfig

class Petal(FlowerPart):
    def __init__(self):
        super().__init__()
        self.quantity = 0

    def setFlowerPartImages(self, flowerImages):
        for flower in flowerImages:
            self.flowerPartPixels.append(flower.getPetalPixels())
            jsonInfo = flower.getJsonData()
            info =\
                {
                    FlowerPartConfig.PIXEL_CENTRAL: jsonInfo[FlowerConfig.PIXEL_CENTRAL],
                    FlowerPartConfig.FLOWERPART_LIMIT: jsonInfo[FlowerConfig.PIXEL_PETAL_LIMIT],
                    FlowerPartConfig.FLOWERPART_OUTLINE_INIT_POS: jsonInfo[FlowerConfig.PETAL_OUTLINE_INIT_POS],
                    FlowerPartConfig.FLOWERPART_OUTLINE_END_POS: jsonInfo[FlowerConfig.PETAL_OUTLINE_END_POS],
                    FlowerPartConfig.FLOWERPART_OUTLINE_INCREASEY: jsonInfo[FlowerConfig.OUTLINE_INCREASEY],
                    FlowerPartConfig.QUANTITY_FLOWERPART: jsonInfo[FlowerConfig.CTD_PETALOS]
                }
            self.flowerPartImageInfo.append([flower.getPetal(), info])

    def analyzeQuantityOfPetals(self):
        self.quantity = 0
        for flowerInfo in self.flowerPartImageInfo:
            info = flowerInfo[1]
            self.quantity += info[FlowerPartConfig.QUANTITY_FLOWERPART]
        self.quantity = int(self.quantity/len(self.flowerPartImageInfo))


    def analyzeChromosome(self, chromosome):
        self.chromosomes[chromosome].analyzeDistribution(self.flowerPartPixels, self.flowerPartImageInfo)
        self.analyzeQuantityOfPetals()