from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'apps.base.views.index', name='index'),
)
