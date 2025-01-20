import uuid

from django.db import models

from user.models import User


class Student(models.Model):
    EDUCATION_CHOICES = [
        ('CSIT', 'Computer Science and Information Technology'),
        ('BIT', 'Bachelor in Information Technology'),
        ('BCA', 'Bachelor in Computer Application'),
        ('BIM', 'Bachelor in Information Management'),
    ]

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

    EXPERIENCE_CHOICES = [
        ('6', '6 Months'),
        ('12', '12 Months'),
        ('18', '18 Months'),
        ('24', '24 Months'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    education = models.CharField(max_length=10, choices=EDUCATION_CHOICES)
    skills = models.JSONField(default=list)  # Store array of strings
    experience = models.CharField(max_length=3, choices=EXPERIENCE_CHOICES)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
