from rest_framework import serializers
from .models import *


class TextRightSerializers(serializers.ModelSerializer):
    class Meta:
        model = TextRight
        fields = ('id', 'name_right', 'text_right', 'link_right')


class TextLeftSerializers(serializers.ModelSerializer):
    class Meta:
        model = TextLeft
        fields = ('id', 'name_left', 'text_left', 'link_left')



