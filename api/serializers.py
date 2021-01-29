# from .models import Project_Description,Project,Assignment,Assignment_Remarks,Technical_Query,Technical_Queries_Remarks,User
# from rest_framework import serializers
# from drf_writable_nested.serializers import WritableNestedModelSerializer

# class UserSerializer(serializers.ModelSerializer):
#     model = User
#     fields = ['username']

# class FULLProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Project
#         fields = ['id','project_code','project_name','project_description','Assignments']

# class ProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Project
#         fields = ['id','project_code','project_name','project_description']


# class AssignmentSerializer(serializers.ModelSerializer):
#     project = ProjectSerializer()
#     class Meta:
#         model = Assignment
#         fields = ['id','item','unit','description','engineer','due_date','date_closed','project','closed','approved']
#         depth = 2

#     def create(self,validated_data):
#         projects_data = validated_data.pop('project')
#         assignment = Assignment.objects.create(**validated_data)
#         for project_data in projects_data:
#             pr = Project.objects.get_or_create(**projects_data)
#             pr(Assignments=assignment)
#         return assignment











# class Project_DescriptionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Project_Description
#         fields = "__all__"

    

# class Assignment_RemarksSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Assignment_Remarks
#         fields = "__all__"
    

# class Technical_QuerySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Technical_Query
#         fields = "__all__"

# class Technical_Queries_RemarksSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Technical_Queries_Remarks
#         fields = "__all__"

# # class ShowProjectSerializer(serializers.ModelSerializer):
#     # Assignments = AssignmentSerializer()
#     # class Meta:
#     #     model = Project
#     #     fields = ['id','project_code','project_name','project_description','Assignments']
#     # def create(self,validated_data):
#     #     assignments_data = validate_data.pop('Assignments')
#     #     project = Project.objects.create(**validated_data)
#     #     for assignments_data in assignments_data:
#     #         Assignments.objects.create(project=project,**assignments_data)
#     #     return assignments






# class ProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Project
#         fields = ['id','project_code','project_name','project_description','Assignments']

#     # def create(self,validated_data):
#     #     assignments_data = validated_data.pop('Assignments')
#     #     project = Project.objects.create(**validated_data)
#     #     for assignment_data in assignments_data:
#     #         Assignment.objects.create(project=project)
#     #     return project



# class writebleAssignmentSerializer(WritableNestedModelSerializer):
#     project = ProjectSerializer(allow_null=False)
#     engineer = UserSerializer(many=True)
#     class Meta:
#         model = Assignment
#         fields = ['id','item','unit','description','engineer','due_date','date_closed','project','closed','approved']
    
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import Approved,Milestone,User,Project_Description,Project,Assignment,Assignment_Remarks,Technical_Query,Technical_Queries_Remarks,Activity,Time_and_Expance,Engineer


class ApprovedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Approved
        fields = ['user','approved']


class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = ['goal','percentage','completed']


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['date','day','activity','project','description','working_hours']



class ProjectDescriptionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project_Description
        fields = ['project_description','customer','end_user','internal_acceptance_test_dates','factory_acceptance_test_dates','site_acceptance_test_dates']



class AssignmentRemarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assignment_Remarks
        fields = ['text']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','password','email']
            
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class UserSerializer2(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = ['username']


class EngineerSerializer(WritableNestedModelSerializer):
    user = UserSerializer2(required=False,allow_null=True)
    class Meta:
        model = Engineer
        fields = ['pk','user','department']
        

class AssignmentSerializer(WritableNestedModelSerializer):
    Approvers = ApprovedSerializer(many=True,required=False)
    engineer = EngineerSerializer(many=True,required=False)
    AssRemarks = AssignmentRemarkSerializer(many=True,required=False)
    class Meta:
        model = Assignment
        fields = ['pk','item','unit','description','engineer','due_date','date_closed','closed','approved','Approvers','AssRemarks']

    def update(self, instance, validated_data):
        print(self)
        print(instance)
        print(validated_data)
        return instance



class TechnicalQueryRemarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technical_Queries_Remarks
        fields = ['text']

class TechnicalQuerySerializer(WritableNestedModelSerializer):
    TQRemarks = TechnicalQueryRemarkSerializer(many=True,required=False)
    initiator = UserSerializer(many=True,required=False)
    actioner = UserSerializer(many=True,required=False)
    class Meta:
        model = Technical_Query
        fields = ['item','unit','description','initiator','actioner','due_date','date_closed','TQRemarks']

class ProjectSerializer(WritableNestedModelSerializer):
    milestones = MilestoneSerializer(many=True,required=False)
    Assignments = AssignmentSerializer(many=True,required=False)
    Technical_Queries = TechnicalQuerySerializer(many=True,required=False)
    project_description = ProjectDescriptionSerializer(allow_null=True,required=False)
    Activities = ActivitySerializer(many=True,required=False)
    class Meta:
        model = Project
        fields = ['project_code','project_name','project_description','milestones','Assignments','Technical_Queries','Activities']
        depth = 3


class TimeAndExpance(WritableNestedModelSerializer):
    class Meta:
        model = Time_and_Expance
        fields = ['person','period']



# class AvatarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Avatar
#         fields = ['pk', 'image']


# class SiteSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Site
#         fields = ['pk', 'url']


# class AccessKeySerializer(serializers.ModelSerializer):

#     class Meta:
#         model = AccessKey
#         fields = ['pk', 'key']


# class ProfileSerializer(WritableNestedModelSerializer):
#     # Direct ManyToMany relation
#     sites = SiteSerializer(many=True)

#     # Reverse FK relation
#     avatars = AvatarSerializer(many=True)

#     # Direct FK relation
#     access_key = AccessKeySerializer(allow_null=True)

#     class Meta:
#         model = Profile
#         fields = ['pk', 'sites', 'avatars', 'access_key']


# class UserSerializer(WritableNestedModelSerializer):
#     # Reverse OneToOne relation
#     profile = ProfileSerializer()

#     class Meta:
#         model = User
#         fields = ['pk', 'profile', 'username']


