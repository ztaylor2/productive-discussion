"""Database models for debates."""
from django.db import models


class Debate(models.Model):
    """The database model for a debate."""

    title = models.CharField(max_length=50)
    publication_date = models.DateField(auto_now_add=True)
