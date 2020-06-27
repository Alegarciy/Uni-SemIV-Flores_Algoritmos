from flask import Flask, render_template, url_for, flash, Markup, redirect, request
from models.forms import ImageForm
from models.fileManager import FileManager
#from controllers import app
from controllers.controller import Controller
import os
from models.config import Config
import secrets


template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
template_dir = os.path.join(template_dir, 'Progra1')
template_dir = os.path.join(template_dir, 'app')
template_dir = os.path.join(template_dir, 'templates')
template_view_dir = os.path.join(template_dir, 'view')
static_dir = os.path.join(template_dir, Config.STATICFOLDER)

app = Flask(__name__, template_folder=template_view_dir, static_folder=static_dir)
app.config['SECRET_KEY'] = 'eb289e8e6629dd79004bf93963dc2933'

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
uploads_dir = os.path.join(template_dir, Config.STATICFOLDER)
uploads_dir = os.path.join(uploads_dir, Config.USERINPUTFOLDER)

Config.DATADIRECTORY = uploads_dir

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

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
        return "True"
    return "False"


@app.route("/convertProcess", methods=["GET"])
def showConvertProcess():
    plot_url = Controller.getConvertProcess()
    if(plot_url == "False") :
        return "False"

    model_plot = Markup('<img src="data:image/png;base64,{}" class="img-fluid" alt="Responsive image" width: 360px; height: 288px>'.format(plot_url))
    return model_plot

@app.route("/convertProgress", methods=["GET"])
def showConvertProgressBar():
    progress = Controller.getConvertProgress()
    return progress

# ----- IMAGE ANALYZER ---------

@app.route("/analyze", methods=["GET"])
def analyze():
    print("ANALYZEEEEEEE")
    Controller.setImageAnayzer()
    return render_template('home.html')
