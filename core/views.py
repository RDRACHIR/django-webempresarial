from django.shortcuts import render
from .models import Page

# Create your views here.
def home(request):
  return render(request, 'core/home.html')

def history(request):
  return render(request, 'core/history.html')

def visit(request):
  return render(request, 'core/visit.html')

def other(request):
  pages = Page.objects.all()
  return render(request, 'core/other.html', {'pages': pages})
