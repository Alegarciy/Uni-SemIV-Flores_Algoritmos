from flask import Flask, render_template, url_for, flash, redirect, request
from models.forms import ImageForm
from models.fileManager import FileManager
#from controllers import app
from controllers.controller import Controller
import os
import secrets


template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
template_dir = os.path.join(template_dir, 'Progra1')
template_dir = os.path.join(template_dir, 'app')
template_dir = os.path.join(template_dir, 'templates')
template_view_dir = os.path.join(template_dir, 'view')
static_dir = os.path.join(template_dir, "static")

app = Flask(__name__, template_folder=template_view_dir, static_folder=static_dir)
app.config['SECRET_KEY'] = 'eb289e8e6629dd79004bf93963dc2933'

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/loadImage", methods=['GET', 'POST'])
def loadImage():
    pass
    
@app.route("/upload-image", methods=['GET', 'POST'])
def upload_image():
    form = ImageForm()
    userImages = Controller.getListLoadedImages()

    if request.method == "POST" and form.image.data and form.json:
        Controller.loadImage(form.image.data, form.json.data)
        #FileManager.save_image(form.image.data, "imagen_000.png")
        #FileManager.save_json(form.json.data, "data.json")

    return render_template("upload_image.html", form=form, userImages=userImages)
