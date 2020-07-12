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
        true = "True"
        false = "False"

        #----CONVERTE-----
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

        #------ANALYZER-------
        #Image analyzer method
        @staticmethod
        #Agrega los datos del voraz al annalizador que trabaja de forma sistematica
        def setImageAnayzer():
            if(Controller.imageConverter.finished):
                Controller.imageAnalyzer.setAnalyzer(Controller.imageConverter.userImages)
                markup = Controller.imageAnalyzer.analyze()
                return markup

            else:
                return Controller.false


        @staticmethod
        def getMarkup():
            return Controller.imageAnalyzer.getMarkup()


        #------GENETIC-------

        #Crear estructura del genetico y 'setear' los datos necesarios de las flores
        @staticmethod
        def setGenetic():
            if Controller.imageAnalyzer.finished:
                Controller.genetic.setGenetic(Controller.imageAnalyzer.getFlowerParts())
                return Controller.true
            else:
                return Controller.false

        #Iniciar o Reiniciar el genetico
        @staticmethod
        def startGenetic(flowerPartId):
            if flowerPartId == FlowerPartConfig.PETAL_ID:
                return Controller.genetic.start(FlowerPartConfig.PETAL, ChromosomeConfig.COLOR)
            if flowerPartId == FlowerPartConfig.CENTER_ID:
                return Controller.genetic.start(FlowerPartConfig.CENTER, ChromosomeConfig.COLOR)
            else:
                return Controller.false

        #Pausar o continuar el genetico
        @staticmethod
        def pauseGenetic(flowerPartId):
            if flowerPartId == FlowerPartConfig.PETAL_ID:
                return Controller.genetic.pause(FlowerPartConfig.PETAL)
            elif flowerPartId == FlowerPartConfig.CENTER_ID:
                return Controller.genetic.pause(FlowerPartConfig.CENTER)

            return Controller.false

        #Retorna representacion de la poblacion del genetico
        @staticmethod
        def showGenetic(flowerPartId):
            if flowerPartId == FlowerPartConfig.PETAL_ID:
                return Controller.genetic.drawProgress(FlowerPartConfig.PETAL)
            elif flowerPartId == FlowerPartConfig.CENTER_ID:
                return Controller.genetic.drawProgress(FlowerPartConfig.CENTER)

            return Controller.false

        #Muestra los datos del proceso genetico
        @staticmethod
        def showGeneticInfo(flowerPartId):
            if flowerPartId == FlowerPartConfig.PETAL_ID:
                return Controller.genetic.getGeneticInfo(FlowerPartConfig.PETAL)
            elif flowerPartId == FlowerPartConfig.CENTER_ID:
                return Controller.genetic.getGeneticInfo(FlowerPartConfig.CENTER)

            return Controller.false

        #Crea la flor nueva con base en la población del genetico
        @staticmethod
        def newFlower():
            return Controller.genetic.drawFlower()


        #Modifica el porcentaje de mutacion
        @staticmethod
        def modifyMutation(flowerPartId, mutationValue):
            if flowerPartId == FlowerPartConfig.PETAL_ID:
                return Controller.genetic.modifyMutationRate(FlowerPartConfig.PETAL, mutationValue)
            elif flowerPartId == FlowerPartConfig.CENTER_ID:
                return Controller.genetic.modifyMutationRate(FlowerPartConfig.CENTER, mutationValue)
            return Controller.false
