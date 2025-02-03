from django.shortcuts import render

def index(request):
    name="HARY POTTER"
    return render(request,"index.html" , {"name":name})

# Create your views here.
