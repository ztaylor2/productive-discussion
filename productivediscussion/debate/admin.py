"""Admin."""
from django.contrib import admin
from debate.models import Debate
from debate.models import Argument

admin.site.register(Debate)
admin.site.register(Argument)
