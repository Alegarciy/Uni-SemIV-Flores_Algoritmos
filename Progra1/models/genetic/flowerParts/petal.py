from models.genetic.flowerParts.flowerPart import FlowerPart

class Petal(FlowerPart):
    def __init__(self):
        super().__init__()

    def setFlowerPartImages(self, flowerImages):
        for flower in flowerImages:
            self.flowerPartImages.append(flower.getPetal())

    def analyzeChromosome(self, chromosome):
        self.chromosomes[chromosome].analyzeDistribution(self.flowerPartImages)