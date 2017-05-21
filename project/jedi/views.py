from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, FormView
from django.views.generic.edit import FormMixin

from .forms import CandidateForm, ChallengeForm, JediSelectForm, AddPadawan
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
        jedi = Jedi.with_padawans.can_teach().get(id=self.kwargs['jedi_id'])
        return Candidate.objects.filter(planet=jedi.planet)

    def get_context_data(self, **kwargs):
        context = super(JediView, self).get_context_data(**kwargs)
        context['jedi_id'] = self.kwargs['jedi_id']
        return context


class CandidateToPadawanView(DetailView, FormMixin):
    model = Candidate
    template_name = 'jedi/candidate_detail.html'
    pk_url_kwarg = 'candidate_id'
    form_class = AddPadawan
    success_url = '/'

    def get_initial(self):
        return {'candidate_id': self.kwargs['candidate_id'],
                'jedi_id': self.kwargs['jedi_id']}

    def form_valid(self, form):
        form.save()
        return super(CandidateToPadawanView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class JediListView(ListView):
    queryset = Jedi.with_padawans.all()
    template_name = 'jedi/list_jedi.html'
    context_object_name = 'jedis'


class JediListMoreThanOneView(JediListView):
    queryset = Jedi.with_padawans.more_than_one()
