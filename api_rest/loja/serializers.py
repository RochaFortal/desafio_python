from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from .models import (Pedido, Movimentacao, Estoque)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'is_superuser')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, params):
        user = User(
            email=params['email'],
            username=params['username'])

        user.set_password(params['password'])
        user.save()
        Token.objects.create(user=user)
        return user


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ('numer', 'user', 'produtos')


class MovimentacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimentacao
        fields = ('tipo')


class EstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estoque
        fields = ('produto', 'quantidade', 'tipo')