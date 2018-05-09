"""Database models for debates."""
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.dispatch import receiver


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


class ArgumentsFor(models.Model):
    """All of the arguments in favor of a debate."""

    argument = models.TextField(max_length=500)
    publication_date = models.DateField(auto_now_add=True)
    debate = models.ForeignKey(
        'Debate',
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )
    created_by = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )


class ArgumentsAgainst(models.Model):
    """All of the arguments against a debate topic."""

    argument = models.TextField(max_length=500)
    publication_date = models.DateField(auto_now_add=True)
    debate = models.ForeignKey(
        'Debate',
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )
    created_by = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )


@receiver(models.signals.post_save, sender=ArgumentsFor)
def update_debate_for_arguments(sender, **kwargs):
    """When an argument for is saved, it is added to the debate model."""
    import pdb; pdb.set_trace()

    sitter = kwargs['instance']


    # letters_seen = set()
    # num_unique_letters = 0
    # for char in sitter.name.lower():
    #     if char.isalpha() and char not in letters_seen:
    #         num_unique_letters += 1

    # sitter_score = 5 * (num_unique_letters / 26)

    # sitter_rank, created = SitterRank.objects.get_or_create(
    #     sitter=sitter,
    #     defaults={'sitter_score': sitter_score, 'sitter_rank': sitter_score})