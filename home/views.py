from email.message import EmailMessage
from django.shortcuts import redirect, render
from django.http import HttpResponse
from rest_framework import generics, permissions
from mediapage.models import MediaDetail
from .models import Slider,Index, Contact
from .serializers import  SliderSerializer, IndexSerializer
from django.http import HttpRequest
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.core.paginator import Paginator
from django.utils.translation import get_language, activate
from about.models import PartenerLogo
from django.core.mail import send_mail,  EmailMessage
from what_we_are_doing.models import Themes
def index(request):
    assert isinstance(request, HttpRequest)
    queryset = Index.objects.all()
    serializer_class = IndexSerializer(queryset, many=True)
    media = MediaDetail.objects.all()

    # Show many contacts per page for stories
    paginator_media = Paginator(media, 10000000000000000)
    page_number_media = request.GET.get('page')
    page_obj_media = paginator_media.get_page(page_number_media)
    logo_show = PartenerLogo.objects.all()
    themes = Themes.objects.all()

    # Show many contacts per page for stories
    slider_show = Slider.objects.all()[:4]
    context = {
        'data': serializer_class.data,
        'slider_show': slider_show,
        'media' : page_obj_media,
        'logo':  logo_show,
                'themes': themes,

       
    }
    return render(request, 'index.html', context)




def contact(request):
    queryset = Contact.objects.all()
    media = MediaDetail.objects.all()
    assert isinstance(request, HttpRequest)

    # Show many contacts per page for stories
    paginator_media = Paginator(media, 10000000000000000)
    page_number_media = request.GET.get('page')
    page_obj_media = paginator_media.get_page(page_number_media)

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
    return render(request, 'contact.html',
    {
                'data': queryset,
         'media' : page_obj_media
    })


def translate(language):
    cur_language = get_language()
    try:
        activate(language)
    finally:
        activate(cur_language)
