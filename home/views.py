from django.shortcuts import render, HttpResponse
from home.models import Contact

def homepage(request):
    return render(request, 'home.html')

def AboutUs(request):
    return render(request, 'AboutUs.html')

def contactus(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        cname = request.POST['cname']
        role = request.POST['role']
        query = request.POST['query']
        ins = Contact(name=name, email=email, phone=phone, cname=cname, role=role, query=query)
        ins.save()

    return render(request, 'contactus.html')