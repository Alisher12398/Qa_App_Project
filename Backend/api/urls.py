from django.urls import path
# from .views.fbv import *
# from .views.cbv import *
from .views.views import *
from .views.cbv import *
from .views.fbv import *
urlpatterns = [
#    path('groups/', groups),
    # path('qas/', QaCBView.as_view()),
    # path('qas/', QaGenericsCBView.as_view()),
    # path('groups/', GroupCBView.as_view()),
    # path('groups/', GroupGenericsCBView.as_view()),
    # path('company/', CompanyCBView.as_view()),
    # path('company/', CompanyGenericsCBView.as_view()),

    # path('company/', company),
    # path('offers/', offer),
    # path('purchases/offers/', purchase_offers),
    # path('group/<int:id_group>/', qa),
    # path('user/data/', data),

    path('groups/', GroupList.as_view()),
    path ('groups/<int:pk>/', GroupDetail.as_view()),
    path ('qas/<int:pk>/', qa_list),
    path ('offers/', OffersList.as_view()),
]