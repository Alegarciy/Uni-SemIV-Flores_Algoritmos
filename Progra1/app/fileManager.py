
from app import app
from app.forms import RegistrationForm, LoginForm, ImageForm
import os
import json

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


class FileManager():

    #Saves image with a given name
    def save_image(self, form_picture, name):
        target = os.path.join(APP_ROOT, 'images/')
        print(target)

        if not os.path.isdir(target):
            os.mkdir(target)
        
        print(form_picture)
        destination = "/".join([target, name])
        print(destination)
        form_picture.save(destination)

    #Saves json with a given name
    def save_json(self, form_picture, name):
        target = os.path.join(APP_ROOT, 'images/')
        print(target)

        if not os.path.isdir(target):
            os.mkdir(target)

        print(form_picture)
        destination = "/".join([target, name])
        print(destination)
        form_picture.save(destination)

    #Pruebas para generar un json
    def create_json(self):
        information = {}
        information ["colorPetaloMasPreferido"] = "#f20c2f"
        information ["colorCentroMasPreferido"] = "#f20c2f"
        information ["colorPetaloMenosPreferido"] = "#f20c2f"
        information ["colorCentroMenosPreferido"] = "#f20c2f"
        information ["numeroDePetalos"] = 9
        information ["numeroDeCentros"] = 1
        # Las coordenadas de datos estan expresados como (x,y)
        information ["pixelPetaloMasAlejado"] = [5,5]
        information ["pixelCentroMasAlejado"] = [1,1]
        information ["pixelCentral"] = [0,0]

        fileTemp = open("D:/jsonFlores.txt", "w", encoding="utf-8")
        json.dump(information, fileTemp, ensure_ascii=False)
    





