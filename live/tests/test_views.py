import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
class TestTextRight:

    def test_list_right_success(self, api_client, right_factory):
        # Bazada ma'lumot borligida
        right_factory.create_batch(2)
        url = reverse('right-list')
        response = api_client.get(url)
        assert response.status_code == 200
        assert len(response.data) == 2

    def test_list_right_empty(self, api_client):
        # Bazada ma'lumot bo'lmaganda
        url = reverse('right-list')
        response = api_client.get(url)
        assert response.status_code == 200
        assert response.data == []  # Bo'sh list qaytishi kerak


    def test_create_right_permission_denied(self, api_client):
        # 1. Login qilmagan (anonim) foydalanuvchi
        url = reverse('right-list')
        data = {"name_right": "Test", "text_right": "Test", "link_right": "http://test.com"}

        # 2. POST so'rovi yuboramiz
        response = api_client.post(url, data)

        # 3. Endi bu assert PASS bo'ladi, chunki IsAuthenticatedOrReadOnly POSTni bloklaydi
        assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
class TestTextLeft:

    def test_list_left_success(self, api_client, left_factory):
        # Bazada ma'lumot borligida
        left_factory.create_batch(2)
        url = reverse('left-list')
        response = api_client.get(url)
        assert response.status_code == 200
        assert len(response.data) == 2

    def test_list_left_empty(self, api_client):
        # Bazada ma'lumot bo'lmaganda
        url = reverse('left-list')
        response = api_client.get(url)
        assert response.status_code == 200
        assert response.data == []  # Bo'sh list qaytishi kerak


    def test_create_left_permission_denied(self, api_client):
        # 1. Login qilmagan (anonim) foydalanuvchi
        url = reverse('left-list')
        data = {"name_left": "Test12", "text_left": "Test_left", "link_left": "http://test-left.com"}

        # 2. POST so'rovi yuboramiz
        response = api_client.post(url, data)

        # 3. Endi bu assert PASS bo'ladi, chunki IsAuthenticatedOrReadOnly POSTni bloklaydi
        assert response.status_code == status.HTTP_403_FORBIDDEN