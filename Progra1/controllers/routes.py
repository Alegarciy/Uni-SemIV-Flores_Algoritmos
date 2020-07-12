from flask import Flask, render_template, url_for, flash, Markup, redirect, request
from models.forms import ImageForm
from models.fileManager.fileManager import FileManager
#from controllers import app
from controllers.controller import Controller
import os
from models.fileManager.config import Config
import secrets


template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
template_dir = os.path.join(template_dir, 'Progra1')
template_dir = os.path.join(template_dir, 'app')
template_dir = os.path.join(template_dir, 'templates')
template_view_dir = os.path.join(template_dir, 'view')
static_dir = os.path.join(template_dir, Config.STATICFOLDER)

app = Flask(__name__, template_folder=template_view_dir, static_folder=static_dir)
app.config['SECRET_KEY'] = 'eb289e8e6629dd79004bf93963dc2933'

#DIRECTORIES
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
uploads_dir = os.path.join(template_dir, Config.STATICFOLDER)
uploads_dir = os.path.join(uploads_dir, Config.USERINPUTFOLDER)
Config.DATADIRECTORY = uploads_dir

#----RENDER VIEWS----
@app.route("/")
@app.route("/home")
def home():
    markup_ = Controller.getMarkup()
    return render_template('home.html', markup=markup_)

@app.route("/about")
def about():
    return render_template('about.html')

# ----- IMAGE UPLOAD ---------
#POST Method. El usuario carga una imagen/json de la flor
@app.route("/loadImage", methods = ["POST"])
def loadImage():
    if request.files:
        image = request.files["image"]
        json = request.files["json"]
        filename_ext = image.filename.rsplit(".", 1)
        ext = filename_ext[1]
        filename = filename_ext[0]
        if filename_ext[1].upper() in Config.EXTENSIONSALLOWED:
            Controller.loadImage(image, json, filename, ext)
        return redirect(url_for("upload"), code=302)

#El usuario elimina una imagen/json cargada anteriormente
@app.route("/deleteImage/<int:position>")
def deleteImage(position):
    Controller.deleteImage(position)
    return redirect(url_for("upload"), code=302)

#GET Pagina para que el usuario cargue las imagenes y datos
@app.route("/upload", methods=['GET'])
def upload():
    return render_template("upload_image.html", form=ImageForm(), userImages=Controller.getListLoadedImages(), maxInput=Config.MAXUSERINPUT)


# ----- IMAGE CONVERT ---------

@app.route("/isConvertRunning", methods=["GET"])
def isConvertRunning():
    return str(Controller.isConvertRunning())

@app.route("/isConvertFinished", methods=["GET"])
def isConvertFinished():
    return str(Controller.isConvertFinished())

@app.route("/convert", methods=["GET"])
def startConvertProcess():
    if Controller.isReadyToConvert():
        Controller.startProcess()
        return Controller.true
    return Controller.false

@app.route("/convertProcess", methods=["GET"])
def showConvertProcess():
    plot_url = Controller.getConvertProcess()
    if plot_url == Controller.false:
        return Controller.false

    #HTML element
    model_plot = Markup('<img src="data:image/png;base64,{}" class="img-fluid" alt="Responsive image" width: 360px; height: 288px>'.format(plot_url))
    return model_plot

@app.route("/convertProgress", methods=["GET"])
def showConvertProgressBar():
    progress = Controller.getConvertProgress()
    return progress

@app.route("/totalSteps", methods=["GET"])
def showTotalSteps():
    return str(Controller.getTotalSteps())

@app.route("/currentStep", methods=["GET"])
def showCurrentStep():
    return str(Controller.getCurrentStep())

# ----- IMAGE ANALYZER ---------

@app.route("/analyze", methods=["GET"])
def analyze():
    markup = Controller.setImageAnayzer()
    return markup

# ------ GENETIC ALGORITHM -----
@app.route("/genetic", methods=["GET"])
def genetic():
    return Controller.setGenetic()

@app.route("/startGenetic/<int:flowerPartId>")
def startGenetic(flowerPartId):
    return Controller.startGenetic(flowerPartId)

@app.route("/pauseGenetic/<int:flowerPartId>", methods=["GET"])
def pauseGenetic(flowerPartId):
    return Controller.pauseGenetic(flowerPartId)


@app.route("/showGenetic/<int:flowerPartId>", methods=["GET"])
def showGenetic(flowerPartId):
    return Controller.showGenetic(flowerPartId)

@app.route("/showGeneticInfo/<int:flowerPartId>", methods=["GET"])
def showGeneticInfo(flowerPartId):
    return Controller.showGeneticInfo(flowerPartId)


@app.route("/newFlower", methods=["GET"])
def newFlower():
    return Controller.newFlower()

@app.route("/modifyMutation/<int:flowerPartId>/<int:mutationValue>", methods=["GET"])
def modifyMutation(flowerPartId, mutationValue):
    return Controller.modifyMutation(flowerPartId, mutationValue)