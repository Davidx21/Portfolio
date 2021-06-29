from django.shortcuts import render
from django.contrib import messages
from .models import Skills
# Create your views here.

def index(request):
    skills = Skills.objects.all()
    context = {"skills":skills}
    return render(request,"index.html",context)