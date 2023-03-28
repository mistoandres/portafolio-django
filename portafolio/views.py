from django.shortcuts import render
from .models import Project
from django.core.mail import EmailMessage
from django.conf import settings

def home(request):
    projects = Project.objects.all()

    return render(request, 'home.html', {'projects': projects})

def home(request):
    # CONTACT FORM
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        email = EmailMessage(
            'Contacto portafolio', #Subject
            f'Hola, soy {name} y me contacto a través del formulario de contacto del portafolio. \n\n Mi correo: {email}\n El asunto: {subject} \n Mi mensaje: \n \n {message}',
            settings.EMAIL_HOST_USER, #sender
            ['andreslamus23@gmail.com'] #receiver
        )

        email.fail_silently = True
        email.send()
        
    return render(request, 'layout.html', {})