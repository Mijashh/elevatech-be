# Generated by Django 5.1.4 on 2025-01-15 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(choices=[('student', 'Student'), ('organization', 'Organization')], default='student', max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
