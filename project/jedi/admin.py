from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import Planet, Jedi, Challenge, Question

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    pass


@admin.register(Jedi)
class JediAdmin(admin.ModelAdmin):
    pass


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    filter_horizontal = ('question',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass
