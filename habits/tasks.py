from datetime import datetime, timedelta

import pytz
from celery import shared_task

from config import settings
from habits.models import Habit
from habits.services import send_telegram_message
from users.models import User


@shared_task
def send_remainder():
    """Send a remainder in telegram  at what time which habits need to be done."""
    habits = Habit.objects.all()
    users = User.objects.all()
    for user in users:
        if user.tg_chat_id:
            for habit in habits:
                if habit.time() == datetime.now(pytz.timezone(settings.TIME_ZONE)):
                    if habit.pleasant_habit_sign:
                        send_telegram_message(
                            tg_chat_id=user.tg_chat_id,
                            message=f"Необходимо сделать: {habit.action}, "
                            f"время выполнения: {habit.duration} секунд."
                        )
                        if habit.related_habit:
                            send_telegram_message(
                                tg_chat_id=user.tg_chat_id,
                                message=f"Необходимо сделать: {habit.action}, "
                                f"время выполнения: {habit.duration} секунд, "
                                f"затем можно будет: {habit.related_habit}.")
                            if habit.reward:
                                send_telegram_message(
                                    tg_chat_id=user.tg_chat_id,
                                    message=f"Необходимо сделать: {habit.action}, "
                                    f"время выполнения: {habit.duration} секунд, "
                                    f"за это плолучишь: {habit.reward}.")
                    habit.time = datetime.now(pytz.timezone(settings.TIME_ZONE)) + timedelta(days=habit.periodicity)
                    habit.save()
