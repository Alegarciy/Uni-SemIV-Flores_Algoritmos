#import cv2
from matplotlib import pyplot as plt
import numpy as np
from models.config import Config
from models.fileManager import FileManager
class ImageConverter:

    def __init__(self):
        self.userImages = []

    def addImage(self, image, jsonData):
        numberFlower = len(self.userImages)
        flowerDirectory = Config.FLOWERFOLDER + str(numberFlower) + "/"
        flowerFilename = Config.IMAGEFILENAME + str(numberFlower)
        flowerImageDir = FileManager.save_image(image, flowerDirectory, flowerFilename)


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