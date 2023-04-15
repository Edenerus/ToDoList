from django.db import models
from django.utils import timezone

from core.models import User


class DatesModel(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(verbose_name='Дата создания')
    updated = models.DateTimeField(verbose_name='Дата последнего обновления')

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super().save(*args, **kwargs)


class GoalCategory(DatesModel):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    title = models.CharField(verbose_name='Название', max_length=255)
    user = models.ForeignKey(User, verbose_name="Автор", on_delete=models.PROTECT)
    is_deleted = models.BooleanField(verbose_name='Удалена', default=False)

    def __str__(self):
        return self.title


class Goal(DatesModel):
    class Status(models.IntegerChoices):
        to_do = 1, 'К выполнению'
        in_progress = 2, 'В процессе'
        done = 3, 'Выполнено'
        archived = 4, 'Архив'

    class Priority(models.IntegerChoices):
        low = 1, 'Низкий'
        medium = 2, 'Средний'
        high = 3, 'Высокий'
        critical = 4, 'Критический'

    class Meta:
        verbose_name = 'Цель'
        verbose_name_plural = 'Цели'

    title = models.CharField(verbose_name='Название', max_length=255)
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор')
    category = models.ForeignKey(GoalCategory, on_delete=models.CASCADE, verbose_name='Категория')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    status = models.PositiveSmallIntegerField(choices=Status.choices, default=Status.to_do, verbose_name='Статус')
    priority = models.PositiveSmallIntegerField(choices=Priority.choices, default=Priority.low,
                                                verbose_name='Приоритет')
    due_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата дедлайна')

    def __str__(self):
        return self.title


class GoalComment(DatesModel):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Коментарии'

    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, verbose_name='Цель')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    text = models.TextField(verbose_name='Комментарий')

    def __str__(self):
        return self.text
