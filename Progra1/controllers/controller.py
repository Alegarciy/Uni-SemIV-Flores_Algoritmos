from models.converter.imageConverter import ImageConverter
from models.converter.flowerImage import FlowerImage
from models.analyzer.imageAnalyzer import ImageAnalyzer
from models.genetic.chromosome.chromosomeConfig import ChromosomeConfig
from models.genetic.flowerParts.flowerPartConfig import FlowerPartConfig
from models.genetic.genetic import Genetic
class Controller:

        imageConverter = ImageConverter()
        imageAnalyzer = ImageAnalyzer()
        genetic = Genetic()

        #Image Converted methods
        @staticmethod
        def loadImage(image, jsonData, filename, ext):
            Controller.imageConverter.addImage(image, jsonData, filename, ext)

        @staticmethod
        def deleteImage(position):
            Controller.imageConverter.deleteImage(position)

        @staticmethod
        def getListLoadedImages():
            return Controller.imageConverter.userImages

        @staticmethod
        def startProcess():
            Controller.imageConverter.convert()

        @staticmethod
        def getConvertProcess():
            return Controller.imageConverter.getConvertProcess()

        @staticmethod
        def isConvertRunning():
            return Controller.imageConverter.isRunning

        @staticmethod
        def isConvertFinished():
            return Controller.imageConverter.finished

        @staticmethod
        def isReadyToConvert():
            return Controller.imageConverter.isReadyToConvert()

        @staticmethod
        def getConvertProgress():
            return Controller.imageConverter.getProgress()

        @staticmethod
        def getTotalSteps():
            return Controller.imageConverter.getTotal()

        @staticmethod
        def getCurrentStep():
            return Controller.imageConverter.getCurrentStep()

        #--------------------------------------------------------#
        #Image analyzer method
        @staticmethod
        def setImageAnayzer():
            Controller.imageAnalyzer.setAnalyzer(Controller.imageConverter.userImages)
            markup = Controller.imageAnalyzer.analyze()
            return markup

            #Controller.setGenetic()

        @staticmethod
        def setGenetic():
            Controller.genetic.setGenetic(Controller.imageAnalyzer.getFlowerParts())

            #Controller.genetic.draw()