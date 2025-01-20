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
