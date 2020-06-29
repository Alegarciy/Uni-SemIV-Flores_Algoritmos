#import cv2
from matplotlib import pyplot as plt
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

    def deleteImage(self, position):
        flower = self.userImages[position]
        FileManager.removeDirectory(flower.getFlowerDirectory())
        self.userImages.remove(flower)
        self.finished = False

    '''
    def normalizeCenterPoint(self, flowers):
        listSize_i = []
        listSize_j = []
        for flower in flowers:
            listSize_i.append(flower.getSize_I())
            listSize_j.append(flower.getSize_J())

        maxSize_i = max(listSize_i)
        maxSize_j = max(listSize_j)
        center = [maxSize_i/2, maxSize_j/2]
        allFlowers = np.zeros([maxSize_i, maxSize_j, 3], dtype=np.uint8)

        for flower in flowers:
            info = flower.getJsonData()
            flowerCenter = info[FlowerConfig.PIXEL_CENTRAL]
            differenceCenter = [center[self.I]-flowerCenter[self.I], center[self.J]-flowerCenter[self.J]]
            petal = flower.getPetal()
            size_i = flower.getSize_I()
            size_j = flower.getSize_J()
            for i in range(0, size_i - 1):
                for j in range(0, size_j - 1):
                    newI = (i + differenceCenter[self.I])
                    newJ = (j + differenceCenter[self.J])
                    print(str(newI) + " " + str(newJ))
                    if(np.all(petal[i, j] != FlowerConfig.BACKGROUND_COLOR) and newI < size_i-1 and newJ < size_j-1):
                        allFlowers[newI, newJ] = petal[i, j]

            plt.imshow(allFlowers)
            plt.show()

        return allFlowers
    '''

    def outline(self):
        #allFlowers = self.normalizeCenterPoint(self.userImages)
        for flower in self.userImages:
            outlineFlower = self.outlineProcess(flower)
            plt.imshow(outlineFlower)
            plt.show()
            plt.imsave("contorno2.png", outlineFlower)

    #Temporalmente situado en esta clase
    def outlineProcess(self, flower):
        info = flower.getJsonData()
        petal = flower.getPetal()
        size_i = flower.getSize_I()
        size_j = flower.getSize_J()
        outlineImage = np.zeros([size_i, size_j, 3], dtype=np.uint8)
        for i in range(0, size_i - 1):
            for j in range(0, size_j - 1):
                if(self.isInPetal(i,j,info) and np.all(petal[i,j] != FlowerConfig.BACKGROUND_COLOR)):
                    if ((i - 1 >= 0 and np.all(petal[i - 1, j] == FlowerConfig.BACKGROUND_COLOR)) or
                        (i + 1 <= size_i and np.all(petal[i + 1, j] == FlowerConfig.BACKGROUND_COLOR)) or
                        (j - 1 >= 0 and np.all(petal[i, j-1] == FlowerConfig.BACKGROUND_COLOR)) or
                        (j + 1 <= size_j and np.all(petal[i, j+1] == FlowerConfig.BACKGROUND_COLOR))):
                            outlineImage[i, j] = FlowerConfig.OUTLINE_COLOR
        return outlineImage


    #Recorre las imagenes del usuario (numpy arrays) y llama al voraz

    def convert(self):
        self.isRunning = True
        self.imageIndex = 0
        for flowerImage in self.userImages:
            self.convertImage(flowerImage)
            self.imageIndex += 1

        if(self.imageIndex>=len(self.userImages)>0):
            self.finished = True
        else:
            self.finished = False
        self.isRunning = False
        plt.close('all')


    #Algoritmo voraz

    def convertImage(self, flowerImage):
        info = flowerImage.getJsonData()
        flowerPixels = flowerImage.getFlower() #Subestructura
        size_i = flowerImage.getSize_I()
        size_j = flowerImage.getSize_J()
        self.total = size_j*size_i
        for i in range(0,size_i-1):
            for j in range(0, size_j-1):
                self.step = (i*size_i + (j+1))
                self.progress = (self.step / self.total)*100
                if(self.isInCenter(i,j,info)):

                    if(self.isCenterColor(flowerPixels[i,j], info)):
                        center = flowerImage.getCenter()
                        center[i,j] = flowerPixels[i,j]
                elif(self.isInPetal(i,j,info)): #Criterio
                    petalColorDif = self.getPetalColor(flowerPixels[i,j], info)
                    if(petalColorDif <= FlowerConfig.DIFFERENCE_COLOR_LIMIT):
                        petal = flowerImage.getPetal()
                        petalPixels = flowerImage.getPetalPixels()
                        petal[i,j] = flowerPixels[i,j]
                        pixelPetalFlower = PixelFlower(flowerPixels[i,j], math.floor(petalColorDif), (i,j))
                        petalPixels.append(pixelPetalFlower)
        flowerImage.sortByDifference()
    #Criterios espcificacion 

    def isInCenter(self, i, j, info):
        minI = info[FlowerConfig.PIXEL_CENTRAL][self.I] - info[FlowerConfig.PIXEL_CENTER_LIMIT][self.I]
        maxI = info[FlowerConfig.PIXEL_CENTRAL][self.I] + info[FlowerConfig.PIXEL_CENTER_LIMIT][self.I]
        minJ = info[FlowerConfig.PIXEL_CENTRAL][self.J] - info[FlowerConfig.PIXEL_CENTER_LIMIT][self.J]
        maxJ = info[FlowerConfig.PIXEL_CENTRAL][self.J] + info[FlowerConfig.PIXEL_CENTER_LIMIT][self.J]

        return (minI < i < maxI and minJ < j < maxJ)

    def isInPetal(self, i, j, info):
        minI = info[FlowerConfig.PIXEL_CENTRAL][self.I] - info[FlowerConfig.PIXEL_PETAL_LIMIT][self.I]
        maxI = info[FlowerConfig.PIXEL_CENTRAL][self.I] + info[FlowerConfig.PIXEL_PETAL_LIMIT][self.I]
        minJ = info[FlowerConfig.PIXEL_CENTRAL][self.J] - info[FlowerConfig.PIXEL_PETAL_LIMIT][self.J]
        maxJ = info[FlowerConfig.PIXEL_CENTRAL][self.J] + info[FlowerConfig.PIXEL_PETAL_LIMIT][self.J]

        return (minI < i < maxI and minJ < j < maxJ)

    def getPetalColor(self, pixel, info):
        return Color.colorDifference(pixel, info[FlowerConfig.COLOR_PETAL_PREF])

    def isCenterColor(self, pixel, info):
        return Color.colorDifference(pixel, info[FlowerConfig.COLOR_CENTER_PREF]) <= FlowerConfig.DIFFERENCE_COLOR_LIMIT

    def getConvertProcess(self):
        if(self.imageIndex >= len(self.userImages)):
            return "False"

        flowerImage = self.userImages[self.imageIndex]
        images = [flowerImage.getFlower(), flowerImage.getPetal(), flowerImage.getCenter()]
        titles = ["Flower", "Petal", "Center"]
        fig, axs = plt.subplots(1, 3, figsize=(10, 6), constrained_layout=True)
        for ax, image, title in zip(axs, images, titles):
            ax.imshow(image)
            ax.set_title(title)


        img = i_o.BytesIO()
        plt.savefig(img, format = "png")
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