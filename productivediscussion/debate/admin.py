"""Admin."""
from django.contrib import admin
from debate.models import Debate
from debate.models import ArgumentsFor
from debate.models import ArgumentsAgainst

admin.site.register(Debate)
admin.site.register(ArgumentsFor)
admin.site.register(ArgumentsAgainst)
