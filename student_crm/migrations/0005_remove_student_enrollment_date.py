# Generated by Django 5.0.7 on 2024-07-28 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_crm', '0004_alter_student_enrollment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='enrollment_date',
        ),
    ]