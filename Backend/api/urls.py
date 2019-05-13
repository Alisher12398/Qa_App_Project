from django.urls import path
from .views.fbv import *
urlpatterns = [
    path('groups/', groups),
    path('company/', company),
    path('offers/', offer),
    path('purchases/offers/', offer_purchases),
]