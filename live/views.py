from django.shortcuts import render
from .models import *




def home_page(request):
    #img   = Img.objects.all()
    text  = TextRight.objects.all()
    text1 = TextLeft.objects.all()

    ctx = {
        "text":text,
        "text1":text1,
        #"img":img
    }

    return render(request, 'index.html', ctx)
