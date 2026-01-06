import factory
from .models import *


class TextRightFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TextRight

    name_right = factory.Faker('word')
    text_right = factory.Faker('sentence')
    link_right = factory.Faker('url')


class TextLeftFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TextLeft

    name_left = "Excel"      # Har doim "Excel" bo'lib yaratiladi
    text_left = "left text"  # Har doim shu matn bo'ladi
    link_left = factory.Faker('url')


# class TextLeftFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = TextLeft
#
#     name_left = factory.Faker('Excel')
#     text_left = factory.Faker('left')
#     link_left = factory.Faker('url')