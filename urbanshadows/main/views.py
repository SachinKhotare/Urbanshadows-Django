from django.shortcuts import render, redirect

def home_redirect(request):
    return redirect('index')

def solve_the_curse(request):
    return render(request, 'index.html')
