from django import forms
from django.http import Http404
from .models import Candidate, Answer, Jedi


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        exclude = ('jedi',)


class ChallengeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        candidate_id = kwargs.pop('candidate_id', None)
        questions = kwargs.pop('questions', None)
        if None in (candidate_id, questions):
            raise Http404
        super(ChallengeForm, self).__init__(*args, **kwargs)
        self.candidate_id = candidate_id
        for q in questions:
            self.fields[str(q[0])] = forms.BooleanField(label=q[1], required=False)

    def save(self):
        for k, v in self.cleaned_data.items():
            Answer.objects.create(question_id=k, candidate_id=self.candidate_id, answer=v)


class JediSelectForm(forms.Form):
    jedi = forms.ModelChoiceField(queryset=Jedi.can_teach.all())

