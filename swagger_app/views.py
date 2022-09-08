from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
# Create your views here.


class UserView(GenericAPIView):

    serializer_class = UserSerializer

    def post(self, request):
        data = request.data
        print(data)
        try:
            create_user = User(username = data['username'], email = data['email'], password = data['password'])
            create_user.save()

            return Response({'msg': 'registration successfully.'})

        except:
            return Response({'error': 'registration failed.'})