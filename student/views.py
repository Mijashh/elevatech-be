from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from company.models import Job

from .models import Application, Job, Student
from .serializers import (
    ApplicationDetailSerializer,
    ApplicationListSerializer,
    StudentDetailSerializer,
    StudentListSerializer,
)

# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return StudentListSerializer
        return StudentDetailSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ApplicationViewSet(viewsets.ModelViewSet):
    
    def get_queryset(self):
        # import ipdb; ipdb.set_trace()
        # If user is a student, show only their applications
        if hasattr(self.request.user, 'student'):
            return Application.objects.filter(student=self.request.user.student)
        # If user is a company, show applications for their jobs
        elif hasattr(self.request.user, 'company'):
            return Application.objects.filter(job__company=self.request.user.company)
        return Application.objects.none()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ApplicationListSerializer
        return ApplicationDetailSerializer
    
    def perform_create(self, serializer):
        student = get_object_or_404(Student, user=self.request.user)
        job = get_object_or_404(Job, id=self.request.data.get('job'))
        serializer.save(student=student, job=job)
