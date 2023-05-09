from factory.django import DjangoModelFactory
from factory import SubFactory, Faker, post_generation

from core.models import User
from goals.models import Goal, GoalCategory, GoalComment, Board, BoardParticipant


# Создание фабрик для тестов
class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = Faker('user_name')
    password = Faker('password')
    email = ''

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        return cls._get_manager(model_class).create_user(*args, **kwargs)


class BoardFactory(DjangoModelFactory):
    class Meta:
        model = Board

    title = Faker('word')

    @post_generation
    def with_owner(self, create, owner, **kwargs):
        if owner:
            BoardParticipant.objects.create(board=self, user=owner, role=BoardParticipant.Role.owner)


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = GoalCategory

    user = SubFactory(UserFactory)
    title = Faker('word')
    board = SubFactory(BoardFactory)


class GoalFactory(DjangoModelFactory):
    class Meta:
        model = Goal

    user = SubFactory(UserFactory)
    category = SubFactory(CategoryFactory)
    title = Faker('word')


class BoardParticipantFactory(DjangoModelFactory):
    class Meta:
        model = BoardParticipant

    board = SubFactory(BoardFactory)
    user = SubFactory(UserFactory)


class CommentFactory(DjangoModelFactory):
    class Meta:
        model = GoalComment

    goal = SubFactory(GoalFactory)
    user = SubFactory(UserFactory)
    text = Faker('text')
