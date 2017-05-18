from django.urls import reverse
from django.views.generic.edit import CreateView, FormView
from .forms import CandidateForm


class NewCandidateView(CreateView):
    form_class = CandidateForm
    template_name = 'jedi/new_candidate.html'

    def get_success_url(self):
        return reverse('try-challenge', kwargs={'candidate_id': self.object.pk,
                                                'order_id': self.object.planet_id})


class ChallengeView(FormView):
    pass
