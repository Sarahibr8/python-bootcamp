from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello from Home")


def about(request):
    return HttpResponse("Hello from About")


def contact(request):
    return HttpResponse("Hello from Contact")