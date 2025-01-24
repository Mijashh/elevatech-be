from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Company, Job
from .serializers import (
    CompanyDetailSerializer,
    CompanyListSerializer,
    JobDetailSerializer,
    JobListSerializer,
)


class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Company.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return CompanyListSerializer
        return CompanyDetailSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class JobViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        if hasattr(self.request.user, 'company'):
            return Job.objects.filter(company=self.request.user.company)
        return Job.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return JobListSerializer
        return JobDetailSerializer
    
    def perform_create(self, serializer):
        company = get_object_or_404(Company, user=self.request.user)
        serializer.save(company=company)
