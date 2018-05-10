"""Test the debate app."""
from django.test import TestCase
from debate.models import Debate


class DebateTest(TestCase):
    """Test the debate functionality."""

    def setUp(self):
        """Setup database with debate and arguments."""
        new_debate = Debate(title='Should we have stricter gun laws?')

        new_debate.save()

    def test_debate_is_created_and_title_added(self):
        """Test that a debate model instance is created by setup."""
        one_debate = Debate.objects.get(id=1)
        debate_title = one_debate.title
        self.assertEqual(debate_title, 'Should we have stricter gun laws?')
