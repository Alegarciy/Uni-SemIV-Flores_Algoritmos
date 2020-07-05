from flask import Markup
from matplotlib import pyplot as plt
import io as i_o
import base64
# hola soy un comentario para hacer commit
class PlotModelDrawer:

    @staticmethod
    def draw(image, title):
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.imshow(image)
        ax.set_title(title)
        fig.patch.set_visible(False)
        ax.axis('off')

        img = i_o.BytesIO()
        plt.savefig(img, format="png")
        img.seek(0)
        base64_plot = base64.b64encode(img.getvalue()).decode()
        plt.clf()

        return base64_plot

    @staticmethod
    def createMarkup(base64_plot, description, classname):
        divInit = Markup('<div class="{}">'.format(classname))
        title = Markup('<h4 class="my-2">{}</h4>'.format(description))
        divImageInit = Markup('<div>')
        divEnd = Markup('</div>')

        images = ""
        for plot in base64_plot:
            images += Markup('<img src="data:image/png;base64,{}" class="img-fluid" alt="Responsive image" width: 320px; height: 244px>'.format(plot))
            images += "\n"

        markup = divInit + "\n" + title + "\n" + divImageInit + "\n" + images + "\n" + divEnd + "\n" + divEnd + "\n"
        print(markup)
        return markup