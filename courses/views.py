from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Course, Category
from django.contrib.auth.mixins import LoginRequiredMixin





class CourseList(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'courses/home.html'

class CourseDetail(LoginRequiredMixin,DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'courses/detail.html'

def home2(request,category_name):
    courses = Course.objects.filter(category__name =category_name)
    cat = Category.objects.get(name = category_name)
    categories = Category.objects.all()
    return render(request,'courses/course.html',{"courses":courses,"categories":categories,"cat":cat})

def home(request):
    courses = Course.objects.filter(category__name = "Python")
    categories = Category.objects.all()
    cat = Category.objects.get(name = "Python")
    return render(request,'courses/home.html',{"courses":courses,"categories":categories,"cat":cat})


class CourseCreate(LoginRequiredMixin,CreateView):
    model = Course
    fields = '__all__'
    success_url =  reverse_lazy('home')

class CourseUpdate(LoginRequiredMixin,UpdateView):
    model = Course
    fields = '__all__'
    success_url = reverse_lazy('home')

