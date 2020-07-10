from models.genetic.flowerParts.flowerPart import FlowerPart
from models.genetic.flowerParts.flowerPartConfig import FlowerPartConfig
from models.converter.flowerConfig import FlowerConfig

class Center(FlowerPart):
    def __init__(self):
        super().__init__()

    def setFlowerPartImages(self, flowerImages):
        for flower in flowerImages:
            self.flowerPartPixels.append(flower.getCenterPixels())
            jsonData = flower.getJsonData()
            info = \
                {
                    FlowerPartConfig.PIXEL_CENTRAL: jsonData[FlowerConfig.PIXEL_CENTRAL],
                    FlowerPartConfig.FLOWERPART_LIMIT: jsonData[FlowerConfig.PIXEL_CENTER_LIMIT],
                    FlowerPartConfig.FLOWERPART_OUTLINE_INIT_POS: jsonData[FlowerConfig.CENTER_OUTLINE_INIT_POS],
                    FlowerPartConfig.FLOWERPART_OUTLINE_END_POS: jsonData[FlowerConfig.CENTER_OUTLINE_END_POS],
                    FlowerPartConfig.FLOWERPART_OUTLINE_INCREASE: jsonData[FlowerConfig.CENTER_OUTLINE_INCREASE],
                    FlowerPartConfig.FLOWERPART_OUTLINE_AXIS: jsonData[FlowerConfig.CENTER_OUTLINE_AXIS]
                }

            self.flowerPartImageInfo.append([flower.getCenter(), info])

    def analyzeChromosome(self, chromosome):
        return self.chromosomes[chromosome].analyzeDistribution(self.flowerPartPixels, self.flowerPartImageInfo)
