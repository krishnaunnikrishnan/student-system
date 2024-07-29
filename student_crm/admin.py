from django.contrib import admin

from .models import Student

# Register the Student model with the admin site
admin.site.register(Student)