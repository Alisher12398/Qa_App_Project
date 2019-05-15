from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import authenticate, TokenAuthentication
from api.serializers import QaModelSerializer
from api.models import Group, Data, Qa, Company, Offers, OffersPurchases

#CBV 

class QaCBView(APIView):
    def get(self, request):
        qas = Qa.objects.all()
        serializer = QaModelSerializer(qas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QaModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)        

# CBV Generics

class QaGenericsCBView(generics.ListCreateAPIView):
    queryset = Qa.objects.all()
    serializer_class = QaModelSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)



class CompanyCBView(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanyModelSerializer(qas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)        


class CompanyGenericsCBView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyModelSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
