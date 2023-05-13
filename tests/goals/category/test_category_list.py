import pytest
from django.urls import reverse
from rest_framework import status

from goals.serializers import GoalCategorySerializer


@pytest.mark.django_db
class TestCategoriesList:
    url = reverse('goals:cat_list')

    def test_get_list(self, auth_client, board, category_factory):
        board, category = board
        categories = category_factory.create_batch(2, board=board)

        response = auth_client.get(self.url)

        assert response.status_code == status.HTTP_200_OK
        for cat in GoalCategorySerializer(categories, many=True).data:
            assert cat in response.data
