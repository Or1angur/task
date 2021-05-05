from django.shortcuts import render
from .models import Course

def home(request):
    return render(request, 'appl/layout.html', {})

def list(request):
    oneCourse = Course.objects.all()
    return render(request, 'appl/course_list.html', {'oneCourse': oneCourse})

def about(request):
    return render(request, 'appl/about.html', {})

def course(request):
    return render(request, 'appl/course.html', {})
