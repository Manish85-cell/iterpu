from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'portfolio/index.html')

def intro(request):
    return render(request, 'portfolio/intro.html')

def blog(request):
    return render(request, 'portfolio/blog.html')

def cv(request):
    return render(request, 'portfolio/cv.html')

def contact(request):
    return render(request, 'portfolio/contact.html')