import random
from django.shortcuts import render
from django.contrib.auth import get_user_model, login, logout
from rest_framework import viewsets, status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .models import Player, Card, Game
from django.contrib.auth.models import User
from .serializers import PlayerSerializer, CardSerializer, GameSerializer, UserSerializer, UserRegistrationSerializer


# ---------------------- api ------------------------
class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = (IsAuthenticated, )

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RandomNumberView(APIView):
    def get(self, request, number, *args, **kwargs):
        if number % 2 != 0:
            return Response({"error": "Number should be even"}, status=status.HTTP_400_BAD_REQUEST)

        cards = Card.objects.all()
        if not cards.exists():
            return Response({"error": "No cards available"}, status=status.HTTP_404_NOT_FOUND)

        cards_list = list(cards.values())

        result = random.sample(cards_list, number // 2) * 2
        random.shuffle(result)

        return Response(result, status=status.HTTP_200_OK)

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

# class UserLoginView(generics.CreateAPIView):
#     serializer_class = UserSerializer
#     permission_classes = [permissions.AllowAny]

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data
#         login(request, user)
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key})

# class UserLogoutView(generics.GenericAPIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request, *args, **kwargs):
#         logout(request)
#         return Response({'detail': 'Successfully logged out'})
