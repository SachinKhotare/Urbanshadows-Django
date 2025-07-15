from django.shortcuts import render
from .models import Contact

def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword= request.POST.get('confirmPassword')

        Contact.objects.create(name=name, email=email, password=password,confirmPassword=confirmPassword)

    return render(request, 'register_page.html')
