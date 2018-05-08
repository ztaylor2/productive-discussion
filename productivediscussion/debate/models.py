"""Database models for debates."""
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Debate(models.Model):
    """The database model for a debate."""

    title = models.CharField(max_length=50)
    publication_date = models.DateField(auto_now_add=True)
    created_by = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )
    arguments_for = models.ForeignKey(
        'ArgumentsFor',
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )
    arguments_against = models.ForeignKey(
        'ArgumentsAgainst',
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )


class ArgumentsFor(models.Model):
    """All of the arguments in favor of a debate."""

    argument = models.TextField(max_length=500)
    publication_date = models.DateField(auto_now_add=True)
    created_by = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None,
    )


class ArgumentsAgainst(models.Model):
    """All of the arguments against a debate topic."""

    argument = models.TextField(max_length=500)
    publication_date = models.DateField(auto_now_add=True)
    created_by = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None,
    )
