from models.genetic.flowerParts.flowerPart import FlowerPart
class Center(FlowerPart):
    def __init__(self):
        super().__init__()

    def setFlowerPartImages(self, flowerImages):
        for flower in flowerImages:
            self.flowerPartImages.append(flower.getCenter())

    def analyzeChromosome(self, chromosome):
        print("SOY UN CENTRO")
        self.chromosomes[chromosome].analyzeDistribution(self.flowerPartImages)
