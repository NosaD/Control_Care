from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class User(models.Model):
    
#     password = models.CharField(max_length=100, blank=True, null=True),
#     last_login = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
#     is_superuser = models.BooleanField(default=False),
#     username = models.CharField(  max_length=50),
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField( max_length=50)
#     email = models.EmailField(max_length=254,null=True)
#     is_staf = models.BooleanField(default=True)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(auto_now=False, auto_now_add=False,null=True)


class Approved(models.Model):
    user = models.ForeignKey('Assignment', related_name='Approvers', on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

class Milestone(models.Model):
    project = models.ForeignKey("Project", related_name= "milestones", on_delete=models.CASCADE)
    goal = models.CharField(max_length=255 ,blank=True, null=True)
    percentage = models.IntegerField(blank=True, null=True)
    completed = models.BooleanField(default=False)

class File(models.Model):
    file_name = models.CharField(max_length=100)
    upload = models.FileField(upload_to='uploads/', max_length=100)

class Project_Description(models.Model):
    project_description = models.CharField(max_length=255,null=True,blank=True)
    customer = models.CharField(max_length=255,null=True,blank=True)
    end_user = models.CharField(max_length=255,null=True,blank=True)
    internal_acceptance_test_dates = models.DateField(null=True,blank=True)
    factory_acceptance_test_dates = models.DateField(null=True,blank=True)
    site_acceptance_test_dates = models.DateField(null=True,blank=True)

class Project(models.Model):
    project_code = models.IntegerField(null=True,blank=True,verbose_name="project code")
    project_name = models.CharField(max_length=255,null=True,blank=True)
    project_description = models.OneToOneField(Project_Description,on_delete=models.CASCADE,null=True,blank=True)
    

class Engineer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username + ' '  + self.department

class Assignment(models.Model):
    item = models.IntegerField()
    unit = models.CharField(max_length=255,null=True,blank=True)
    description = models.CharField(max_length=255,null=True,blank=True)
    engineer = models.ManyToManyField(Engineer,related_name="Assignments_for_Engineer",blank=True)
    due_date = models.DateField(null=True)
    date_closed = models.DateField(null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="Assignments",null=True)
    closed = models.BooleanField(default = False)
    approved = models.BooleanField(default = False)

class Assignment_Remarks(models.Model):
    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE,related_name='AssRemarks')
    text = models.TextField()

class Technical_Query(models.Model):
    item = models.IntegerField()
    unit = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    initiator = models.ManyToManyField(User,related_name="Initator")
    actioner = models.ManyToManyField(User, related_name="Action_taker")
    due_date = models.DateField(blank=True, null=True)
    date_closed = models.DateField(blank=True, null=True)
    projects = models.ForeignKey(Project, on_delete=models.CASCADE,related_name="Technical_Queries")

class Technical_Queries_Remarks(models.Model):
    technical_queries = models.ForeignKey(Technical_Query,on_delete=models.CASCADE,related_name='TQRemarks')
    text = models.TextField()

class Activity(models.Model):
    date = models.DateField(null=True,blank=True)
    day = models.CharField(max_length=255,null=True,blank=True)
    activity = models.CharField(max_length=255,null=True,blank=True)
    project = models.ManyToManyField(Project,blank=True,related_name="Activities")
    description = models.CharField(max_length=255,null=True,blank=True)
    working_hours = models.IntegerField(verbose_name="Working hours",null=True,blank=True)
    travelling_hours = models.IntegerField(verbose_name="Traveling hours",null=True,blank=True)
    leave_hours = models.IntegerField(verbose_name="Leave hours",null=True,blank=True)
    bank_holiday_hours = models.IntegerField(verbose_name="Bank holiday hours",null=True,blank=True)
    offshore = models.BooleanField(default=False,null=True,blank=True)
    kilometers = models.IntegerField()
    per_diem_applicable = models.BooleanField(default=False,verbose_name="Per diem applicable")
    location = models.CharField(max_length=255,null=True,blank=True)
    breakfast = models.BooleanField(default=False,null=True,blank=True)
    lunch = models.BooleanField(default=False,null=True,blank=True)
    dinner = models.BooleanField(default=False,null=True,blank=True)
    time_expance = models.ForeignKey("Time_and_Expance",on_delete=models.CASCADE,null=True,blank=True)

class Time_and_Expance(models.Model):
    person = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    period = models.CharField(max_length=255,null=True,blank=True)

MODELS = [ Project_Description,Project,Assignment,Assignment_Remarks,Technical_Query,Technical_Queries_Remarks,Engineer,File]

from django.contrib import admin

for model in MODELS:
    admin.site.register(model)
# -------------------------------------------------------------------------------------------------------------------------

# from django.db import models

# class User(models.Model):
#     def __str__(self):
#         return self.username

# class Site(models.Model):
#     url = models.CharField(max_length=100)


# class User(models.Model):
#     username = models.CharField(max_length=100)


# class AccessKey(models.Model):
#     key = models.CharField(max_length=100)


# class Profile(models.Model):
#     sites = models.ManyToManyField(Site)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     access_key = models.ForeignKey(AccessKey, null=True, on_delete=models.CASCADE)


# class Avatar(models.Model):
#     image = models.CharField(max_length=100)
#     profile = models.ForeignKey(Profile, related_name='avatars', on_delete=models.CASCADE)