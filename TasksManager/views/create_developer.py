# -*- coding: utf-8 -*-
import sys

reload(sys)

sys.setdefaultencoding('utf-8')

from django.shortcuts import render
from django.http import HttpResponse
from TasksManager.models import Supervisor, Developer
from django import  forms
# View for create_developer
# def page(request):
#     error = False
#     # If form has posted
#     if request.POST:
#     # This line checks if the data was sent in POST. If so, this    means that the form has been submitted and we should treat it.
#         if 'name' in request.POST:
#         # This line checks whether a given data named name exists in     the POST variables.
#             name = request.POST.get('name', '')
#         # This line is used to retrieve the value in the POST   dictionary. Normally, we perform filters to recover the data to
#         # avoid false data, but it would have required many lines of code.
#         else:
#             error=True
#         if 'login' in request.POST:
#             login = request.POST.get('login', '')
#         else:
#             error=True
#         if 'password' in request.POST:
#             password = request.POST.get('password', '')
#         else:
#             error=True
#         if 'supervisor' in request.POST:
#             supervisor_id = request.POST.get('supervisor', '')
#         else:
#             error=True
#         if not error:
#         # We must get the supervisor
#             supervisor = Supervisor.objects.get(id = supervisor_id)
#             new_dev = Developer(name=name, login=login, password=password, supervisor=supervisor)
#             new_dev.save()
#             return HttpResponse("Developer added")
#         else:
#             return HttpResponse("An error as occured")
#     else:
#         supervisors_list = Supervisor.objects.all()
#         return render(request, 'create_developer.html', {'supervisors_list':supervisors_list})

class Form_inscription(forms.Form):
    error_name = {
        'required': 'You must type a name !',
        'invalid': 'Wrong format.'
    }
    name = forms.CharField(label="Name", max_length=30, error_messages=error_name, initial="new")
    login = forms.CharField(label="Login", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    # We add another field for the password. This field will be used
    # to avoid typos from the user. If both passwords do not match, the
    # validation will display an error message
    password_bis = forms.CharField(label = "Password", widget = forms.PasswordInput)
    supervisor = forms.ModelChoiceField(label="Supervisor", queryset=Supervisor.objects.all(),
                                        initial=Supervisor.objects.all()[:1].get().id)
    def clean(self):
        # This line allows us to extend the clean method that is  responsible for validating data fields.
        cleaned_data = super(Form_inscription, self).clean()
        # This method is very useful because it performs the clean()
        # method of the superclass. Without this line we would be rewriting
        # the method instead of extending it.
        password = self.cleaned_data.get('password')
        # We get the value of the field password in the variable.
        password_bis = self.cleaned_data.get('password_bis')
        if password and password_bis and password != password_bis:
            raise forms.ValidationError("Passwords are not identical.")
            # This line makes us raise an exception. This way, when the
            # view performs the is_valid() method, if the passwords are not
            # identical, the form is not validated .
        return self.cleaned_data

def page(request):
    if request.POST:
        form = Form_inscription(request.POST)
        # If the form has been posted, we create the variable that
        # will contain our form filled with data sent by POST form.
        if form.is_valid():
        # This line checks that the data sent by the user is
        # consistent with the field that has been defined in the form.
            name = form.cleaned_data['name']
            # This line is used to retrieve the value sent by the client.
            # The collected data is filtered by the clean() method that we will
            # see later. This way to recover data provides secure data.
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            supervisor = form.cleaned_data['supervisor']
            # In this line, the supervisor variable is of the Supervisor
            # type, that is to say that the returned data by the cleaned_data
            # dictionary will directly be a model.
            new_developer = Developer(name=name, login=login,
                                      password=password, email="", supervisor=supervisor)
            new_developer.save()
            return HttpResponse("Developer added")
        else:
            return render(request, 'create_developer.html',{'form' : form})
            # To send forms to the template, just send it like any other
            # variable. We send it in case the form is not valid in order to
            # display user errors:
    else:
        form = Form_inscription()
        # form = Form_inscription(initial={'name':'new', 'supervisor':Supervisor.objects.all()[:1].get().id})
        # In this case, the user does not yet display the form, it instantiates with no data inside.
        return render(request, 'create_developer.html', {'form' : form})