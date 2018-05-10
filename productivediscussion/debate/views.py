"""Views for debate app."""

from debate.models import Debate, Argument
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class DebateCreateView(LoginRequiredMixin, CreateView):
    """Create view."""

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    template_name = 'debate/debate_create.html'
    model = Debate
    fields = ['title', 'description']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """Assign the user to the foreign key in the model."""
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class DebateDetailView(DetailView):
    """Detail view."""

    template_name = 'debate/debate_detail.html'
    model = Debate

    def get_context_data(self, **kwargs):
        """Provide the arguments for and against a debate for the view."""
        context = super().get_context_data(**kwargs)
        debate_id = self.request.path.split('/')[-1]
        debate = Debate.objects.get(id=debate_id)
        context['arguments_for'] = debate.argument_set.filter(side='For')
        context['arguments_against'] = debate.argument_set.filter(side='Against')
        return context


class ArgumentCreateView(CreateView):
    """A create view for creating an argument."""

    template_name = 'debate/argument_create.html'
    model = Argument
    fields = ['argument', 'side']

    def form_valid(self, form):
        """Assign the user to the foreign key in the model."""
        form.instance.created_by = self.request.user

        debate_id = self.request.path.split('/')[-1]
        form.instance.debate = Debate.objects.get(id=debate_id)

        return super().form_valid(form)
