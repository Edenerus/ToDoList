import pytest
from django.urls import reverse
from rest_framework import status

from goals.models import Board
from tests.goals.utils import BaseTestCase


@pytest.mark.django_db
class TestBoardCreate(BaseTestCase):
    url = reverse('goals:board_create')

    def test_create_success(self, auth_client):
        response = auth_client.post(self.url, data={
            'title': 'Board',
        })
        board = Board.objects.last()
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == {
            'id': board.id,
            'created': self.date_time_str(board.created),
            'updated': self.date_time_str(board.updated),
            'title': board.title,
            'is_deleted': board.is_deleted,
        }
