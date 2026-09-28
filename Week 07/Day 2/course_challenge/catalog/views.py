from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render


courses_list = [
    {
        "id": 1,
        "name": "Python",
        "level": "Beginner",
        "students": 24,
        "description": "Learn Python fundamentals, variables, loops, functions, and problem solving.",
        "image": "images/python.jpg",
    },
    {
        "id": 2,
        "name": "SQL",
        "level": "Intermediate",
        "students": 0,
        "description": "Learn how to work with databases, tables, queries, and reports using SQL.",
        "image": "images/sql.png",
    },
    {
        "id": 3,
        "name": "Django",
        "level": "Intermediate",
        "students": 18,
        "description": "Build web applications using <strong>Django</strong>, templates, URLs, and views.",
        "image": "images/django.jpg",
    },
]


def home(request):
    context = {
        "username": "Sarah",
        "courses": courses_list,
    }
    return render(request, "catalog/home.html", context)


def courses(request):
    context = {
        "username": "Sarah",
        "courses": courses_list,
    }
    return render(request, "catalog/courses.html", context)


def course_detail(request, course_id):
    selected_course = None

    for course in courses_list:
        if course["id"] == course_id:
            selected_course = course

    if selected_course is None:
        raise Http404("Course not found")

    context = {
        "username": "Sarah",
        "course": selected_course,
    }
    return render(request, "catalog/course_detail.html", context)