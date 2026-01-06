from django.shortcuts import render
from .models import *
from rest_framework.generics import ListAPIView
from .serializers import *
from rest_framework import generics, permissions


def home_page(request):
    text = TextRight.objects.all()
    text1 = TextLeft.objects.all()
    ctx = {
        "text": text,
        "text1": text1
    }

    return render(request, 'index.html', ctx)


class TextRightAPI(ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = TextRight.objects.all()
    serializer_class = TextRightSerializers


class TextLeftAPI(ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = TextLeft.objects.all()
    serializer_class = TextLeftSerializers