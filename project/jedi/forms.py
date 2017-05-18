from django import forms
from .models import Candidate, Answer


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        exclude = ('jedi',)


class ChallengeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.candidate_id = kwargs.pop('candidate_id', None)
        self.order_id = kwargs.pop('order_id', None)
        super(ChallengeForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Answer
        fields = ('question', 'answer')
        widget