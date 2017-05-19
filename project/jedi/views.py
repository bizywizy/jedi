from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, FormView

from .forms import CandidateForm, ChallengeForm, JediSelectForm
from .models import Challenge, Candidate, Jedi


class NewCandidateView(CreateView):
    form_class = CandidateForm
    template_name = 'jedi/new_candidate.html'

    def get_success_url(self):
        return reverse('try-challenge', kwargs={'candidate_id': self.object.pk,
                                                'order_id': self.object.planet_id})


class ChallengeView(FormView):
    form_class = ChallengeForm
    template_name = 'jedi/try_challenge.html'
    success_url = reverse_lazy('passed')

    def dispatch(self, request, *args, **kwargs):
        order_id = kwargs['order_id']
        self.questions = Challenge.objects.get(order_id=order_id).question.all()
        return super(ChallengeView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(ChallengeView, self).get_form_kwargs()
        kwargs['candidate_id'] = self.kwargs['candidate_id']
        kwargs['questions'] = [(q.id, q.text) for q in self.questions]
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(ChallengeView, self).form_valid(form)


class JediSelectView(FormView):
    form_class = JediSelectForm
    template_name = 'jedi/select_jedi.html'

    def form_valid(self, form):
        return redirect(reverse('jedi', kwargs={'jedi_id': form.cleaned_data['jedi'].id}))


class JediView(ListView):
    template_name = 'jedi/jedis_candidates.html'
    context_object_name = 'candidates'

    def get_queryset(self):
        jedi = Jedi.can_teach.get(id=self.kwargs['jedi_id'])
        return Candidate.objects.filter(planet=jedi.planet)


class CandidateToPadawanView(DetailView):
    model = Candidate
    template_name = 'jedi/candidate_detail.html'
    pk_url_kwarg = 'candidate_id'
