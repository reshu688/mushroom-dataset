from django.urls import path
from .views import *

urlpatterns = [
    path("",homepage),
    path("submit",prediction)
]