from rest_framework import serializers

from .models import Company, Job


class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'company_name', 'industry', 'location']


class CompanyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'user', 'company_name', 'industry', 'location', 
                 'description', 'created_at', 'updated_at']
        read_only_fields = ['user']


class JobListSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.company_name')

    class Meta:
        model = Job
        fields = ['id', 'title', 'company_name', 'location', 'skills', 'deadline']


class JobDetailSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.company_name')

    class Meta:
        model = Job
        fields = ['id', 'company', 'company_name', 'title', 'description', 
                 'requirements', 'skills', 'location', 'posted_at', 'deadline']
        read_only_fields = ['company', 'posted_at'] 