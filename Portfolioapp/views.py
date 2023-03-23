from django.shortcuts import render, HttpResponse

# Create your views here.

def Home(request):
    
    return render(request, "Portfolioapp/home.html")

def Projects(request):
    
    return render(request, "Portfolioapp/projects.html")

def About(request):
    
    return render(request, "Portfolioapp/about.html")

def Contact(request):
    
    return render(request, "Portfolioapp/contact.html")
