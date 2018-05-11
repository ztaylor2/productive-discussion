"""Database models for debates."""
from django.db import models
# from django.conf import settings
from django.contrib.auth.models import User
from django.dispatch import receiver

from django.urls import reverse


class Debate(models.Model):
    """The database model for a debate."""

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    publication_date = models.DateField(auto_now_add=True)
    number_of_arguments = models.IntegerField(default=0)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )


class Argument(models.Model):
    """All of the arguments in favor of a debate."""

    SIDES = (
        ('For', 'For'),
        ('Against', 'Against')
    )

    argument = models.TextField(max_length=500)
    side = models.CharField(max_length=50, choices=SIDES)
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


class Like(models.Model):
    """A model that represents a like."""

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,)
    argument = models.ForeignKey(Argument,
                                 on_delete=models.CASCADE,)
    created = models.DateTimeField(auto_now_add=True)


@receiver(models.signals.post_save, sender=Argument)
def update_debate_for_arguments(sender, **kwargs):
    """When an argument for is saved."""
    argument = kwargs['instance']
    debate = argument.debate
    debate.number_of_arguments += 1
    debate.save()
