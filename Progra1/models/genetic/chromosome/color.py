from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
from models.genetic.chromosome.Chromosome import Chromosome
from abc import ABC, abstractmethod

class Color(Chromosome):

    def __init__(self):
        super().__init__()

    @staticmethod
    def colorDifference(color_rgb_1, color_rgb_2):
        rgb1 = sRGBColor(color_rgb_1[0], color_rgb_1[1], color_rgb_1[2])
        rgb2 = sRGBColor(color_rgb_2[0], color_rgb_2[1], color_rgb_2[2])
        color_lab_1 = convert_color(rgb1, LabColor)
        color_lab_2 = convert_color(rgb2, LabColor)
        d = delta_e_cie2000(color_lab_1, color_lab_2)
        return d

    #define abstract method
    def analyzeDistribution(self, flowerPartsImages): #Como creo la tabla de distribucion para los coleres
        print("Soy color :o")

    def fitness(self):
        pass
