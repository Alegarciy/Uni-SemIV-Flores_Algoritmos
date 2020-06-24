#import cv2
from matplotlib import pyplot as plt
import numpy as np
from skimage import io
from models.config import Config
from models.fileManager import FileManager
from models.flowerImage import FlowerImage
from models.flowerConfig import FlowerConfig
from models.color import Color
class ImageConverter:



    def __init__(self):
        self.userImages = []
        self.I = 0;
        self.J = 1;

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

        #Just for debug
        plt.imshow(image)
        plt.show()

    def deleteImage(self, position):
        flower = self.userImages[position]
        FileManager.removeDirectory(flower.getFlowerDirectory())
        self.userImages.remove(flower)

    #Recorre las imagenes del usuario (numpy arrays) y llama al voraz
    def convert(self):
        for flowerImage in self.userImages:
            self.convertImage(flowerImage)
            plt.imshow(flowerImage.getPetal())
            plt.show()

    #Algoritmo voraz
    def convertImage(self, flowerImage):
        info = flowerImage.getJsonData()
        flowerPixels = flowerImage.getFlower() #Subestructura
        size_i = flowerImage.getSize_I()
        size_j = flowerImage.getSize_J()
        for i in range(0,size_i-1):
            for j in range(0, size_j-1):
                if(self.isInCenter(i,j,info)):
                    if(self.isCenterColor(flowerPixels[i,j], info)):
                        center = flowerImage.getCenter()
                        center[i,j] = flowerPixels[i,j]
                elif(self.isInPetal(i,j,info)):
                    if(self.isPetalColor(flowerPixels[i,j], info)):
                        petal = flowerImage.getPetal()
                        petal[i,j] = flowerPixels[i,j]

    #Criterios
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

    def isPetalColor(self, pixel, info):
        return Color.colorDifference(pixel, info[FlowerConfig.COLOR_PETAL_PREF]) <= FlowerConfig.DIFFERENCE_COLOR_LIMIT

    def isCenterColor(self, pixel, info):
        return Color.colorDifference(pixel, info[FlowerConfig.COLOR_CENTER_PREF]) <= FlowerConfig.DIFFERENCE_COLOR_LIMIT

    


    '''
img = cv2.imread("../app/images/imagen_01.png", cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=1)
lap = np.uint8(np.absolute(lap))

titles = ['image', 'Laplacian']
images = [img, lap]

for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

'''