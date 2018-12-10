from django.conf.urls import patterns, url

from webblog import views

urlpatterns = patterns(
    '',
    url(r'^$', views.get_name, name='index'),
    url(r'^thanks$', views.thanks, name='thanks'),
    # url(r'^your-name$', views.get_name, name='your-name'),
    # url(r'^(?P<pk>\d+)$', views.DetailView.as_view(), name='detail'),
    # url(
    #     r'^(?P<pk>\d+)/results$',
    #     views.ResultsView.as_view(), name='results'),
    # url(r'^$', views.index, name='index'),
    # url(r'^(?P<question_id>\d+)/vote$', views.vote, name='vote')
)

#eof
