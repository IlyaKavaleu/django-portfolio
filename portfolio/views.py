from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'portfolio/home.html', context)


def about(request):
    context = {'about_site': 'About this site'}
    return render(request, 'portfolio/about.html', context)
