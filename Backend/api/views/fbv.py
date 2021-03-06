from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import authenticate, TokenAuthentication
# from api.serializers import QaSerializer, DataSerializer, OffersPurchasesSerializer, OffersSerializer, CompanySerializer, GroupSerializer
# from api.models import Group, Data, Qa, Company, Offers, OffersPurchases
from api.serializers import QaSerializer, GroupSerializer
from api.models import Qa, Group

def qa_list(request,pk):
    if request.method == 'GET':
        group = Group.objects.get(id=pk)
        qas= Qa.objects.filter(id_group = group)
        serializer = QaSerializer(qas, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    # elif request.method == 'POST':
    #
    #     serializer = CategorySerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(owner=request.user)
    #         return JsonResponse(serializer.data)
    #     return JsonResponse(serializer.errors)
    # return JsonResponse({'error': 'bad request'})
# @api_view(['GET', 'POST'])
# def groups(request):
#     if request.method == 'GET':
#         groups = Group.objects.all()
#         serializer = GroupSerializer(groups, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = GroupSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
# @api_view(['GET', 'POST'])
# def qa(request, id_group):
#     if request.method == 'GET':
#         qas = Qa.objects.filter(id_group=id_group)
#         serializer = QaSerializer(qas, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = QaSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
# @api_view(['GET', 'POST'])
# def data(request):
#     if request.method == 'GET':
#         data_ = Data.objects.for_user(request.user)
#         serializer = DataSerializer(data_, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = DataSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#
# @api_view(['GET', 'POST'])
# def company(request):
#     if request.method == 'GET':
#         companies = Company.objects.all()
#         serializer = CompanySerializer(companies, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CompanySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#
# @api_view(['GET', 'POST'])
# def offer(request):
#     if request.method == 'GET':
#         offers = Offers.objects.all()
#         serializer = OffersSerializer(offers, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = OffersSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
# @api_view(['GET', 'POST'])
# def offer_purchases(request):
#     if request.method == 'GET':
#         offers_purchases = OffersPurchases.objects.for_user(request.user)
#         serializer = OffersPurchasesSerializer(offers_purchases, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = OffersPurchasesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
# @csrf_exempt
# def purchase_offers(request):
#     if request.method == 'GET':
#         offers_purchased = OffersPurchases.objects.all()
#         for op in offers_purchased:
#             op.get_user_offers()
#         return JsonResponse(OffersPurchases.objects.first().get_user_offers(), safe=False)
#     elif request.method == 'POST':
#         data = json.loads(request.body)
#         offer = Offers.objects.get(pk=1)
#         offer_id = OffersPurchases.objects.create(id_offer=offer)
#         po_list = OffersPurchases(
#             id_offer=data[offer_id]
#         )
#         po_list.save()
#         return JsonResponse(po_list.get_user_offers())

    # @api_view(['GET', 'POST'])
    # def contacts(request):
    #     if request.method == 'GET':
    #         contacts = Contact.objects.for_user(request.user)
    #         serializer = ContactSerializer(contacts, many=True)
    #         return Response(serializer.data)
    #     elif request.method == 'POST':
    #         serializer = ContactSerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save(owner=request.user)
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #         return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    #
    # @api_view(['GET', 'PUT', 'DELETE'])
    # def contacts_detail(request, pk):
    #     try:
    #         contacts = Contact.objects.for_user(request.user).get(id=pk)
    #     except TaskList.DoesNotExist as e:
    #         return Response({'error': f'{e}'}, status=status.HTTP_404_NOT_FOUND)
    #
    #     if request.method == 'GET':
    #         serializer = ContactSerializer(contacts)
    #         return Response(serializer.data)
    #     elif request.method == 'PUT':
    #         serializer = ContactSerializer(instance=contacts, data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    #     elif request.method == 'DELETE':
    #         contacts.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)