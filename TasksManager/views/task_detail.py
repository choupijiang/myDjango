from django.shortcuts import render, get_object_or_404
from TasksManager.models import Task
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
def page(request, pk):
    check_task =get_object_or_404(Task, id = pk)
    # This line is used to retrieve a queryset of the elements whose ID property matches to
    # the parameter pk sent to the URL. We will use this queryset in the following line : task = check_task.get().
    try:
    # This is used to define an error handling exception to the next line.
        task = check_task.get()
        # This line is used to retrieve the record in the queryset.
    except (Task.DoesNotExist, Task.MultipleObjectsReturned):
    # This allows to process the two kind of exceptions:
    # DoesNotExist and MultipleObjectsReturned.
    # The DoesNotExist   exception type is raised if the queryset has no records. \
    # The MultipleObjectsReturned exception type is raised if queryset contains multiple records.
        return HttpResponseRedirect(reverse('public_index'))
        # This line redirects the user if an exception is thrown. We could also redirect to an error page.
    else:
        request.session['last_task'] = task.id
        # This line records the ID property of the task in a session variable named last_task.
        #In this line, we use the same template that defines the form CBV DetailView. W
        # ithout having to modify the template, we send our task in a variable named object.
    return render(request, 'task_detail.html', {'object' : task})