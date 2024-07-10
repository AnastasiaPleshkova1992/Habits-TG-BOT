from rest_framework import serializers

from habits.models import Habit
from habits.validators import EliminationChoiceValidator, TimeDurationValidator, CombinationValidator, AbsenceValidator


class HabitSerializers(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ('__all__',)
        validators = [
            EliminationChoiceValidator('related_habit', 'reward'),
            TimeDurationValidator('time_duration'),
            CombinationValidator('related_habit', 'pleasant_habit_sign'),
            AbsenceValidator('reward', 'related_habit', 'pleasant_habit_sign'),
        ]
