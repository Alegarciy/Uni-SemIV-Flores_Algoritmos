class FlowerConfig:
    #(R,G,B)
    COLOR_PETAL_PREF = "colorPetaloPreferido"
    COLOR_CENTER_PREF = "colorCentroPreferido"
    PETAL_DIFFERENCE_COLOR_LIMIT = "petalColorDifference"
    CENTER_DIFFERENCE_COLOR_LIMIT = "centerColorDifference"
    CTD_PETALOS = "numeroPetalos"

    #(i,j)
    PIXEL_PETAL_LIMIT = "pixelPetaloMasAlejado" #Distancia del centro al limite en pixeles q
    PIXEL_CENTER_LIMIT = "pixelCentroMasAlejado"
    PIXEL_CENTRAL = "pixelCentral"

    #outline positions init
    PETAL_OUTLINE_INIT_POS = "petalOutlineInitPos"
    CENTER_OUTLINE_INIT_POS = "centerOutlineInitPos"

    #outline positions end
    PETAL_OUTLINE_END_POS = "petalOutlineEndPos"
    CENTER_OUTLINE_END_POS = "centerOutlineEndPos"
    PETAL_OUTLINE_INCREASE = "petalOutlineIncrease"
    CENTER_OUTLINE_INCREASE = "centerOutlineIncrease"
    PETAL_OUTLINE_AXIS = "petalOutlineAxis"
    CENTER_OUTLINE_AXIS = "centerOutlineAxis"


    #Convert image
    BACKGROUND_COLOR = (0,0,0) #Black
    OUTLINE_COLOR = (255,255,255) #White
    HIGHLIGHT_COLOR = (242, 255, 0)

