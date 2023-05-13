import pytest
from django.urls import reverse
from rest_framework import status

from goals.models import GoalComment
from tests.goals.utils import BaseTestCase


@pytest.mark.django_db
class TestCommentCreate(BaseTestCase):
    url = reverse('goals:comment_create')

    def test_create_success(self, auth_client, goal):
        response = auth_client.post(self.url, data={
            'text': 'Test comment',
            'goal': goal.id
        })
        comment = GoalComment.objects.last()
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == {
            'id': comment.id,
            'created': self.date_time_str(comment.created),
            'updated': self.date_time_str(comment.updated),
            'text': 'Test comment',
            'goal': comment.goal.id
        }
