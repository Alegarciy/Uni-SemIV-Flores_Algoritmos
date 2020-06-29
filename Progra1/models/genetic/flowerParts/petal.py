from models.genetic.flowerParts.flowerPart import FlowerPart

class Petal(FlowerPart):
    def __init__(self):
        super().__init__()

    def setFlowerPartImages(self, flowerImages):
        for flower in flowerImages:
            self.flowerPartImages.append(flower.getPetalPixels())

    def analyzeChromosome(self, chromosome):
        print("SOY UN PETALO")
        self.chromosomes[chromosome].analyzeDistribution(self.flowerPartImages)