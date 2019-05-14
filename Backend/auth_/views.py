from django.shortcuts import render

from django.contrib.auth.models import User
from auth_.serializers import UserSerializer, UserRegisterSerializer
from rest_framework import generics, authentication
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from api.models import Data, Group

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['POST'])
def register(request):
    serializer = UserRegisterSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        for group in Group.objects.all():
            data = Data.objects.create(id_user=user, id_group=group, points=0)

        user.set_password(serializer.data['password'])
        user.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})


@api_view(['POST'])
def logout(request):
    request.auth.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)