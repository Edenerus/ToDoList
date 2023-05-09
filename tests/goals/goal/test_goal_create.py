import pytest
from django.urls import reverse
from rest_framework import status

from goals.models import Goal
from tests.goals.utils import BaseTestCase


@pytest.mark.django_db
class TestGoalCreate(BaseTestCase):
    url = reverse('goals:goal_create')

    def test_create_successful(self, auth_client, board):
        board, category = board
        response = auth_client.post(self.url, data={
            'category': category.id,
            'title': 'test_title'
        })

        goal = Goal.objects.last()

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == {
            'id': goal.id,
            'category': category.id,
            'created': self.date_time_str(goal.created),
            'updated': self.date_time_str(goal.updated),
            'title': 'test_title',
            'description': goal.description,
            'due_date': goal.due_date,
            'status': goal.status,
            'priority': goal.priority
        }
