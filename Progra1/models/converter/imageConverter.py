from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('Agg')
import numpy as np
from skimage import io
import io as i_o
import base64
from models.fileManager.config import Config
from models.fileManager.fileManager import FileManager
from models.converter.flowerImage import FlowerImage
from models.converter.flowerConfig import FlowerConfig
from models.genetic.chromosome.color import Color
from models.converter.pixelFlower import PixelFlower
import math

class ImageConverter:

    def __init__(self): 
        # Array de flower images
        self.userImages = []
        self.I = 0
        self.J = 1
        # Current image analized
        self.imageIndex = 0
        self.step = 0
        self.total = 0
        self.progress = 0
        self.isRunning = False
        self.finished = False

    def isReadyToConvert(self):
        if(len(self.userImages)  >= 1 and not self.isRunning):
            return True
        return False

    #El usuario agrega una nueva flor
    def addImage(self, image, jsonData, filename, extension):
        numberFlower = len(self.userImages)
        flowerDirectory = Config.DATADIRECTORY + "/" + filename
        #Save Flower image

        flowerFilename = Config.IMAGEFILENAME + "." + extension
        FlowerImagePathBackEnd = FileManager.save_image(image, flowerDirectory, flowerFilename)

        flowerFolder = Config.STATICFOLDER + "/" + Config.USERINPUTFOLDER + "/" + filename
        flowerImagePathFrontEnd = flowerFolder + "/" + flowerFilename

        #Save Json Data
        jsonFilename = Config.JSONFILENAME + Config.JSONEXTENSION
        FileManager.save_json(jsonData, flowerDirectory, jsonFilename)

        #Read
        jsonDirectory = flowerDirectory + "/" + jsonFilename
        json = FileManager.read_json(jsonDirectory)

        #Transform image in Numpy.array
        image = io.imread(FlowerImagePathBackEnd)

        flowerDirectory.replace("/", "\\")
        #Create flowerImage instance
        flowerImage = FlowerImage(image, flowerImagePathFrontEnd, FlowerImagePathBackEnd, json, flowerDirectory, filename)

        #Add flower image to userInput list
        self.userImages.append(flowerImage)

        self.finished = False

    #El usuario elimina una imagen que subió
    def deleteImage(self, position):
        flower = self.userImages[position]
        FileManager.removeDirectory(flower.getFlowerDirectory())
        self.userImages.remove(flower)
        self.finished = False

    #Recorre las imagenes del usuario (numpy arrays) y llama al voraz
    def convert(self):
        #image index indica la flor que se esta procesando con el voraz
        #is running indica que el voraz está trabajando
        self.isRunning = True
        self.imageIndex = 0
        flowerNumber = 0
        for flowerImage in self.userImages:
            self.convertImage(flowerImage, flowerNumber)
            self.imageIndex += 1
            flowerNumber += 1

        #Verifica si el proceso voraz terminó con exito
        if(self.imageIndex>=len(self.userImages)>0):
            self.finished = True
        else:
            self.finished = False
        self.isRunning = False
        plt.close('all')

    #Algoritmo voraz
    def convertImage(self, flowerImage, flowerNumber):
        #Datos de la flor
        info = flowerImage.getJsonData()
        flowerPixels = flowerImage.getFlower() #Subestructura
        size_i = flowerImage.getSize_I()
        size_j = flowerImage.getSize_J()

        # Dictionaries of colors
        # Inside is indexDic for each color
        colorDicPetal = {}
        colorDicCenter = {}

        indexDicPetals = {}
        indexDicCenter = {}
        self.total = size_j*size_i

        for i in range(0, size_i-1):
            for j in range(0, size_j-1):

                self.step = (i*size_i + (j+1)) #Etapa
                self.progress = (self.step / self.total)*100 #Porcentaje del proceso

                #SI ES UN PIXEL DE CENTRO
                #Se verfica que esté dentro del area requerida
                if self.isInCenter(i, j, info):
                    #Se obtiene la diferencia de color
                    centerColorDif = self.getCenterColorDif(flowerPixels[i, j], info)

                    if(centerColorDif[0] <= info[FlowerConfig.CENTER_DIFFERENCE_COLOR_LIMIT]):
                        center = flowerImage.getCenter()
                        center[i, j] = flowerPixels[i, j]
                        centerPixels = flowerImage.getCenterPixels()

                        if math.floor(centerColorDif[0]) not in indexDicCenter:
                            centerPixels.append(PixelFlower(flowerPixels[i, j], math.floor(centerColorDif[0]), (i, j), flowerNumber))
                            indexDicCenter[math.floor(centerColorDif[0])] = len(centerPixels) - 1 #last item inserted

                        else:# if key is inserted
                            index = indexDicCenter[math.floor(centerColorDif[0])]
                            centerPixels[index].incrementQuantity()

                #SI ES UN PIXEL DEL PETALO
                elif(self.isInPetal(i,j,info)): #Criterio
                    petalColorDif = self.getPetalColorDif(flowerPixels[i, j], info) # [dif, clrIndex]

                    if(petalColorDif[0] <= info[FlowerConfig.PETAL_DIFFERENCE_COLOR_LIMIT]):
                        petal = flowerImage.getPetal()
                        petal[i, j] = flowerPixels[i, j]
                        petalPixels = flowerImage.getPetalPixels()

                        #If there is no color dic of clrIndex (COLOR)
                        if petalColorDif[1] not in colorDicPetal:
                            print(petalColorDif[1])
                            colorDicPetal[petalColorDif[1]] = {}

                        # (COLOR DIFFERENCE)
                        if math.floor(petalColorDif[0]) not in colorDicPetal[petalColorDif[1]]:
                            petalPixels.append(PixelFlower(flowerPixels[i, j], math.floor(petalColorDif[0]), (i, j), flowerNumber))
                            colorDicPetal[petalColorDif[1]][math.floor(petalColorDif[0])] = len(petalPixels) - 1 #last item inserted
                            #print(colorDicPetal)
                        else:# if key is inserted
                            index = colorDicPetal[petalColorDif[1]][math.floor(petalColorDif[0])]
                            petalPixels[index].incrementQuantity()
                            #print(colorDicPetal)
                            
        flowerImage.sortByDifference()

    #Verifica si el pixel está dentro del area requerida para el centro
    def isInCenter(self, i, j, info):
        minI = info[FlowerConfig.PIXEL_CENTRAL][self.I] - info[FlowerConfig.PIXEL_CENTER_LIMIT][self.I]
        maxI = info[FlowerConfig.PIXEL_CENTRAL][self.I] + info[FlowerConfig.PIXEL_CENTER_LIMIT][self.I]
        minJ = info[FlowerConfig.PIXEL_CENTRAL][self.J] - info[FlowerConfig.PIXEL_CENTER_LIMIT][self.J]
        maxJ = info[FlowerConfig.PIXEL_CENTRAL][self.J] + info[FlowerConfig.PIXEL_CENTER_LIMIT][self.J]

        return (minI < i < maxI and minJ < j < maxJ)

    #Verifica si el pixel esta dentro del area requerida para el petalo
    def isInPetal(self, i, j, info):
        minI = info[FlowerConfig.PIXEL_CENTRAL][self.I] - info[FlowerConfig.PIXEL_PETAL_LIMIT][self.I]
        maxI = info[FlowerConfig.PIXEL_CENTRAL][self.I] + info[FlowerConfig.PIXEL_PETAL_LIMIT][self.I]
        minJ = info[FlowerConfig.PIXEL_CENTRAL][self.J] - info[FlowerConfig.PIXEL_PETAL_LIMIT][self.J]
        maxJ = info[FlowerConfig.PIXEL_CENTRAL][self.J] + info[FlowerConfig.PIXEL_PETAL_LIMIT][self.J]

        return (minI < i < maxI and minJ < j < maxJ)

    #Diferencia de color para el petalo
    def getPetalColorDif(self, pixel, info):
        listOfColors = info[FlowerConfig.COLOR_PETAL_PREF]
        colorSelected = []
        minDifference = 0
        index = 0

        #Calcula la diferencia con cada color que venga en el .Json
        for color in listOfColors:
            dif = Color.colorDifference(pixel, color)
            selected = [dif, index]

            #Siempre busca el color con el que tenga la menor diferencia
            if(minDifference == 0 or dif <= minDifference):
                colorSelected = selected
                minDifference = dif
            index += 1

        colorSelected[1] = math.floor(colorSelected[1])
        colorSelected[0] = math.floor(colorSelected[0])
        return colorSelected

    #Diferencia de color para el centro
    def getCenterColorDif(self, pixel, info):
        listOfColors = info[FlowerConfig.COLOR_CENTER_PREF]
        colorSelected = []
        minDifference = 0
        index = 0
        for color in listOfColors:
            dif = Color.colorDifference(pixel, color)
            selected = [dif, index]
            if (minDifference == 0 or dif <= minDifference):
                colorSelected = selected
                minDifference = dif
            index += 1
        return colorSelected

    #Muestra el proceso del voraz creando una imagen
    def getConvertProcess(self):
        if(self.imageIndex >= len(self.userImages)):
            return "False"

        #Configura el subplot
        flowerImage = self.userImages[self.imageIndex]
        images = [flowerImage.getFlower(), flowerImage.getPetal(), flowerImage.getCenter()]
        titles = ["Flower", "Petal", "Center"]
        fig, axs = plt.subplots(1, 3, figsize=(8, 4), constrained_layout=True)
        fig.patch.set_visible(False)
        for ax, image, title in zip(axs, images, titles):
            ax.imshow(image)
            ax.set_title(title)
            ax.axis('off')

        #convierte la imagen a base 64
        img = i_o.BytesIO()
        plt.savefig(img, format="png")
        img.seek(0)
        base64_plot = base64.b64encode(img.getvalue()).decode()
        plt.clf()

        return base64_plot

    def getProgress(self):
        print(str(self.progress))
        return str(int(self.progress))

    def getTotal(self):
        return self.total

    def getCurrentStep(self):
        return self.step