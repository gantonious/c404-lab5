from django.conf.urls import url
from . import views

urlpatterns = [
    # /poll/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /poll/5
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /poll/5/results
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # /poll/5/vote
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote')
]