class FlowerConfig:
    #(R,G,B)
    COLOR_PETAL_PREF = "colorPetaloPreferido"
    COLOR_CENTER_PREF = "colorCentroPreferido"
    CTD_PETALOS = "numeroPetalos"

    #(i,j)
    PIXEL_PETAL_LIMIT = "pixelPetaloMasAlejado" #Distancia del centro al limite en pixeles q
    PIXEL_CENTER_LIMIT = "pixelCentroMasAlejado"
    PIXEL_CENTRAL = "pixelCentral"

    #Convert image
    BACKGROUND_COLOR = (0,0,0) #Black
    OUTLINE_COLOR = (255,255,255) #White
    DIFFERENCE_COLOR_LIMIT = 35
