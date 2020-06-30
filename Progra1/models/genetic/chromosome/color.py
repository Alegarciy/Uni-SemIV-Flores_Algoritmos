from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
from models.genetic.chromosome.Chromosome import Chromosome
from models.genetic.chromosome.GeneticChromosome import GeneticChromosome
from models.genetic.chromosome.analyzeInfoConfig import AnalyzeInfoConfig
import numpy as np

from abc import ABC, abstractmethod
import matplotlib
import webcolors
import math
from models.genetic.chromosome.Distribution import Distribution

class Color(GeneticChromosome):

    def __init__(self):
        super().__init__()
        self.__averageColorList = [] # [0,0,0] list of rgb
        self.__representationTable = None #Distribution type

    @staticmethod
    def colorDifference(color_rgb_1, color_rgb_2):
        rgb1 = sRGBColor(color_rgb_1[0], color_rgb_1[1], color_rgb_1[2])
        rgb2 = sRGBColor(color_rgb_2[0], color_rgb_2[1], color_rgb_2[2])
        color_lab_1 = convert_color(rgb1, LabColor)
        color_lab_2 = convert_color(rgb2, LabColor)
        d = delta_e_cie2000(color_lab_1, color_lab_2)
        return d

    def calculateAverageColor(self, colorList):
        size = len(colorList)
        accumulatedR = 0
        accumulatedG = 0
        accumulatedB = 0
        resultRGB = 0
        for color in colorList:
            accumulatedR += color[0]
            accumulatedG += color[1]
            accumulatedB += color[2]
        
        resultRGB = [math.floor(accumulatedR/size), math.floor(accumulatedG/size), math.floor(accumulatedB/size)]
        return resultRGB

    
    def analyzeDistributionList(self, pixelList, flowerNumber):
        
        currentDifference = 0
        currentList = []
        for pixel in pixelList:
            if(currentDifference != pixel.getIdealDiference()):
                #averageColor = self.calculateAverageColor(currentList)
                self.__averageColorList.append([currentList,len(currentList),flowerNumber, currentDifference])
                currentList = []
                currentDifference += 1
            currentList.append(pixel.getRGB())
        print(len(self.__averageColorList))


    def createDistributionTable(self, avergeColorList, numElements, binaryRepresentation):
        # Average color list compostion: [RGB Subgroup, times it appears, currentFlower, currentDifference]
        # distributionTable : [RGB Subgroup, Distribution]
        minimun = 0
        distributionTable = []
        currentDistribution = None
        for subgroup in avergeColorList:
            # Set distribution
            currentDistribution = Distribution()
            currentDistribution.setTotal(binaryRepresentation)
            currentDistribution.setQuantity(subgroup[1]) # subgroup size
            print(minimun)
            currentDistribution.setPercentage(numElements) # %
            print(minimun)
            currentDistribution.setRange(minimun) 
            print(minimun)
            minimun = math.floor((currentDistribution.getRangeMax()))
            print(minimun)
            # Append to distribution table
            distributionTable.append([subgroup[0], currentDistribution])
        return distributionTable



    #define abstract method
    def analyzeDistribution(self, flowerPartPixels, flowerPartImageInfo): #Como creo la tabla de distribucion para los coleres

        print("analyze COLOR")
        floweNumber = 0
        numElements = 0
        for pixelList in flowerPartPixels:
            #Store data in variable self.__averageColorList
            self.analyzeDistributionList(pixelList, floweNumber)
            numElements += len(pixelList)
            floweNumber += 1

        #Create a distribution table 
        print('TACO MINIMO') 
        print(numElements)     
        self.__representationTable = self.createDistributionTable(self.__averageColorList, numElements, 65535) #Numero magico
        print('TACO MEDIO')   
        for element in self.__representationTable:
           element[1].print()
        #print(len(self.__representationTable))
        print('TACO MAXIMO')   

        
        #print('TACO MAXIMO')
        #for element in self.__averageColorList:
        #print(element[0], element[1], element[2], element[3])
        #print(self.chromosomeDistribution)

        self.setAnalyzeInfo()
        return self.analyzeInfo

    def setAnalyzeInfo(self):
        images = []
        index = 1
        images.append([np.zeros([1000, 1000, 3], dtype=np.uint8), "Colors"])
        self.analyzeInfo[AnalyzeInfoConfig.DESCRIPTION] = "Colores del "
        self.analyzeInfo[AnalyzeInfoConfig.IMAGES] = images


    #Define abstract method
    def fitness(self):
        pass
