from django import forms
from django.core.exceptions import PermissionDenied
from .models import Candidate, Answer, Jedi
from django.db import IntegrityError


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        exclude = ('jedi',)


class ChallengeForm(forms.Form):
    # переопределим конструктор формы для динамического создания полей
    def __init__(self, *args, **kwargs):
        candidate = kwargs.pop('candidate', None)
        questions = kwargs.pop('questions', None)
        super(ChallengeForm, self).__init__(*args, **kwargs)
        self.candidate = candidate
        # создание полей, где id вопроса является названием поля, а text вопроса - лейблом поля
        for q in questions:
            self.fields[str(q[0])] = forms.BooleanField(label=q[1], required=False)

    def save(self):
        try:
            for k, v in self.cleaned_data.items():
                Answer.objects.create(question_id=k, candidate=self.candidate, answer=v)
        except IntegrityError:
            raise PermissionDenied


class JediSelectForm(forms.Form):
    jedi = forms.ModelChoiceField(queryset=Jedi.with_padawans.can_teach())


class AddPadawan(forms.Form):
    take = forms.BooleanField(label='Take this candidate?', required=False)

    def save(self):
        if self.cleaned_data['take']:
            jedi = self.initial['jedi']
            candidate = self.initial['candidate']
            candidate.jedi = jedi
            candidate.save()
