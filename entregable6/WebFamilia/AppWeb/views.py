from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def familiares(self):
    lista= [["Matias", "Mayoral", "27", "15/01/1995"], ["Agustin", "Peron", "22", "11/01/2000"], ["Alma", "Berzaghi", "15", "28/08/2008"]]
    diccionario= {"familiares" : lista}
    plantilla= loader.get_template("webfamiliat.html")
    documento= plantilla.render(diccionario)
    return HttpResponse(documento)

