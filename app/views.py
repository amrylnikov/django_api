import random
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer


# ---------------------- api ------------------------
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class RandomNumberView(APIView):
    def get(self, request, number, *args, **kwargs):
        if number % 2 != 0:
            return Response({"error": "Number should be even"}, status=status.HTTP_400_BAD_REQUEST)

        half_number = number // 2
        cards = list(range(1, half_number + 1)) * 2
        random.shuffle(cards)

        return Response({"cards": cards}, status=status.HTTP_200_OK)
