"""Views for debate app."""

from debate.models import Debate
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class DebateCreateView(LoginRequiredMixin, CreateView):
    """Create view."""

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    template_name = 'debate/debate_create.html'
    model = Debate
    fields = ['title']
    success_url = reverse_lazy('home')


class DebateDetailView(DetailView):
    """Detail view."""

    template_name = 'debate/debate_detail.html'
    model = Debate


class ArgumentForCreateView(CreateView):
    """A create view for creating an argument for a debate."""


class ArgumentAgainstCreateView(CreateView):
    """A create view for creating an argument against a debate."""
