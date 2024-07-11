from rest_framework import serializers

from habits.models import Habit
from habits.validators import (
    EliminationChoiceValidator,
    TimeDurationValidator,
    CombinationValidator,
    AbsenceValidator,
    PeriodicityValidator,
)
from users.serializers import UserSerializer


class HabitSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            EliminationChoiceValidator("related_habit", "reward"),
            TimeDurationValidator("duration"),
            CombinationValidator("related_habit", "pleasant_habit_sign"),
            AbsenceValidator("reward", "related_habit", "pleasant_habit_sign"),
            PeriodicityValidator("periodicity"),
        ]
