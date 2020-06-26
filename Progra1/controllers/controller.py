from models.imageConverter import ImageConverter
from models.flowerImage import FlowerImage
from models.imageAnalyzer import ImageAnalyzer
from models.genetic.chromosome.chromosomeConfig import ChromosomeConfig
from models.genetic.flowerParts.flowerPartConfig import FlowerPartConfig

class Controller:

        imageConverter = ImageConverter()
        imageAnalyzer = ImageAnalyzer()


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
        def isReadyToConvert():
            return Controller.imageConverter.isReadyToConvert()

        @staticmethod
        def getConvertProgress():
            return Controller.imageConverter.getProgress()

        #Image analyzer method
        @staticmethod
        def setImageAnayzer():
            Controller.imageAnalyzer.setAnalyzer(Controller.imageConverter.userImages)
            #POR EL MOMENTO PARA PRUEBA
            Controller.imageAnalyzer.setChromosomeToAnalyze(ChromosomeConfig.COLOR)
            Controller.imageAnalyzer.setFlowerPartToAnalyze(FlowerPartConfig.PETAL)
            Controller.imageAnalyzer.analyze()
