from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View


class RegisterView(View):

    def get(self, request):
        return render(request, "accounts/register.html")

    def post(self, request):
        return HttpResponse("Register Form Submitted")


class LoginView(View):

    def get(self, request):
        return render(request, "accounts/login.html")

    def post(self, request):
        return HttpResponse("Login Form Submitted")


class ProfileView(View):

    def get(self, request):
        username = request.session.get("username", "Guest")
        return render(request, "accounts/profile.html", {"username": username})


def status(request):
    return JsonResponse({"status": "OK"})