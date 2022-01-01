from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .models import Skills, Project, Art, Contact
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
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message =request.POST['message']
        if name == "" or email == "" or subject == "" or message == "":
            messages.add_message(request, messages.INFO, 'Null Data')
        else:
            contact = Contact(name = name,email = email, subject = subject, message = message)
            contact.save()
            messages.add_message(request, messages.INFO, 'Message sent')
        return redirect('/contact') #Siempre debe retornar a la misma página, entonces solo un return.
    else:
        return render(request,"contact.html")

def art(request):
    return render(request,"art.html")
