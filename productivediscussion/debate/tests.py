"""Test the debate app."""
from django.test import TestCase
from debate.models import Debate


class DebateTest(TestCase):
    """Test the debate functionality."""

    def setUp(self):
        """Setup database with debate and arguments."""
        new_debate = Debate(title='Should we have stricter gun laws?')

        new_debate.save()

    