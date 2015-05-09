from django.shortcuts import render
from models import Pages
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from xmlbarrapunto import getNews


news = ""


@csrf_exempt
def mostrar(request, recurso):

    if request.method == "GET":
        try:
            clave = Pages.objects.get(name=recurso)
            salida = clave.name + ": " + clave.page + "<br><hr>" + news
            return HttpResponse(salida)

        except Pages.DoesNotExist:
            return HttpResponseNotFound("Page not found")

    if request.method == "PUT":
        page = Pages(name=recurso, page=request.body)
        page.save()
        return HttpResponse("Contenido Guardado")
    else:
        return HttpResponseNotFound("Method not found.")


def updateNews(request):
    global news
    news = getNews()
    return HttpResponse("BarraPunto updated.<br>" + news)
