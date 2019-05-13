from django.urls import path
from .views.fbv import *
urlpatterns = [
    path('groups/', groups),
]