from django.conf.urls import url
from django.views.generic import TemplateView, FormView

from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='jedi/index.html'), name='home'),
    url(r'candidate/$', views.NewCandidateView.as_view(), name='new-candidate'),
    url(r'candidate/(?P<candidate_id>[0-9]+)/order/(?P<order_id>[0-9]+)/try/$',
        views.ChallengeView.as_view(), name="try-challenge"),
    url(r'candidate/passed/$',
        TemplateView.as_view(template_name='jedi/passed_candidate.html'), name='passed'),
    url(r'jedi/$', views.JediSelectView.as_view(), name='select-jedi'),
    url(r'jedi/(?P<jedi_id>[0-9]+)/candidate/list/$', views.JediView.as_view(), name='jedi'),
    url(r'jedi/(?P<jedi_id>[0-9]+)/candidate/(?P<candidate_id>[0-9]+)/$',
        views.CandidateToPadawanView.as_view(), name='candidate'),
    url(r'jedi/list/$', views.JediListView.as_view(), name='jedi-list'),
    url(r'jedi/list/gt1/$', views.JediListMoreThanOneView.as_view(), name='jedi-list-gt1')
]
