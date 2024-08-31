from django.shortcuts import render

from .models import Menu

# Create your views here.
def home(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def book(request):
  return render(request, 'index.html')

def menu(request):
  menu_data = Menu.objects.order_by('name')
  main_data = {'menu': menu_data}

  return render(request, 'menu.html', main_data)