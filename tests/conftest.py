import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from goals.models import Goal, GoalCategory, GoalComment, Board
from tests.factories import GoalFactory, CategoryFactory, CommentFactory, UserFactory, \
        BoardFactory, BoardParticipantFactory


register(GoalFactory)
register(CategoryFactory)
register(CommentFactory)
register(UserFactory)
register(BoardFactory)
register(BoardParticipantFactory)


@pytest.fixture
def client() -> APIClient:
    return APIClient()


@pytest.fixture
def auth_client(client, user) -> APIClient:
    client.force_login(user)
    return client


@pytest.fixture(autouse=True)
def another_user(user_factory):
    return user_factory.create()


@pytest.fixture
def goal(goal_factory, user, board) -> Goal:
    _, category = board
    return goal_factory.create(user=user, category=category)


@pytest.fixture
def comment(goal, user, comment_factory) -> GoalComment:
    return comment_factory.create(user=user, goal=goal)


@pytest.fixture
def board(board_factory, category_factory, user) -> tuple[Board, GoalCategory]:
    board = board_factory.create(with_owner=user)
    category = category_factory.create(board=board, user=user)
    return board, category
