from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request , "web/index.html")

def contact_view(request):
    return render(request , "web/contact.html")

def about_view(request):
    return render(request , "web/about.html")