from django.shortcuts import render
from django.views import View
# CBV / Bonus
class HomeView(View):

    def get(self, request):
        return render(request, "home.html")

def reports(request):
    return render(request, "reports.html")