from django.shortcuts import render, redirect, get_object_or_404
from . import views
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CSVUploadForm
import csv

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
def index(request):
    return render(request, "index.html")


def login_ad(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user,'user')
        if user is not None:
            login(request, user)
            # Redirect to a success page or homepage
            return redirect('index')
        else:
            # Display an error message if authentication fails
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def list(request):
    listt = Admin.objects.all()
    context = {'admin_listt':listt}
    return render(request, 'list.html',context)

@login_required(login_url='login')
def add(request):
    form = RegisterForm
    context = {'form': form}
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.role='Admin'
            data.save()
            messages.success(request, 'Admin Added Successfully', 'alert-success')
            return redirect('admin_list')
        else:
            print(form.errors)
            messages.success(request, 'Data is not valid.', 'alert-danger')
            context = {'form': form}
            return render(request, 'add.html', context)
    else:
        return render(request, 'add.html', context)
    
def edit(request, id):
    admin_obj = Admin.objects.get(id=id)
    form = RegisterForm(instance=admin_obj)
    context = {'form': form, 'admin_obj': admin_obj}
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES, instance=admin_obj)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.success(request, 'Admin Updated Successfully', 'alert-success')
            return redirect('list')
        else:
            print(form.errors)
            messages.success(request, 'Data is not valid.', 'alert-danger')
            context = {'form': form}
            return render(request, 'edit.html', context)
    else:
        return render(request,'edit.html', context) 

def delete(request, pk):
    deleteadmin = get_object_or_404(Admin, id=pk)
    deleteadmin.delete()
    messages.success(request, 'Admin deleted successfully.')
    return redirect('list')

def logout_ad(request):
    logout(request)
    return redirect(login_ad)

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students_list': students})


@login_required(login_url='login')
def student_create(request):
    form = StudentForm
    template_name = 'student_create.html'
    context = {'form': form}
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            print(data)
            messages.success(request, 'Student details added successfully', 'alert-success')
            return redirect('student_list')
        else:
            print(form.errors)
            messages.success(request, 'Data is not valid.', 'alert-danger')
            context = {'form': form}
            return render(request, template_name, context)
    else:
        return render(request, template_name, context)
    

def student_edit(request, id):
    std_obj = Student.objects.get(id=id)
    form = StudentForm(instance=std_obj)
    context = {'form': form, 'std_obj': std_obj}
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=std_obj)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.success(request, 'Student details Updated Successfully', 'alert-success')
            return redirect('student_list')
        else:
            print(form.errors)
            messages.success(request, 'Data is not valid.', 'alert-danger')
            context = {'form': form}
            return render(request, 'student_edit.html', context)
    else:
        return render(request,'student_edit.html', context) 
    


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    messages.success(request, 'Student deleted successfully.')
    return redirect('student_list')

def upload_students_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            reader = csv.DictReader(csv_file.read().decode('utf-8').splitlines())
            for row in reader:
                Student.objects.update_or_create(
                    email=row['email'],
                    defaults={
                        'first_name': row['first_name'],
                        'last_name': row['last_name'],
                        'date_of_birth': row['date_of_birth'],
                        'profile_picture': row.get('profile_picture'),
                    }
                )
            messages.success(request, 'Students data uploaded successfully.')
            return redirect('student_list')
    else:
        form = CSVUploadForm()
    return render(request, 'upload_students_csv.html', {'form': form})


