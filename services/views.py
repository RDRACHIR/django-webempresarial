from django.shortcuts import render

from .models import Service

# Create your views here.
def service(request):
  platillos = Service.objects.all()
  return render(request, 'services/service.html', {'platillos': platillos})