import pytest
from django.urls import reverse
from rest_framework import status

from goals.models import GoalCategory
from tests.goals.utils import BaseTestCase


@pytest.mark.django_db
class TestCategoryCreate(BaseTestCase):
    url = reverse('goals:cat_create')

    def test_create_success(self, auth_client, board):
        board, _ = board
        response = auth_client.post(self.url, data={
            'title': 'Category',
            'board': board.id
        })
        category = GoalCategory.objects.last()
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == {
            'id': category.id,
            'created': self.date_time_str(category.created),
            'updated': self.date_time_str(category.updated),
            'title': category.title,
            'is_deleted': category.is_deleted,
            'board': category.board.id
        }
