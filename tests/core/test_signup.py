import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
class TestSignup:
    url = reverse('core:signup')

    def test_signup_success(self, client, user_factory):
        user_data = user_factory.build()

        response = client.post(self.url, data={
            'username': user_data.username,
            'password': user_data.password,
            'password_repeat': user_data.password
        })

        assert response.status_code == status.HTTP_201_CREATED

    def test_signup_invalid_password(self, client, user_factory):
        user_data = user_factory.build()

        response = client.post(self.url, data={
            'username': user_data.username,
            'password': '123',
            'password_repeat': '123'
        })

        assert response.status_code == status.HTTP_400_BAD_REQUEST
