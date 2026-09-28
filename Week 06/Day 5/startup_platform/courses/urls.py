from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path("", views.course_list, name="course_list"),
    path("<slug:slug>/", views.course_detail, name="detail"),
    path("category/<slug:category>/", views.category, name="category"),
]