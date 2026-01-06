import pytest
from live.models import *
from live.factories import TextRightFactory, TextLeftFactory


@pytest.mark.django_db
def test_text_right_creation():
    # Factory orqali obyekt yaratamiz
    text_obj = TextRightFactory(name_right="Ichimliklar")

    # Tekshiramiz
    assert TextRight.objects.count() == 1
    assert str(text_obj) == "Ichimliklar"


@pytest.mark.django_db
def test_text_left_creation():
    # Factory orqali obyekt yaratamiz
    text_obj = TextLeftFactory(name_left="Mohon")

    # Tekshiramiz
    assert TextLeft.objects.count() == 1
    assert str(text_obj) == "Mohon"