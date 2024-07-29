# student_crm/urls.py
from django.urls import path
from . import views
from .forms import CSVUploadForm


urlpatterns = [
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('', views.login_ad, name='login'),

    #------------------------------ crud operations of admin--------------------------------
    path('list/', views.list, name='list'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:pk>/',views.delete, name='delete'),
    path('logout_ad', views.logout_ad, name='logout_ad'),


    # ------------------------student crud-----------------------
    path('student_list/', views.student_list, name='student_list'),
    path('student_create/', views.student_create, name='student_create'),
    path('student_edit/<int:id>/', views.student_edit, name='student_edit'),
    path('student_delete/<int:pk>/',views.student_delete, name='student_delete'),


    path('upload_students/', views.upload_students_csv, name='upload_students_csv'),



    




]