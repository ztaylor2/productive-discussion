"""."""
from django.views.generic import ListView
from debate.models import Debate


class HomeView(ListView):
    """Home page view."""

    template_name = 'productivediscussion/home.html'
    model = Debate
    context_object_name = 'debate_list'
