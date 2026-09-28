from django.shortcuts import render
from django.http import HttpResponse


def create_view(request):
    return HttpResponse("Create Product")


def details_view(request, id):
    return HttpResponse(f"Product ID: {id}")