from django.urls import path
from .views import *

urlpatterns = [
     path('', home_page),
     path('right', TextRightAPI.as_view(), name="right-list"),
     path('left', TextLeftAPI.as_view(), name="left-list"),



]