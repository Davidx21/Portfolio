from django.shortcuts import render
from django.contrib import messages
from .models import Skills, Project, Art
# Create your views here.

def index(request):
    """skills = Skills.objects.all()
    projects = Project.objects.all()
    art = Art.objects.all()
    context = {"skills":skills,"projects":projects,"art":art}"""
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")
def work(request):
    return render(request,"work.html")
def contact(request):
    return render(request,"contact.html")
def art(request):
    return render(request,"art.html")