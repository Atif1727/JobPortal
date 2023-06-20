from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='login')
def index(request):
    return render(request , "pages/index.html")  

def login(request):
    return render(request, "pages/login.html")


def register(request):
    return render(request, "pages/register.html")
