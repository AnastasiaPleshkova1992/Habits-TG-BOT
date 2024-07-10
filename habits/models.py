from datetime import timedelta

from django.db import models

from config import settings

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    """Model for habit"""

    period = [("weekly", "еженедельно"), ("daily", "ежедневно")]
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Создатель привычки",
        **NULLABLE,
    )
    place = models.CharField(
        max_length=100,
        verbose_name="Место выполнения привычки",
        help_text="Укажите место выполнения привычки",
    )
    time = models.TimeField(
        verbose_name="Время выполнения привычки",
        help_text="Укажите время выполнения привычки",
    )
    action = models.CharField(
        max_length=200,
        verbose_name="Действие, которое требуется сделать",
        help_text="Укажите действие, которое требуется сделать",
    )
    pleasant_habit_sign = models.BooleanField(
        verbose_name="Признак приятной привычки",
        help_text="Укажите, является ли привычка приятной",
        default=False,
    )
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        verbose_name="Связанная привычка",
        help_text="Укажите связанную привычку",
        **NULLABLE,
    )
    periodicity = models.CharField(
        max_length=10,
        choices=period,
        default="daily",
        verbose_name="Периодичность выполнения привычки",
        help_text="Укажите периодичность выполнения привычки",
    )
    reward = models.CharField(
        max_length=200,
        verbose_name="Награда за выполнение привычки",
        help_text="Укажите награду за выполнение привычки",
        **NULLABLE,
    )
    duration = models.DurationField(
        verbose_name="Продолжительность выполнения привычки",
        help_text="Укажите продолжительность выполнения привычки",
        default=timedelta(seconds=120),
    )
    is_published = models.BooleanField(
        verbose_name="Признак публичности",
        help_text="Укажите, опубликована ли привычка",
        default=True,
    )

    def __str__(self):
        return f"{self.user} будет {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
