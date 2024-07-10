from datetime import timedelta

from rest_framework.exceptions import ValidationError


class EliminationChoiceValidator:
    """Validator that eliminates to choice related_habit and reward at the same time"""
    def __init__(self, related_habit, reward):
        self.related_habit = related_habit
        self.reward = reward

    def __call__(self, habit):
        if habit.get(self.related_habit) and habit.get(self.reward):
            raise ValidationError(
                'Выберите либо связанную привычку, либо вознаграждение.'
            )


class TimeDurationValidator:
    """Validator that checks if time_duration is within the interval of 120 seconds"""
    def __init__(self, duration):
        self.duration = duration

    def __call__(self, habit):
        max_duration = timedelta(seconds=120)
        if habit.get(self.duration) > max_duration:
            raise ValidationError(
                f'Длительность выполнения привычки не может превышать {max_duration}.'
            )


class CombinationValidator:
    """Validator that checks that only habits with a sign of a pleasant habit can fall into related habits"""
    def __init__(self, related_habit, pleasant_habit_sign):
        self.related_habit = related_habit
        self.pleasant_habit_sign = pleasant_habit_sign

    def __call__(self, habit):
        if habit.get(self.related_habit) and not habit.get(self.pleasant_habit_sign):
            raise ValidationError(
                'В связанные привычки могут попадать только привычки с признаком приятной привычки.'
            )


class AbsenceValidator:
    """Validator that checks that a pleasant habit cannot have a reward or a related habit"""
    def __init__(self, reward, related_habit, pleasant_habit_sign):
        self.reward = reward
        self.related_habit = related_habit
        self.pleasant_habit_sign = pleasant_habit_sign

    def __call__(self, habit):
        if habit.get(self.pleasant_habit_sign) and (habit.get(self.reward) or habit.get(self.related_habit)):
            raise ValidationError(
                'Приятная привычка не может иметь вознаграждение или связанную привычку.'
            )