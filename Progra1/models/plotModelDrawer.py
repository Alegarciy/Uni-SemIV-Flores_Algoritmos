from flask import Markup
from matplotlib import pyplot as plt
import io as i_o
import base64
class PlotModelDrawer:

    @staticmethod
    #Crea un plot de la imagen
    def draw(image, title):
        #Configura el subplot
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.imshow(image)
        ax.set_title(title)
        fig.patch.set_visible(False)
        ax.axis('off')

        #Convierte la imagen a base 64
        img = i_o.BytesIO()
        plt.savefig(img, format="png")
        img.seek(0)
        base64_plot = base64.b64encode(img.getvalue()).decode()
        plt.clf()
        return base64_plot

    @staticmethod
    #Crea elementos HTML para mostrar en la Vista web
    def createMarkup(base64_plot, description, classname):
        divInit = Markup('<div class="{}">'.format(classname))
        title = Markup('<h4 class="my-2">{}</h4>'.format(description))
        divImageInit = Markup('<div>')
        divEnd = Markup('</div>')

        #Itera sobre las imagenes y las agrega a una etiqueta <img>
        images = ""
        for plot in base64_plot:
            images += Markup('<img src="data:image/png;base64,{}" class="img-fluid" alt="Responsive image" width: 320px; height: 244px>'.format(plot))
            images += "\n"

        markup = divInit + "\n" + title + "\n" + divImageInit + "\n" + images + "\n" + divEnd + "\n" + divEnd + "\n"
        return markup

    @staticmethod
    #Crea elemnto HTMl para mostrar informacion del proceso genetico
    def createInfoMarkup(geneticInfo, classname):
        #info -> "description : value"

        divInit = Markup('<div class="{}">'.format(classname))
        text = ""
        #Itera sobre el texto y lo agrega a una etiqueta <h4>
        for info in geneticInfo:
            text += Markup('<h4 class="my-2">{}</h4>'.format(info)) + "\n"
        divEnd = Markup('</div>')

        markup = divInit + "\n" + text + "\n" + divEnd + "\n"
        return markup
