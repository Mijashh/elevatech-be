import uuid

from django.db import models

from user.models import User


class Company(models.Model):
    INDUSTRY_CHOICES = [
        ('Frontend', 'Frontend Development'),
        ('Backend', 'Backend Development'),
        ('Mobile', 'Mobile Development'),
        ('Database', 'Database Management'),
        ('DevOps', 'DevOps'),
        ('AI/ML', 'Artificial Intelligence/Machine Learning'),
        ('Graphics', 'Graphics Design'),
        ('Digital Marketing', 'Digital Marketing'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    industry = models.CharField(max_length=20, choices=INDUSTRY_CHOICES)
    location = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name_plural = "Companies"


class Job(models.Model):
    SKILL_CHOICES = [
        ('Frontend', 'Frontend Development'),
        ('Backend', 'Backend Development'),
        ('Mobile', 'Mobile Development'),
        ('Database', 'Database Management'),
        ('DevOps', 'DevOps'),
        ('AI/ML', 'Artificial Intelligence/Machine Learning'),
        ('Graphics', 'Graphics Design'),
        ('Digital Marketing', 'Digital Marketing'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    skills = models.JSONField(default=list)  # Store array of skill choices
    location = models.CharField(max_length=255)
    posted_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()

    def __str__(self):
        return f"{self.title} at {self.company.name}"

    class Meta:
        ordering = ['-posted_at']  # Show newest jobs first
