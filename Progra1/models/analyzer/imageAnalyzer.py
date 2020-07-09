from models.genetic.flowerParts.petal import Petal
from models.genetic.flowerParts.center import Center
from models.genetic.chromosome.chromosomeConfig import ChromosomeConfig
from models.genetic.flowerParts.flowerPartConfig import FlowerPartConfig
from models.genetic.chromosome.analyzeInfoConfig import AnalyzeInfoConfig
from models.plotModelDrawer import PlotModelDrawer

class ImageAnalyzer:

    def __init__(self):
        self.__userImages = None
        self.__flowerParts = {}
        self.__flowerPartToAnalyze = None
        self.__chromosomeToAnalyze = ""
        self.__markup = ""
        self.finished = False

    def getUserImages(self):
        return self.__userImages

    def setAnalyzer(self, userImages): #Reinicia los datos
        self.finished = False
        self.__userImages = userImages
        self.__markup = ""
        petal = Petal()
        petal.setFlowerPartImages(userImages)
        center = Center()
        center.setFlowerPartImages(userImages)

        self.__flowerParts = \
        {
            FlowerPartConfig.PETAL: petal,
            FlowerPartConfig.CENTER: center
        }

    def setFlowerPartToAnalyze(self, FLOWERPART):
        self.__flowerPartToAnalyze = self.__flowerParts[FLOWERPART]

    def setChromosomeToAnalyze(self, CHROMOSOME):
        self.__chromosomeToAnalyze = CHROMOSOME

    #Analiza los datos obtenido del voraz
    def analyze(self):
        #Por cada Parte de la flor llama a analizar cada cromosoma
        for flowerKey in self.__flowerParts:
            flowerObject = self.__flowerParts[flowerKey]
            for chromosome in flowerObject.chromosomes:
                analysisInfo = flowerObject.analyzeChromosome(chromosome)
                self.cratePlotModels(analysisInfo, str(flowerKey+"-"+chromosome), flowerKey)

        self.finished = True
        return self.__markup

    #Crea las imagenes que muestran el resultado del analisis
    def cratePlotModels(self, analysisInfo, classname, flowerPart):
        base64_plots = []

        #Crea las imagenes decodificadas en Base 64
        for image_title in analysisInfo[AnalyzeInfoConfig.IMAGES]:
            base64_plots.append(PlotModelDrawer.draw(
                image_title[AnalyzeInfoConfig.IMAGE_PIXELS],
                image_title[AnalyzeInfoConfig.IMAGE_TITLE]))

        #Agrega las imagenes en conjunto de elementos Html
        self.__markup += \
            PlotModelDrawer.createMarkup(
            base64_plots,
            analysisInfo[AnalyzeInfoConfig.DESCRIPTION] + flowerPart,
            classname)

    def getFlowerParts(self):
        return self.__flowerParts

    def getMarkup(self):
        return self.__markup