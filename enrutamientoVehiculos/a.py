import os, sys
sys.path.append('C:/Users/lachy/Desktop/PMA/pma')
os.environ['DJANGO_SETTINGS_MODULE'] = 'pma.settings'
import django
django.setup()
from django.contrib import messages
from enrutamientoVehiculos.models import *


def load_corpus(path):
    text = []
    #por ahora el metodo solo devolvera la lista de los documentos leidos
    if os.path.isdir(path):
        doc = 0
        for root, dirs, files in os.walk(path):
            for filename in files:
                with open(os.path.join(root,filename), encoding='utf8', errors='ignore') as f:
                    method = root.replace("C:/Users/lachy/Music/vrp___\\","")
                    directory = root.replace("\\","/")
                    Publication.objects.create(name = filename, path = root,  autor="", solutions_method=method)
                    
    else:
        #Exception("Direccion incorrecta")
        print("La direccion no es correcta")
    print("Listo")


