"""Database models for debates."""
from django.db import models
# from django.conf import settings
from django.contrib.auth.models import User
# from django.dispatch import receiver

from django.urls import reverse


class Debate(models.Model):
    """The database model for a debate."""

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    publication_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )


class ArgumentsFor(models.Model):
    """All of the arguments in favor of a debate."""

    argument = models.TextField(max_length=500)
    publication_date = models.DateField(auto_now_add=True)
    debate = models.ForeignKey(
        Debate,
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )

    def get_absolute_url(self):
        """The url to redirect to when an argument for is created."""
        return reverse('debate_detail', kwargs={'pk': self.debate.pk})


class ArgumentsAgainst(models.Model):
    """All of the arguments against a debate topic."""

    argument = models.TextField(max_length=500)
    publication_date = models.DateField(auto_now_add=True)
    debate = models.ForeignKey(
        Debate,
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )

    def get_absolute_url(self):
        """The url to redirect to when an argument for is created."""
        return reverse('debate_detail', kwargs={'pk': self.debate.pk})


# @receiver(models.signals.post_save, sender=ArgumentsFor)
# def update_debate_for_arguments(sender, **kwargs):
#     """When an argument for is saved, it is added to the debate model."""
#     sitter = kwargs['instance']
