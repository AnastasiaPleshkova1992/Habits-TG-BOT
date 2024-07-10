from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "action",
        "is_published",
    )
    list_filter = ("user",)
    search_fields = ("action",)
