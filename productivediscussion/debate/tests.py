"""Test the debate app."""
from django.test import TestCase
from debate.models import Debate, ArgumentsFor, ArgumentsAgainst
from django.contrib.auth.models import User


class DebateTest(TestCase):
    """Test the debate functionality."""

    def setUp(self):
        """Setup database with debate and arguments."""
        user = User(password='potatoes',
                    username='zach',
                    email='zach@example.com')
        user.save()

        new_debate = Debate(title='Should we have stricter gun laws?', created_by=user)
        new_debate.save()

        one_argument_for = ArgumentsFor(argument='If its harder to get your hands on a gun it will allow people to have more time to think before doing something reckless.',
                                        debate=new_debate,
                                        created_by=user)
        one_argument_for.save()

        two_argument_for = ArgumentsFor(argument='Another argument for stricter gun laws.',
                                        debate=new_debate,
                                        created_by=user)
        two_argument_for.save()

        one_argument_against = ArgumentsAgainst(argument='One argument against.',
                                                debate=new_debate,
                                                created_by=user)
        one_argument_against.save()

        two_argument_against = ArgumentsAgainst(argument='Another argument against.',
                                                debate=new_debate,
                                                created_by=user)
        two_argument_against.save()

    def test_debate_is_created_and_title_added(self):
        """Test that a debate model instance is created by setup."""
        one_debate = Debate.objects.get(id=1)
        debate_title = one_debate.title
        self.assertEqual(debate_title, 'Should we have stricter gun laws?')

    def test_debate_multiple_arguments_for(self):
        """Test the one to many relationship for a debate and arguments for."""
        a_debate = Debate.objects.get(id=3)
        arguments_for = a_debate.argumentsfor_set.all()
        self.assertEqual(len(arguments_for), 2)

    def test_debate_multiple_arguments_against(self):
        """Test the one to many relationship for a debate and arguments for."""
        a_debate = Debate.objects.get(id=2)
        arguments_against = a_debate.argumentsagainst_set.all()
        self.assertEqual(len(arguments_against), 2)

    def test_user_can_create_multiple_arguments(self):
        """Test that a user can create multiple arguments for a debate."""
        a_user = User.objects.get(username='zach')
        arguments_for = a_user.argumentsfor_set.all()
        self.assertEqual(len(arguments_for), 2)
