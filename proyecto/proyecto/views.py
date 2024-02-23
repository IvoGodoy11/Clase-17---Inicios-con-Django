from django.template import Template, Context
from django.http import HttpResponse

import datetime

def saludar(request):
    return HttpResponse("Bienvenido a la Comisión 50215 - Clase Django")


def bienvenida(request, nombre, apellido):
    respuesta = f"Te damos la bienvenida a la Comisión 50215 {nombre} {apellido}"
    return HttpResponse(respuesta)


def bienvenido_html(request, nombre, apellido):
    hoy = datetime.datetime.now()
    respuesta = f"""
    <html>
    <h1>Bienvenidos al curso de Django!! Comisión 50215, {nombre} {apellido}</h1>
    <h2>Esta es la comisión de los estudiosos</h2>
    <h2>Te damos la bienvenida de nuevo {nombre}!</h2>
    <h3>Hoy es {hoy}</h3>
    </html>
    """
    return HttpResponse(respuesta)


def bienvenido_template(request, nombre, apellido):
    miHtml = open("C:/Users/ivo-g/Documents/Python Coder House/Codigo de las clases/clase 17/proyecto/proyecto/plantillas/bienvenido.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    contexto = Context()
    respuesta = plantilla.render(contexto)
    return HttpResponse(respuesta)
