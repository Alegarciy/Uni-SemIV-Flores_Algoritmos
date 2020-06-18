from cv2 import cv2 
import numpy as np
from matplotlib import pyplot as plt

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