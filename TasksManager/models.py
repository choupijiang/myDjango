from django.db import models
from django.contrib.auth.models import User

# Create your models here.

error_name = {
    'required': 'You must type a name !',
    'invalid': 'Wrong format.'
}

# class UserProfile(models.Model):
#     name = models.CharField(max_length=50, verbose_name="Name", error_messages=error_name)
#     login = models.CharField(max_length=25, verbose_name="Login")
#     password = models.CharField(max_length=100, verbose_name="Password")
#     phone = models.CharField(max_length=20, verbose_name="Phone  number" , null=True, default=None, blank=True)
#     last_connection = models.DateTimeField(verbose_name="Date of last connection" , null=True, default=None, blank=True)
#     born_date = models.DateField(verbose_name="Born date", null=True, default=None, blank=True)
#     email = models.EmailField(verbose_name="Email")
#     years_seniority = models.IntegerField(verbose_name="Seniority", default=0)
#     date_created = models.DateField(verbose_name="Date of Birthday", auto_now_add=True)
#     def __unicode__(self):
#         return  self.name

class UserProfile(models.Model):
    user_auth = models.OneToOneField(User, primary_key=True, default="zhangsh")
    # name = models.CharField(max_length=50, verbose_name="Name", error_messages=error_name)
    phone = models.CharField(max_length=20, verbose_name="Phone number", null=True, default=None, blank=True)
    born_date = models.DateField(verbose_name="Born date", null=True, default=None, blank=True)
    last_connexion = models.DateTimeField(verbose_name="Date of last connexion", null=True, default=None, blank=True)
    years_seniority = models.IntegerField(verbose_name="Seniority", default=0)
    def __str__(self):
        return self.user_auth.username

class Project(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title")
    description = models.CharField(max_length=1000, verbose_name="Description")
    client_name = models.CharField(max_length=1000, verbose_name="Client name")
    def __str__(self):
        return self.title

class Supervisor(UserProfile):
    specialisation = models.CharField(max_length=50, verbose_name="Specialisation")
    # def __str__(self):
    #     return self.specialisation

class Developer(UserProfile):
    supervisor = models.ForeignKey(Supervisor, verbose_name="Supervisor")

class Task(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title")
    description = models.CharField(max_length=1000,verbose_name="Description")
    time_elapsed = models.IntegerField(verbose_name="Elapsed time" ,null=True, default=None, blank=True)
    importance = models.IntegerField(verbose_name="Importance")
    project = models.ForeignKey(Project, verbose_name="Project" ,null=True, default=None, blank=True)
    # developers = models.ManyToManyField(Developer ,through="DeveloperWorkTask")
    developer = models.ForeignKey(Developer, verbose_name="User")
    def __str__ (self):
        return self.title
    # class Meta:
    #     verbose_name = "task"
    #     verbose_name_plural = "tasks"


class DeveloperWorkTask(models.Model):
    developer = models.ForeignKey(Developer)
    task = models.ForeignKey(Task)
    time_elapsed_dev = models.IntegerField(verbose_name="Time elapsed", null=True, default=None, blank=True)