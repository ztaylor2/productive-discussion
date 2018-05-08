"""Database models for debates."""
from django.db import models


class Debate(models.Model):
    """The database model for a debate."""

    title = models.CharField(max_length=50)
    publication_date = models.DateField(auto_now_add=True)
    arguments_for = models.ForeignKey(
        'ArgumentsFor',
        on_delete=models.CASCADE
    )
    arguments_against = models.ForeignKey(
        'ArgumentsAgainst',
        on_delete=models.CASCADE
    )


class ArgumentsFor(models.Model):
    """All of the arguments in favor of a debate."""


class ArgumentsAgainst(models.Model):
    """All of the arguments against a debate topic."""
