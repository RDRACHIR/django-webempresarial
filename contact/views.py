from django.shortcuts import render,redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
  contact_form = ContactForm()
  
  if request.method == "POST":
    contact_form = ContactForm(data=request.POST)
    if contact_form.is_valid():
      name = request.POST.get('name', '')
      mail = request.POST.get('mail', '')
      content = request.POST.get('content', '')
      
      # Creamos el correo
      mail = EmailMessage(
        'La Sabrosa: Nuevo mensaje de contacto', #Asunto
        'De {} {}\n\nEscribio:\n\n{}'.format(name, mail, content), #Mensaje
        'lasabrosa.com', #Email de Origen
        ['ramirezrichard1709@gmail.com'], #Email de destino
        reply_to=[mail]
      )
      
      # Lo enviamos y redireccionamos
      try:
        mail.send()
        return redirect(reverse('contact')+'?ok')
      except:
        return redirect(reverse('contact')+'?fail')
      
  return render(request, 'contact/contact.html', {'form': contact_form})