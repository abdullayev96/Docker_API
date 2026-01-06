import pytest
from rest_framework.test import APIClient
from live.factories import TextLeftFactory, TextRightFactory

# 1. API Client fixture (hamma testlarda request yuborish uchun)
@pytest.fixture
def api_client():
    return APIClient()

# 2. Avtorizatsiyadan o'tgan client (login qilgan user sifatida)
@pytest.fixture
def auth_client(db, api_client, django_user_model):
    user = django_user_model.objects.create_user(username="test_user", password="123")
    api_client.force_authenticate(user=user)
    return api_client


# 3. Factory fixture'larni tanitish
@pytest.fixture
def right_factory(db):
    return TextRightFactory


@pytest.fixture
def left_factory(db):
    return TextLeftFactory