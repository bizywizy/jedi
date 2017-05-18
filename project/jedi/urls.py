from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='jedi/index.html')),
    url(r'candidate$', views.NewCandidateView.as_view(), name='new-candidate'),
    url(r'candidate/(?P<candidate_id>[0-9]+)/order/(?P<order_id>[0-9]+)/try$',
        views.ChallengeView, name="try-challenge"),

]