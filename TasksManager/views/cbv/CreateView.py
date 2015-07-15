# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
__author__ = 'zhangshenghu'

from django.views.generic.edit import CreateView
# In this line, we import the ListView class
from TasksManager.models import Task

class Task_CreateView(CreateView):
    model = Task
    template_name = "create_task.html"
    fields = ['title','description','importance','project']