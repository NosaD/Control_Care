from django.contrib import admin
from django.urls import path,include

from .views import current_datetime,test,CreateProjects,ListProjects,UpdateProjects,DeleteProjects,GetProjects,ListAssignments,CreateAssignments,UpdateAssignments,DeleteAssignments,GetAssignments,ListTQ,CreateTQ,UpdateTQ,DeleteTQ,GetTQ,ListEngineers,CreateEngineers,UpdateEngineerAssignments,UpdateEngineers,DeleteEngineers,GetEngineers,ListUsers,CreateUsers,UpdateUsers,DeleteUsers,GetUsers

urlpatterns = [
    path('create-project/', CreateProjects.as_view()),
    path('list-project/', ListProjects.as_view()),
    path('update-project/<int:pk>', UpdateProjects.as_view()),
    path('delete-project/<int:pk>', DeleteProjects.as_view()),
    path('get-project/<int:pk>', GetProjects.as_view()),
    path('create-assignment/', CreateAssignments.as_view()),
    path('list-assignment/', ListAssignments.as_view()),
    path('update-assignment/<int:pk>', UpdateAssignments.as_view()),
    path('delete-assignment/<int:pk>', DeleteAssignments.as_view()),
    path('get-assignment/<int:pk>', GetAssignments.as_view()),
    path('create-technical-query/', CreateTQ.as_view()),
    path('list-technical-query/', ListTQ.as_view()),
    path('update-technical-query/<int:pk>', UpdateTQ.as_view()),
    path('delete-technical-query/<int:pk>', DeleteTQ.as_view()),
    path('get-technical-query/<int:pk>', GetTQ.as_view()), 
    path('create-engineer/', CreateEngineers.as_view()),
    path('list-engineer/', ListEngineers.as_view()),
    path('update-engineer/<int:pk>', UpdateEngineers.as_view()),
    path('assignment-add-engineer/<int:pk>', UpdateEngineerAssignments.as_view()),
    path('delete-engineer/<int:pk>', DeleteEngineers.as_view()),
    path('get-engineer/<int:pk>', GetEngineers.as_view()),
    path('create-user/', CreateUsers.as_view()),
    path('list-user/', ListUsers.as_view()),
    path('update-user/<int:pk>', UpdateUsers.as_view()),
    path('delete-user/<int:pk>', DeleteUsers.as_view()),
    path('get-user/<int:pk>', GetUsers.as_view()),                                              
    path('request',current_datetime)
    
]