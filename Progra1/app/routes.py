from flask import Flask, render_template, url_for, flash, redirect, request
from app.forms import RegistrationForm, LoginForm, ImageForm
from app.fileManager import FileManager
from app import app
import os
import secrets

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)



    

@app.route("/upload-image", methods=['GET', 'POST'])
def upload_image():
    form = ImageForm()
    fileManager = FileManager()
    if form.image_01.data and form.image_02:
        fileManager.save_image(form.image_01.data, "imagen_01.png")
        fileManager.save_image(form.image_02.data, "imagen_02.png")
        fileManager.save_json(form.json.data, "data.json")
        if form.image_03.data:
            fileManager.save_image(form.image_03.data, "imagen_03.png")
    if request.args.get("building") == "casinos":
        print("Hola Mundo")
        fileManager.create_json()



    return render_template("upload_image.html", form=form)
