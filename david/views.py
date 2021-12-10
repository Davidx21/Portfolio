from django.shortcuts import render
from django.contrib import messages
from .models import Skills, Project, Art
# Create your views here.

def index(request):
    skills = Skills.objects.all()
    projects = Project.objects.all()
    art = Art.objects.all()
    context = {"skills":skills,"projects":projects,"art":art}
    return render(request,"index.html",context)