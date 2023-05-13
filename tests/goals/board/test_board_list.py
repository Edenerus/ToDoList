import pytest
from django.urls import reverse
from rest_framework import status

from goals.serializers import BoardListSerializer


@pytest.mark.django_db
class TestBoardsList:
    url = reverse('goals:board_list')

    def test_get_list(self, auth_client, board_factory, user):
        boards = board_factory.create_batch(size=2, with_owner=user)

        response = auth_client.get(self.url)

        assert response.status_code == status.HTTP_200_OK
        for board in BoardListSerializer(boards, many=True).data:
            assert board in response.data
