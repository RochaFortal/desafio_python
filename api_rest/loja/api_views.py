from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from django.contrib.auth import authenticate
from .serializers import UserSerializer, EstoqueSerializer, MovimentacaoSerializer, PedidoSerializer


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

class LoginView(APIView):
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key, "user": UserSerializer(user).data})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class PedidoViewSet(viewsets.ViewSet):
    serializer_class = PedidoSerializer


class MovimentacaoViewSet(viewsets.ViewSet):
    serializer_class = PedidoSerializer


class EstoqueViewSet(viewsets.ViewSet):
    serializer_class = EstoqueSerializer