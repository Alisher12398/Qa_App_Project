from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Qa, Group
from api.serializers import QaSerializer, GroupSerializer
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