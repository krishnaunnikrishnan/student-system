from django.db import models
from django.contrib.auth.models import AbstractUser




class Admin(AbstractUser):
    ROLE_TYPES = (
        ('ADMIN', 'ADMIN'),
        ('STUDENT', 'STUDENT'),
    )
    role = models.CharField(max_length=10, choices=ROLE_TYPES)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='adminuser_set',  # Custom related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='adminuser_set',  # Custom related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.username

    
    
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


