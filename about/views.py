from email.message import EmailMessage
from django.shortcuts import redirect, render
from django.http import HttpResponse
from rest_framework import generics, permissions
from mediapage.models import MediaDetail
from .models import About,Goal,Academics,CoreBgImage, GrassRoot,Capacity, CapacityList, VisionMissionValue,WhereWeWork, InternalSystemList, Goal,PartenerLogo, PartenerNetwork, InternalSystem, GoalList, Core, History
from .serializers import AboutSerializer,CoreBgImageSerializer,GoalSerializer,CapacityListSerializer, CapacitySerializer, AcademicsSerializer, GrassRootSerializer, WhereWeWorkSerializer, InternalSystemListSerializer, VisionMissionValueSerializer, PartenerNetworkSerializer, InternalSystemSerializer, GoalListSerializer, CoreSerializer, HistorySerializer
from django.http import HttpRequest
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.core.paginator import Paginator
from django.utils.translation import get_language, activate

from django.core.mail import send_mail,  EmailMessage
# from .filters import CoreDetailFilter




renderer_classes = (JSONRenderer, TemplateHTMLRenderer,)



def about(request):
    """Renders the create about page."""
    assert isinstance(request, HttpRequest)
    queryset = About.objects.all()
    serializer_class = AboutSerializer(queryset, many=True)
    media = MediaDetail.objects.all()

    # Show many contacts per page for stories
    paginator_media = Paginator(media, 10000000000000000)
    page_number_media = request.GET.get('page')
    page_obj_media = paginator_media.get_page(page_number_media)

    return render(request, 'about.html',
                  {
                      'data': serializer_class.data,
        'media' : page_obj_media
                  }
                  )



def goals(request):
    """Renders the create goals page."""
    assert isinstance(request, HttpRequest)
    queryset = GoalList.objects.all()
    serializer_class = GoalListSerializer(queryset, many=True)
    queryset = Goal.objects.all()
    img = GoalSerializer(queryset, many=True)
    media = MediaDetail.objects.all()

    # Show many contacts per page for stories
    paginator_media = Paginator(media, 10000000000000000)
    page_number_media = request.GET.get('page')
    page_obj_media = paginator_media.get_page(page_number_media)

    return render(request, 'goals.html',
                  {
                      'goal': serializer_class.data,
                      'img': img.data,
        'media' : page_obj_media
                  }
                  )


def history(request):
    """Renders the create history page."""
    assert isinstance(request, HttpRequest)
    queryset = History.objects.all()
    serializer_class = HistorySerializer(queryset, many=True)
    media = MediaDetail.objects.all()

    # Show many contacts per page for stories
    paginator_media = Paginator(media, 10000000000000000)
    page_number_media = request.GET.get('page')
    page_obj_media = paginator_media.get_page(page_number_media)

    return render(request, 'history.html',
                  {
                      'history': serializer_class.data,
        'media' : page_obj_media
                  }
                  )

def vission_mission(request):
    """Renders the create history page."""
    assert isinstance(request, HttpRequest)
    queryset = VisionMissionValue.objects.all()
    serializer_class = VisionMissionValueSerializer(queryset, many=True)
    media = MediaDetail.objects.all()

    # Show many contacts per page for stories
    paginator_media = Paginator(media, 10000000000000000)
    page_number_media = request.GET.get('page')
    page_obj_media = paginator_media.get_page(page_number_media)

    return render(request, 'vission-mission.html',
                  {
                      'data': serializer_class.data,
        'media' : page_obj_media
                  }
                  )
        


def partener_network(request):
    """Renders the create history page."""
    assert isinstance(request, HttpRequest)
    queryset = PartenerNetwork.objects.all()
    serializer_class = PartenerNetworkSerializer(queryset, many=True)
    logo_show = PartenerLogo.objects.all()
    media = MediaDetail.objects.all()

    # Show many contacts per page for stories
    paginator_media = Paginator(media, 10000000000000000)
    page_number_media = request.GET.get('page')
    page_obj_media = paginator_media.get_page(page_number_media)

    return render(request, 'parteners-networks.html',
                  {
                      'data': serializer_class.data,
                      'logo': logo_show,
        'media' : page_obj_media
                  }
                  )
def internal_system(request):
    """Renders the create history page."""
    assert isinstance(request, HttpRequest)
    queryset = InternalSystem.objects.all()
    serializer_class = InternalSystemSerializer(queryset, many=True)
    internal_list = InternalSystemList.objects.all()
    media = MediaDetail.objects.all()

    # Show many contacts per page for stories
    paginator_media = Paginator(media, 10000000000000000)
    page_number_media = request.GET.get('page')
    page_obj_media = paginator_media.get_page(page_number_media)

    return render(request, 'internal-system.html',
                  {
                      'data': serializer_class.data,
                      'list': internal_list,
        'media' : page_obj_media
                  }
                  )

def where_we_work(request):
    """Renders the create history page."""
    assert isinstance(request, HttpRequest)
    queryset = WhereWeWork.objects.all()
    serializer_class = WhereWeWorkSerializer(queryset, many=True)
    media = MediaDetail.objects.all()

    # Show many contacts per page for stories
    paginator_media = Paginator(media, 10000000000000000)
    page_number_media = request.GET.get('page')
    page_obj_media = paginator_media.get_page(page_number_media)

    return render(request, 'where-we-work.html',
                  {
                      'data': serializer_class.data,
        'media' : page_obj_media
                  }
                  )
def grass_root(request):
    """Renders the create history page."""
    assert isinstance(request, HttpRequest)
    queryset = GrassRoot.objects.all()
    serializer_class = GrassRootSerializer(queryset, many=True)
    media = MediaDetail.objects.all()

    # Show many contacts per page for stories
    paginator_media = Paginator(media, 10000000000000000)
    page_number_media = request.GET.get('page')
    page_obj_media = paginator_media.get_page(page_number_media)

    return render(request, 'crass_root.html',
                  {
                      'data': serializer_class.data,
        'media' : page_obj_media
                  }
                  )
def academics(request):
    """Renders the create history page."""
    assert isinstance(request, HttpRequest)
    queryset = Academics.objects.all()
    serializer_class = AcademicsSerializer(queryset, many=True)
    media = MediaDetail.objects.all()

    # Show many contacts per page for stories
    paginator_media = Paginator(media, 10000000000000000)
    page_number_media = request.GET.get('page')
    page_obj_media = paginator_media.get_page(page_number_media)

    return render(request, 'acadimic.html',
                  {
                      'data': serializer_class.data,
        'media' : page_obj_media
                  }
                  )
                
def capacity(request):
    assert isinstance(request, HttpRequest)
    queryset = Capacity.objects.all()
    serializer_class = CapacitySerializer(queryset, many=True)
    icapacity_list = CapacityList.objects.all()
    media = MediaDetail.objects.all()

    # Show many contacts per page for stories
    paginator_media = Paginator(media, 10000000000000000)
    page_number_media = request.GET.get('page')
    page_obj_media = paginator_media.get_page(page_number_media)

    return render(request, 'capacity.html',
                  {
                      'data': serializer_class.data,
                      'list': icapacity_list,
        'media' : page_obj_media
                  }
                  )
                
def core_list(request):
    core_list = Core.objects.all()
    assert isinstance(request, HttpRequest)
    queryset = Core.objects.all()
    serializer_class = CoreSerializer(queryset, many=True)
    media = MediaDetail.objects.all()
    core_bg = CoreBgImage.objects.all()

    # Show many contacts per page for stories
    paginator_media = Paginator(media, 10000000000000000)
    page_number_media = request.GET.get('page')
    page_obj_media = paginator_media.get_page(page_number_media)


    paginator = Paginator(core_list, 10000000000000000)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if core_list:
        context = {'core': page_obj, 
        # 'myfilter': myfilter,
                   'data': serializer_class.data,
        'media' : page_obj_media,
        'core_bg': core_bg}  # template name

    else:
        context = {'message': "There are no core available at the moment."}
    return render(request, 'core.html', context)


def core_detail(request, id):
    core_detail = Core.objects.get(id=id)
    print(core_detail)
    assert isinstance(request, HttpRequest)
    media = MediaDetail.objects.all()

    # Show many contacts per page for stories
    paginator_media = Paginator(media, 10000000000000000)
    page_number_media = request.GET.get('page')
    page_obj_media = paginator_media.get_page(page_number_media)

    context = {'core': core_detail,
        'media' : page_obj_media}
    return render(request, 'core-details.html', context)