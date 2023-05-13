import pytest
from django.urls import reverse
from rest_framework import status

from goals.serializers import GoalSerializer
from tests.goals.utils import BaseTestCase


@pytest.mark.django_db
class TestGoalList(BaseTestCase):
    url = reverse('goals:goal_list')

    def test_get_list(self, auth_client, board, goal_factory):
        _, category = board
        goals = goal_factory.create_batch(2, category=category)

        response = auth_client.get(self.url)

        assert response.status_code == status.HTTP_200_OK
        for cat in GoalSerializer(goals, many=True).data:
            assert cat in response.data
