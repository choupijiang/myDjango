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
from TasksManager.views.cbv.CreateView import Task_CreateView
from TasksManager.views.cbv.DetailView import Developer_detail
from django.views.generic import UpdateView
from TasksManager.views.cbv.UpdateView import Task_update_time
from TasksManager.views.cbv.DeleteView import Task_delete
from TasksManager.views.cbv.UpdateViewCustom import UpdateViewCustom

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace="polls"),),
    # url(r'^$', include('polls.urls'))
    url(r'^$', 'TasksManager.views.index.page'),
    url (r'^index$', 'TasksManager.views.index.page', name="public_index"),
    url(r'^connection$', 'TasksManager.views.connection.page', name="public_connection"),
    # url(r'^project-detail-(?P<pk>\d+)$', 'TasksManager.views.project_detail.page', name="project_detail"),
    url(r'^create-developer$', 'TasksManager.views.create_developer.page', name="create_developer"),
    url(r'^create-supervisor$','TasksManager.views.create_supervisor.page', name="create_supervisor"),
    # url(r'^create_project$', 'TasksManager.views.create_project.page', name='create_project'),
    # # url(r'^create_project$',
    # #     CreateView.as_view(model=Project, template_name="create_project.html", success_url="index"),
    # #     name='create_project'),
    # # url(r'^create_task$',
    # #      CreateView.as_view(model=Task, template_name="create_task.html", success_url ='index',
    # #                         fields=['title','description','importance','project']),
    # #      name="create_task"),
    # url(r'^create_task$',Task_CreateView.as_view() , name="create_task"),
    # url(r'^project_list$',Project_list.as_view(), name="project_list"),
    # # url (r'^developer_list$', ListView.as_view(model=Developer, template_name="developer_list.html"),
    # #      name="developer_list"),
    # url (r'^developer_list$', Project_list.as_view(), name = "project_list"),
    # # url (r'^task_detail_(?P<pk>\d+)$', DetailView.as_view(model=Task,
    # #                   template_name="task_detail.html"), name="task_detail"),
    # url (r'^task_detail_(?P<pk>\d+)$', 'TasksManager.views.task_detail.page', name="task_detail"),
    url (r'^developer_detail_(?P<pk>\d+)$', Developer_detail.as_view(), name="developer_detail"),
    # # url (r'^update_task_(?P<pk>\d+)$',
    # #      UpdateView.as_view(model=Task, template_name="update_task.html", success_url="index",
    # #                         fields=["title", "description", "importance", "project"]
    # #                         ),
    # #      name="update_task"),
    # url (r'^update_task_time_(?P<pk>\d+)$', Task_update_time.as_view(), name = "update_task_time"),
    # url(r'task_delete_(?P<pk>\d+)$', Task_delete.as_view(), name="task_delete"),
    # url (r'^update_task_(?P<pk>\d+)$',
    #      UpdateViewCustom.as_view(model=Task,
    #                               url_name="update_task",
    #                               success_url="public_index",
    #                              fields=["title", "description", "importance", "project"]
    #                               ), name="update_task"),
    # url (r'^task_list$', 'TasksManager.views.task_list.page', name="task_list"),
    url(r'^connection$', 'TasksManager.views.connection.page', name="public_connection"),

]
