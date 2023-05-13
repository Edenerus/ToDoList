import pytest
from rest_framework import status
from rest_framework.reverse import reverse


@pytest.mark.django_db
class TestRetrieveProfile:
    url = reverse('core:profile')

    def test_get_profile(self, auth_client, user):
        response = auth_client.get(self.url)

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }

    def test_profile_get_not_authorized(self, client):
        response = client.get(self.url)

        assert response.status_code == status.HTTP_403_FORBIDDEN
        