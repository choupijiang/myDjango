#-*- Coding: utf-8 -*-
from django.http import HttpResponse
# View for index page.
from django.shortcuts import render
from  TasksManager.models  import Project, Task, Supervisor, Developer, DeveloperWorkTask
from django.utils import timezone

def page (request) :
    # my_variable = "Hello World !"
    # years_old = 15
    # array_city_capitale = [ "Paris", "London", "Washington" ]
    # return render(request, 'index.html', {"my_var":my_variable, "years":years_old, "array_city":array_city_capitale })
    #
    # new_project = Project(title="Tasks Manager with Django",
    #                       description="Django project to getting start with Django easily.",
    #                       client_name="Me")
    # new_project.save()
    # return  render(request, 'index.html', {'action': 'Save datas of modle'})

    all_projects = Project.objects.all()
    return render(request, 'index.html', {'action':"Display all project", 'all_projects':all_projects})
    # new_supervisor = Supervisor(name="Guido van Rossum",
    #                             login="python", password="password",
    #                             last_connection=timezone.now(), email="python@python.com",
    #                             specialisation="Python") # line 1
    # new_supervisor.save()
    # # Saving a new developer
    # new_developer = Developer(name="Me", login="me",
    #                           password="pass", last_connection=timezone.now(),
    #                           email="me@python.com", supervisor=new_supervisor)
    # new_developer.save()
    # # Saving a new task
    # project_to_link = Project.objects.get(id = 1) # line 2
    # new_task = Task(title="Adding relation", description="Example of adding relation and save it", time_elapsed=2, importance=0,
    #     project=project_to_link) # line 3
    # new_task.save()
    # new_developer_task = DeveloperWorkTask(developer=new_developer, task= new_task)
    # new_developer_task.save()
    # return render(request, 'index.html', {'action' : 'Save relationship'})
    # tasks_list = Task.objects.filter(time_elapsed__gt=4)
    # array_projects = tasks_list.values_list('project',flat=True).distinct()
    # projects_list = Project.objects.all()
    # projects_list_lt4 = projects_list.exclude(id__in=array_projects)
    # return render(request, 'index.html', {'action' : 'NOT IN SQL equivalent', 'projects_list_lt4':projects_list_lt4})