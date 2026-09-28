from django.shortcuts import render, redirect
from .forms import ContactForm


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            return redirect("thank_you")
    else:
        form = ContactForm()

    return render(request, "feedback/contact.html", {"form": form})

def thank_you(request):
    return render(request, "feedback/thank_you.html")