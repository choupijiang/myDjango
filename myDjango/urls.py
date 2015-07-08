"""myDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from TasksManager.models import Project, Task, Developer
from TasksManager.views.cbv.ListView import Project_list


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace="polls"),),
    # url(r'^$', include('polls.urls'))
    url(r'^$', 'TasksManager.views.index.page'),
    url (r'^index$', 'TasksManager.views.index.page', name="public_index"),
    url(r'^connection$', 'TasksManager.views.connection.page', name="public_connection"),
    url(r'^project-detail-(?P<pk>\d+)$', 'TasksManager.views.project_detail.page', name="project_detail"),
    url(r'^create-developer$', 'TasksManager.views.create_developer.page', name="create_developer"),
    url(r'^create-supervisor$','TasksManager.views.create_supervisor.page', name="create_supervisor"),
    # url(r'^create_project$', 'TasksManager.views.create_project.page', name='create_project'),
    url(r'^create_project$',
        CreateView.as_view(model=Project, template_name="create_project.html", success_url="index"),
        name='create_project'),
    url(r'^create_task$',
         CreateView.as_view(model=Task, template_name="create_task.html", success_url ='index'),
         name="create_task"),
    url(r'^project_list$',Project_list.as_view(), name="project_list"),
    url (r'^developer_list$', ListView.as_view(model=Developer, template_name="developer_list.html"),
         name="developer_list"),
    url (r'^task_detail_(?P<pk>\d+)$', DetailView.as_view(model=Task,
                      template_name="task_detail.html"), name="task_detail"),

]
