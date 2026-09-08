from django.shortcuts import render

def home(request):
    context = {
        "name": "Sarah",
        "welcome_message": "Welcome to my Django template lab!",
    }
    return render(request, "pages/home.html", context)


def courses(request):
    course_list = [
        {"name": "Python", "level": "Beginner", "available": True},
        {"name": "Django", "level": "Intermediate", "available": True},
        {"name": "React", "level": "Advanced", "available": False},
    ]

    context = {
        "courses": course_list,
    }
    return render(request, "pages/courses.html", context)


def about(request):
    context = {
        "description": "This website was built for the Django Templates lab."
    }
    return render(request, "pages/about.html", context)