from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
from models.genetic.chromosome.Chromosome import Chromosome
from models.genetic.chromosome.GeneticChromosome import GeneticChromosome
from models.genetic.chromosome.analyzeInfoConfig import AnalyzeInfoConfig
from models.genetic.algorithm.individual import Individual
import numpy as np

from abc import ABC, abstractmethod
import matplotlib
import webcolors
import math
from models.genetic.chromosome.Distribution import Distribution

from models.genetic.chromosome.chromosomeConfig import ChromosomeConfig

class Color(GeneticChromosome):

    def __init__(self):
        super().__init__()
        self.__averageColorList = [] # [0,0,0] list of rgb
        self.__representationTable = None #Distribution type
        self.__idealFitness = None # Needed for fitness comparison
        self.__dominantColors = [] #it can be just one color [[RGB], Quantity]

    @staticmethod
    def colorDifference(color_rgb_1, color_rgb_2):
        rgb1 = sRGBColor(color_rgb_1[0], color_rgb_1[1], color_rgb_1[2])
        rgb2 = sRGBColor(color_rgb_2[0], color_rgb_2[1], color_rgb_2[2])
        color_lab_1 = convert_color(rgb1, LabColor)
        color_lab_2 = convert_color(rgb2, LabColor)
        d = delta_e_cie2000(color_lab_1, color_lab_2)
        return d

    #Give formated information to class vatiable "averageColorList"
    def analyzeDistributionList(self, colorList, flowerNumber):
        for colorPixel in colorList:
            self.__averageColorList.append([colorPixel.getRGB(),colorPixel.getQuantity(),flowerNumber,colorPixel.getIdealDiference()])

    # Average color list compostion: [RGB Subgroup, times it appears, currentFlower,   ((x)) currentDifference]
    # distributionTable : [RGB Subgroup, Distribution]
    def createDistributionTable(self, avergeColorList, numElements, binaryRepresentation):
        minimun = 0
        distributionTable = []
        currentDistribution = None
        for color in avergeColorList:
            # Set distribution
            currentDistribution = Distribution()
            currentDistribution.setTotal(binaryRepresentation)
            currentDistribution.setQuantity(color[1]) # color size
            currentDistribution.setPercentage(numElements) # %
            currentDistribution.setRange(minimun) 
            minimun = math.floor((currentDistribution.getRangeMax())) + 1
            if(color is avergeColorList[-1]):
                currentDistribution.setMaxRange(binaryRepresentation)
            # Append to distribution table
            distributionTable.append([color[0], currentDistribution])
        return distributionTable

    # Get dominant colors on the chromosome color
    def defineDominantColors(self, dominantColorQuantity):
        distributionTable = []
        indexTemp = 0
	    #Read desired data from representation table
        for element in self.__representationTable:
            distributionTable.append([element[0], element[1].getQuantity()])
	    #Sort base on second row(quantity)
        quantity = lambda distributionTable: distributionTable[1]
        distributionTable.sort(key=quantity, reverse =True)
	    #Set desired colors of dominance
        while(dominantColorQuantity > 0):
            dominantColorQuantity -= 1
            self.__dominantColors.append(distributionTable[indexTemp])
            indexTemp += 1
        for element in self.__dominantColors:
            print("Dominant color:", element[0])

    #Get data from distribution table
    def findRange(self, value):
        for rangedValue in self.__representationTable:
            if(rangedValue[1].getRangeMin() <= value and rangedValue[1].getRangeMax() >= value):
                return rangedValue[0]
        print('No se encontro rango')
        return self.__representationTable[0][0]
        

    #Calcultated the fitness of an individual
    #Stores the resullt on individual
    def fitness(self, individual):
        range = individual.getIntValue()
        print('Gene: ',individual.getGene())
        print('Gene value: ',range)
        color = self.findRange(range)
        print('Gene color: ',color)
        fitnessValue = 0
        for dominantColor in self.__dominantColors:
            print('Dominant color: ',dominantColor[0])
            fitnessValue += Color.colorDifference(color,dominantColor[0])
        print('Fitness value: ', fitnessValue)
        individual.setFitness(fitnessValue)


    #define abstract method
    def analyzeDistribution(self, flowerPartPixels, flowerPartImageInfo): #Como creo la tabla de distribucion para los coleres
        print("analyze COLOR")
        floweNumber = 0
        numElements = 0
        for colorList in flowerPartPixels:
            #Store data in variable self.__averageColorList
            self.analyzeDistributionList(colorList, floweNumber)
            for colorPixels in colorList:
                numElements += colorPixels.getQuantity()
            floweNumber += 1

        #Create distribution table
        self.__representationTable = self.createDistributionTable(self.__averageColorList, numElements, 65535) #Numero magico  

        #Print the distribution table  
        for element in self.__representationTable:
           print("Color:", element[0], end=" ")
           element[1].print()

        #Get dominant colors or color
        print("BROWN KNEE")
        self.defineDominantColors(ChromosomeConfig.DOMINANT_COLORS)

        #Test individual
        individual = Individual()
        print('LET FITNESS BEGIN')
        self.fitness(individual)
        print('LET FITNESS END')
        

        self.setAnalyzeInfo()
        return self.analyzeInfo



    # Give the browser a representation of the flowerPart color
    def setAnalyzeInfo(self):
        images = [] #array
        index = 1
        images.append([np.zeros([1000, 1000, 3], dtype=np.uint8), "Colors"]) #images[0]
        distributionTemp = self.__representationTable
        paintDistribution = []
        totalLength = 1000 * 1000

        #Make color distribution table for image
        for element in distributionTemp:
            paintDistribution.append([element[0],math.floor(totalLength * element[1].getPercentage() / 100)])

        paintDistributionIndx = 0

        # Fill with color mathplot representation      
        for x in range(0,1000):
            for y in range(0, 1000):
                if(paintDistributionIndx < len(paintDistribution) - 1 and paintDistribution[paintDistributionIndx][1] <= 0):
                    paintDistributionIndx += 1
                images[0][0][y][x] = paintDistribution[paintDistributionIndx][0] #Blue
                paintDistribution[paintDistributionIndx][1] -= 1
                
                

        self.analyzeInfo[AnalyzeInfoConfig.DESCRIPTION] = "Colores del "
        self.analyzeInfo[AnalyzeInfoConfig.IMAGES] = images



