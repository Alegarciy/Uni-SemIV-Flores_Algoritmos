import os
import shutil
import json
from models.config import Config

class FileManager:

    #Saves image with a given nam
    @staticmethod
    def save_image(form_picture, folder, filename):
        print("TYPE: ")
        print(type(form_picture))
        target = os.path.join(Config.DATADIRECTORY, Config.USERINPUTFOLDER)
        target = os.path.join(target, folder)
        print(target)

        if not os.path.isdir(target):
            os.mkdir(target)
        
        print(form_picture)
        destination = "/".join([target, filename])
        print(destination)
        form_picture.save(destination)
        return destination

    #Saves json with a given name
    @staticmethod
    def save_json(form_picture, folder, filename):
        target = os.path.join(Config.DATADIRECTORY, Config.USERINPUTFOLDER)
        target = os.path.join(target, folder)
        print(target)

        if not os.path.isdir(target):
            os.mkdir(target)

        print(form_picture)
        destination = "/".join([target, filename])
        print(destination)
        form_picture.save(destination)
        return destination

    @staticmethod
    def read_json(filename):
        with open(filename) as f:
            data = json.load(f)
        return data

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

    @staticmethod
    def removeDirectory(directory):
        shutil.rmtree(directory, ignore_errors=True)




