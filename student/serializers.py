from rest_framework import serializers

from company.models import Job

from .models import Application, Student


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'education', 'skills', 'experience', 'location']


class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'user', 'full_name', 'education', 'skills', 
                 'experience', 'location', 'created_at', 'updated_at']
        read_only_fields = ['user']


class JobMinimalSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.company_name')

    class Meta:
        model = Job
        fields = ['id', 'title', 'company_name', 'location']


class ApplicationListSerializer(serializers.ModelSerializer):
    job = JobMinimalSerializer(read_only=True)
    student = StudentListSerializer(read_only=True)

    class Meta:
        model = Application
        fields = ['id', 'job', 'student', 'status', 'applied_at']


class ApplicationDetailSerializer(serializers.ModelSerializer):
    job = JobMinimalSerializer(read_only=True)
    student = StudentListSerializer(read_only=True)
    
    class Meta:
        model = Application
        fields = ['id', 'job', 'student', 'status', 'applied_at']
        read_only_fields = ['applied_at'] 