from django.urls import path
from . import views


app_name = "app_name"
urlpatterns = [
path("", views.app_name, name="home")
]