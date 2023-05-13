import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
class TestChangePassword:
    url = reverse('core:change_password')

    def test_update_password_success(self, client, user_factory, faker):
        old_password = faker.password()
        new_password = faker.password()
        user = user_factory.create(password=old_password)
        client.force_login(user)

        response = client.patch(self.url, data={
            'old_password': old_password,
            'new_password': new_password
        })
        user.refresh_from_db()

        assert response.status_code == status.HTTP_200_OK
        assert user.check_password(new_password)
        assert not response.json()
