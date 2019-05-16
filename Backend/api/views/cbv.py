from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Qa, Group, OffersPuchases
from api.serializers import QaSerializer, GroupSerializer, OffersPurchasesSerializer
from rest_framework.permissions import IsAuthenticated

class QaList(APIView):

    def get_object(self, pk):
        try:
            return Group.objects.get(id=pk)
        except Group.DoesNotExist:
            raise Http404

    def get(self, request,pk):
        group = self.get_object(pk)
        qas = Qa.objects.filter(id_group=group)
        serializer = QaSerializer(qas, many=True)
        return Response(serializer.data)

class OfferPuchasesCBView(APIView):

    def get(self, request):
        op = OffersPuchases.objects.all()
        serializer = OffersPurchasesSerializer(op, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = OffersPurchasesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST) 