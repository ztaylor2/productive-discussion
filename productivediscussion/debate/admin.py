"""Admin."""
from django.contrib import admin
from debate.models import Debate

admin.site.register(Debate)
