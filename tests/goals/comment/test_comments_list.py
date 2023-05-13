import pytest
from django.urls import reverse
from rest_framework import status

from goals.serializers import GoalCommentSerializer


@pytest.mark.django_db
class TestCommentsList:
    url = reverse('goals:comments_list')

    def test_get_list(self, auth_client, goal, comment_factory):
        comments = comment_factory.create_batch(2, goal=goal)

        response = auth_client.get(self.url)

        assert response.status_code == status.HTTP_200_OK
        for com in GoalCommentSerializer(comments, many=True).data:
            assert com in response.data
