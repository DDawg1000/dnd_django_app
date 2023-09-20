from django.shortcuts import render, redirect
from .models import Button

def home(request):
    buttons = Button.objects.all()
    return render(request, 'home.html', {'buttons': buttons})

def increment(request, button_id):
    button = Button.objects.get(pk=button_id)
    button.count += 1
    button.save()
    return redirect('home')

# Create your views here.
