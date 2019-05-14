from django.urls import path
from .views.fbv import *
urlpatterns = [
    path('groups/', groups),
    path('company/', company),
    path('offers/', offer),
    path('purchases/offers/', offer_purchases),
    path('group/<int:id_group>/', qa),
    path('user/data/', data),
]