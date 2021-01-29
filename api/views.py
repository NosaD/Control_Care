# from django.shortcuts import render
# from rest_framework import generics
# from django.db.models import Q
# # Create your views here.


# from .models import Project,Assignment

# class Project_create(generics.ListCreateAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer

# class Assignment_create(generics.ListCreateAPIView):
#     queryset = Assignment.objects.all()
#     serializer_class = AssignmentSerializer

# class OpenAssignments(generics.ListAPIView,generics.UpdateAPIView):
#     queryset = Assignment.objects.filter(Q(closed=False) & Q(engineer__pk=1))
#     serializer_class = AssignmentSerializer



from django.db.models import Q
from django.core.serializers import serialize 
from django.http import JsonResponse
import jwt
import json
from rest_framework import generics
from .models import User,Project,Assignment,Technical_Query,Technical_Queries_Remarks,Engineer
from .serializers import UserSerializer,ProjectSerializer,AssignmentSerializer,TechnicalQuerySerializer,TechnicalQueryRemarkSerializer,EngineerSerializer,AssignmentRemarkSerializer
from django.http import HttpResponse
import datetime
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from backend import settings

@api_view(['POST','GET'])
def current_datetime(request):
    if request.method == 'GET':
        print('request: GET')
        print(request.user)
        test_object = Assignment.objects.all()
        print('the test object')
        print(test_object)
        now = datetime.datetime.now() 
        html = "<html><body>It is  %s request.</body></html>" % (now)
        return HttpResponse(html)
    if request.method == 'POST':
        print('request POST')
        token = request.headers['Authorization']
        payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])
        print(payload['user_id'])
        c = payload['user_id']
        engineer = Engineer.objects.get(user__id=c)
        print(engineer)
        now = datetime.datetime.now()
        html = "<html><body>It is  %s request.</body></html>" % (now)
        return HttpResponse(html)

class test(generics.ListCreateAPIView,generics.RetrieveUpdateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = UserSerializer
    lookup_fields = ['pk']
# projects
class ListProjects(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class CreateProjects(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class UpdateProjects(generics.RetrieveUpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class DeleteProjects(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class GetProjects(generics.RetrieveAPIView, generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
#assignment
class ListAssignments(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class CreateAssignments(generics.CreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer



class UpdateEngineerAssignments(generics.RetrieveUpdateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        engineers = request.data['engineer']
        pk = request.data['pk']
        assignment = Assignment.objects.get(pk=pk)
        for engineer in engineers:
            Eng = Engineer.objects.get( Q(user__username = engineer['user']['username']) & Q(department = engineer['department'])  )
            assignment.engineer.add(Eng)
        assignment.save()
        data = serialize('python',[assignment])
        return JsonResponse(data, safe=False)

class UpdateAssignments(generics.RetrieveUpdateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer




class DeleteAssignments(generics.DestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class GetAssignments(generics.RetrieveAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
#TQ
class ListTQ(generics.ListAPIView):
    queryset = Technical_Query.objects.all()
    serializer_class = TechnicalQuerySerializer

class CreateTQ(generics.CreateAPIView):
    queryset = Technical_Query.objects.all()
    serializer_class = TechnicalQuerySerializer


class UpdateTQ(generics.UpdateAPIView):
    queryset = Technical_Query.objects.all()
    serializer_class = TechnicalQuerySerializer

class DeleteTQ(generics.DestroyAPIView):
    queryset = Technical_Query.objects.all()
    serializer_class = TechnicalQuerySerializer

class GetTQ(generics.RetrieveAPIView):
    queryset = Technical_Query.objects.all()
    serializer_class = TechnicalQuerySerializer

#Engineer

class ListEngineers(generics.ListAPIView):
    queryset = Engineer.objects.all()
    serializer_class = EngineerSerializer

class CreateEngineers(generics.CreateAPIView):
    queryset = Engineer.objects.all()
    serializer_class = EngineerSerializer

    def create(self, request, *args, **kwargs):
        userobject = User.objects.get(username=request.data['user']['username'])
        department = request.data['department']
        print('getting the user')
        print(userobject)
        print(department)
        engineer = Engineer.objects.create(user=userobject,department=department)
        print(engineer)     
        data = serialize('python',[engineer])
        print(data)
        print('tada')

        return JsonResponse(data, safe=False)


class UpdateEngineers(generics.UpdateAPIView):
    queryset = Engineer.objects.all()
    serializer_class = EngineerSerializer

class DeleteEngineers(generics.DestroyAPIView):
    queryset = Engineer.objects.all()
    serializer_class = EngineerSerializer

class GetEngineers(generics.RetrieveAPIView):
    queryset = Engineer.objects.all()
    serializer_class = EngineerSerializer

#User

class ListUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateUsers(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer




class UpdateUsers(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DeleteUsers(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GetUsers(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

