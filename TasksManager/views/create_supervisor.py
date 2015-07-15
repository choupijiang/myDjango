__author__ = 'zhangshenghu'
from django.shortcuts import render
from TasksManager.models import Supervisor
from django import forms
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# def page(request):
#     if len(request.POST) > 0:
#         form = Form_supervisor(request.POST)
#         if form.is_valid():
#             form.save(commit=True)
#             # If the form is valid, we store the data in a model record in the form.
#             return HttpResponseRedirect(reverse('public_index'))
#             # This line is used to redirect to the specified URL. We use
#             # the reverse() function to get the URL from its name defines urls.py.
#         else:
#             return render(request, 'create_supervisor.html', {'form': form})
#     else:
#         form = Form_supervisor()
#         return render(request, 'create_supervisor.html', {'form': form})
#
#
# class Form_supervisor(forms.ModelForm):
# # Here we create a class that inherits from ModelForm.
#     class Meta:
#     # We extend the Meta class of the ModelForm. It is this class
#     # that will allow us to define the properties of ModelForm.
#         model = Supervisor
#         # We define the model that should be based on the form.
#         exclude = ('date_created', 'last_connexion', )
#         # We exclude certain fields of this form. It would also have
#         # been possible to do the opposite. That is to say with the fields
#         # property, we have defined the desired fields in the form.

from django.shortcuts import render
from TasksManager.models import Supervisor
from django import forms
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
def page(request):
    if request.POST:
        form = Form_supervisor(request.POST)
        if form.is_valid():
            name           = form.cleaned_data['name']
            login          = form.cleaned_data['login']
            password       = form.cleaned_data['password']
            specialisation = form.cleaned_data['specialisation']
            email          = form.cleaned_data['email']
            new_user = User.objects.create_user(username = login, email = email, password=password)
            # In this line, we create an instance of the User model with the create_user() method. It is important to use this method because it can store a hashcode of the password in database. In this way, the password cannot be retrieved from the database. Django uses the PBKDF2 algorithm to generate the hash code password of the user.
            new_user.is_active = True
            # In this line, the is_active attribute defines whether the user can connect or not. This attribute is false by default which allows you to create a system of account verification by email, or other system user validation.
            new_user.last_name=name
            # In this line, we define here the name of the new user.
            new_user.save()
            # In this line, we register the new user in the database.
            new_supervisor = Supervisor(user_auth = new_user, specialisation=specialisation)
            # In this line, we create the new supervisor with the form data. We do not forget to create the relationship with the User model by setting the property user_auth with new_user instance.
            new_supervisor.save()
            return HttpResponseRedirect(reverse('public_index'))
        else:
            return render(request, 'create_supervisor.html', {'form' : form})
    else:
        form = Form_supervisor()
    form = Form_supervisor()
    return render(request, 'create_supervisor.html', {'form' : form})

class Form_supervisor(forms.Form):
    name = forms.CharField(label="Name", max_length=30)
    login = forms.CharField(label = "Login")
    email = forms.EmailField(label = "Email")
    specialisation = forms.CharField(label = "Specialisation")
    password = forms.CharField(label = "Password", widget = forms.PasswordInput)
    password_bis = forms.CharField(label = "Password", widget = forms.PasswordInput)
    def clean(self):
        cleaned_data = super (Form_supervisor, self).clean()
        password = self.cleaned_data.get('password')
        password_bis = self.cleaned_data.get('password_bis')
        if password and password_bis and password != password_bis:
            raise forms.ValidationError("Passwords are not identical.")
        return self.cleaned_data