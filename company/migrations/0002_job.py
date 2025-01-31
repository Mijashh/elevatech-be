# Generated by Django 4.2.16 on 2025-01-21 03:44

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('requirements', models.TextField()),
                ('skills', models.JSONField(default=list)),
                ('location', models.CharField(max_length=255)),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='company.company')),
            ],
            options={
                'ordering': ['-posted_at'],
            },
        ),
    ]
