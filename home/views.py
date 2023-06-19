from email.message import EmailMessage
from django.shortcuts import redirect, render
from django.http import HttpResponse
from rest_framework import generics, permissions
from .models import Slider,Index
from .serializers import  SliderSerializer, IndexSerializer
from django.http import HttpRequest
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.core.paginator import Paginator
from django.utils.translation import get_language, activate

from django.core.mail import send_mail,  EmailMessage

def index(request):
    assert isinstance(request, HttpRequest)
    queryset = Index.objects.all()
    serializer_class = IndexSerializer(queryset, many=True)


   

    

    slider_show = Slider.objects.all()[:4]
    context = {
        'data': serializer_class.data,
        'slider_show': slider_show,
       
    }
    return render(request, 'index.html', context)



def contact(request):
    assert isinstance(request, HttpRequest)
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer(queryset, many=True)

    context = {
        'data': serializer_class.data,
       
    }
    return render(request, 'contact.html', context)

def contact(request):
    if request.method == 'POST':
        print("hello")
        name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = {
            'name': name,
            'phone' : phone,
            'email' : email,
            'subject' : subject,
            'message' : message,
        }
        print(data)
      
        message = ''' 
        New message :{}
        From: {}
        '''.format(data['message'], data['email'])

        if subject and message and email:
            try:
                send_mail(data['subject'], message, from_email= 'info@ashuor.org',recipient_list= ['contact@ashuor.org'],  fail_silently=False)

            except  Exception as error:
                print("error")
                print(error)
                return HttpResponse('Invalid header found.')
    return render(request, 'contact.html')


def translate(language):
    cur_language = get_language()
    try:
        activate(language)
    finally:
        activate(cur_language)
