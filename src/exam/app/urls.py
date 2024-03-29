from django.conf.urls import patterns, url
from app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^(?P<exam_id>\d+)/$', views.view, name='view'),
    url(r'^(?P<exam_id>\d+)/result/$', views.result, name='result'),
    url(r'^(?P<exam_id>\d+)/calc/$', views.calc, name='calc'),
    url(r'^logout/$', views.logout_view, name='logout'),
)
