from django.conf.urls import url
from . import views

urlpatterns = [
    #localhost:8000/polls/
    url(r'^$', views.index, name='index'),

    #http://localhost:8000/polls/<question_id>/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name = 'detail'),
    #http://localhost:8000/polls/<question_id>/results
    url(r'^(?P<question_id>[0-9]+)/results$', views.results, name = 'results'),
    #http://localhost:8000/polls/<question_id>/vote
    url(r'^(?P<question_id>[0-9]+)/vote$', views.vote, name = 'vote'),

]