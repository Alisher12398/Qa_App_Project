from django.urls import path
from .views.fbv import *
from .views.cbv import *
urlpatterns = [
    path('groups/', groups),
    #path('qas/', QaCBView.as_view()),
    #path('qas/', QaGenericsCBView.as_view()),
    path('company/', company),
    path('offers/', offer),
    path('purchases/offers/', offer_purchases),
    path('group/<int:id_group>/', qa),
    path('user/data/', data),
]