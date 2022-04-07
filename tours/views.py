from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.core.handlers.wsgi import WSGIRequest


# Create your views here.
def main_view(request):
    return render(request, 'tours/index.html')


def departure_view(request: WSGIRequest, departure):
    return render(request, 'tours/departure.html')


def tour_view(request: WSGIRequest, id):
    return render(request, 'tours/tour.html')


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')
