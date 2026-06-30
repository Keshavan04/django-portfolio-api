from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project
from .forms import ContactForm



def home_view(request):
    my_projects = Project.objects.all()
    return render(request,'home.html',{'projects':my_projects})

def about_view(request):
    return render(request,'about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
        
    else:
        form = ContactForm()
    
    return render(request,'contact.html',{'form':form})