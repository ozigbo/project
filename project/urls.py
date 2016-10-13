"""FirstApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from  . import  views

app_name ='project'
urlpatterns =[
    # ex: //project/
    # url(r'^$',views.index, name='index'),
     url(r'^$',views.IndexView.as_view(), name='index'),
    # ex:/project/5/detail
    #url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name='detail'),
    # ex: /project/5/results/
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results,name='results'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(),name='results'),
    #ex: /project/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),
    #url(r'^(?P<question_id>[0-9]+)/vote/$',views.VoteView.as_view(),name='vote'),
    ]



