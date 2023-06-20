from typing import List
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import GetInvolved,Volunteer, Donate,CareerDetail,CareerList
from django.core.paginator import Paginator
# from .form import CareerDetailForm
from django.urls import reverse
from django.http import HttpRequest
from .serializers import GetInvolvedSerializer,VolunteerSerializer,CareerListSerializer, DonateSerializer,CareerDetailSerializer
from .filters import CareerDetailFilter
from django.core.mail import send_mail,  EmailMessage


# Create your views here.
def get_involved(request):
    """Renders the create get_involved page."""
    assert isinstance(request, HttpRequest)
    queryset = GetInvolved.objects.all()
    serializer_class = GetInvolvedSerializer(queryset, many=True)

    return render(request, 'get-involved.html',
                  {
                      'data': serializer_class.data,
                  }
                  )

def volunteer(request):
    """Renders the create volunteer page."""
    assert isinstance(request, HttpRequest)
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer(queryset, many=True)

    return render(request, 'volunteers.html',
                  {
                      'data': serializer_class.data,
                  }
                  )


def volunteerForm(request):
    if request.method == 'POST':
        print("hello")
        name = request.POST.get('full_name')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        region = request.POST.get('region')
        address = request.POST.get('address')
        upload_cv = request.FILES.get('upload_cv')
        English = request.POST.get('English')
        Arabic = request.POST.get('Arabic')
        Kurdish = request.POST.get('Kurdish')
        languages = {"English": English,
        "Arabic":Arabic,
        "Kurdish":Kurdish
        }
        cover_letter = request.POST.get('cover_letter')
        # print(select_language)
        select_language = []

        for language in languages:
            print(language)
            if languages[language] != None:
                select_language.append(language)
        data = {
            'name': name,
            'gender' : gender,
            'email' : email,
            'phone' : phone,
            'region' : region,

            'address': address,
            'upload_cv' : upload_cv,
            'select_language' : select_language,
            'cover_letter' : cover_letter,
        }
        print(data)
        print("hello")
        message = ''' 
        New applicant :{}
        From: {}
        Phone: {}
        Region: {}
        Gender: {}
        Address:{}
        CV: {}
        Language:{}
        Cover_letter: {}


        '''.format(data['name'], data['email'], data['phone'], data['region'], data['gender'], data['address'], data['upload_cv'], data['select_language'], data['cover_letter'])

        if name and gender and email  and phone and  region  and  address and   upload_cv  and cover_letter:

            email = EmailMessage(
                              data['name'],    
                              message,
                              'info@ashuor.org', ['volunteer@ashuor.org'],)
                          
            if request.FILES:
                            uploaded_file = request.FILES['upload_cv'] # file is the name value which you have provided in form for file field
                            email.attach(uploaded_file.name, uploaded_file.read(), uploaded_file.content_type)
                            email.send()
            #     send_mail(data['carrer_name'], message, from_email= 'info@ashuor.org',recipient_list= ['hr@aifrd.org'],  fail_silently=False)
            #     send_mail.attach(message. attach.read(), )
            #     send_mail.send()
            # except  Exception as error:
            #     return HttpResponse('Invalid header found.')
    return render(request, 'volunteer.html')
def donate(request):
    """Renders the create volunteer page."""
    assert isinstance(request, HttpRequest)
    queryset = Donate.objects.all()
    serializer_class = DonateSerializer(queryset, many=True)

    return render(request, 'donate.html',
                  {
                      'data': serializer_class.data,
                  }
                  )

def career_list(request):
    career_list = CareerDetail.objects.all()
    assert isinstance(request, HttpRequest)
    queryset = CareerList.objects.all()
    serializer_class = CareerListSerializer(queryset, many=True)

    # filters
    myfilter = CareerDetailFilter(request.GET, queryset=career_list)
    career_list = myfilter.qs

    # Show many contacts per page.
    paginator = Paginator(career_list, 10000000000000000)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if career_list:
        context = {'careers': page_obj, 'myfilter': myfilter,
                   'data': serializer_class.data}  # template name

    else:
        context = {'message': "There are no jobs available at the moment."}
    return render(request, 'career.html', context)


def career_detail(request, id):
    career_detail = CareerDetail.objects.get(id=id)
    print(career_detail)
    assert isinstance(request, HttpRequest)
    queryset = CareerList.objects.all()
    serializer_class = CareerListSerializer(queryset, many=True)

    context = {'careers': career_detail, 'data': serializer_class.data}
    return render(request, 'careers-details.html', context)
    
def careerForm(request,carrer_name):
    if request.method == 'POST':
        print("hello")
        name = request.POST.get('full_name')
        # career_name = request.POST.get('career_name')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        region = request.POST.get('region')
        address = request.POST.get('address')
        upload_cv = request.FILES.get('upload_cv')
        English = request.POST.get('English')
        Arabic = request.POST.get('Arabic')
        Kurdish = request.POST.get('Kurdish')
        languages = {"English": English,
        "Arabic":Arabic,
        "Kurdish":Kurdish
        }
        cover_letter = request.POST.get('cover_letter')
        # print(select_language)
        select_language = []

        for language in languages:
            print(language)
            if languages[language] != None:
                select_language.append(language)
        data = {
            'name': name,
            'carrer_name':carrer_name,
            'gender' : gender,
            'email' : email,
            'phone' : phone,
            'region' : region,

            'address': address,
            'upload_cv' : upload_cv,
            'select_language' : select_language,
            'cover_letter' : cover_letter,
        }
        print(data)
        message = ''' 
        New applicant :{}
        From: {}
        Career Name : {}
        Phone: {}
        Region: {}
        Gender: {}
        Address:{}
        CV: {}
        Language:{}
        Cover_letter: {}


        '''.format(data['name'], data['email'],data['carrer_name'], data['phone'], data['region'], data['gender'], data['address'], data['upload_cv'], data['select_language'], data['cover_letter'])

        if name and gender and email and carrer_name and phone and  region and address and   upload_cv  and cover_letter:
         
            email = EmailMessage(
                              data['carrer_name'],    
                              message,
                              'info@ashuor.org', ['hr@ashuor.org'],)
                          
            if request.FILES:
                            uploaded_file = request.FILES['upload_cv'] # file is the name value which you have provided in form for file field
                            email.attach(uploaded_file.name, uploaded_file.read(), uploaded_file.content_type)
                            email.send()
            #     send_mail(data['carrer_name'], message, from_email= 'representative@aifrd.org',recipient_list= ['hr@aifrd.org'],  fail_silently=False)
            #     send_mail.attach(message. attach.read(), )
            #     send_mail.send()
            # except  Exception as error:
            return HttpResponse('Invalid header found.')
    return render(request, 'formCareer.html')

