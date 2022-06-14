from django.http import HttpResponse
from django.template import Template, Context

def inicio(request):
    doc_externo = open("static/index.html") # este es el archivo que se renderizará (renderizar = interpretar lo que está en un texto, en este caso un html)
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context() # leng de ejecución sobre el que estoy corriendo mis plantillas
    documento = plt.render(ctx)
    return HttpResponse(documento) # -> ahora tenemos archivo html enriquecido que reconoce python (o algo así)
    
def seguimiento(request):
    doc_externo = open("static/seguimiento.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)
    
def donacion(request):
    doc_externo = open("static/donacion.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

def carritoCompra(request):
    doc_externo = open("static/carritoCompra.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)
    
def productos(request):
    doc_externo = open("static/productos.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)
    