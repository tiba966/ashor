from email.message import EmailMessage
from django.shortcuts import redirect, render
from django.http import HttpResponse
from rest_framework import generics, permissions
from .models import About,Goal, VisionMissionValue, PartenerNetwork, InternalSystem, GoalList, Core, History
from .serializers import AboutSerializer,GoalSerializer, VisionMissionValueSerializer, PartenerNetworkSerializer, InternalSystemSerializer, GoalListSerializer, CoreSerializer, HistorySerializer
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

    return render(request, 'about.html',
                  {
                      'data': serializer_class.data,
                  }
                  )



def goals(request):
    """Renders the create goals page."""
    assert isinstance(request, HttpRequest)
    queryset = GoalList.objects.all()
    serializer_class = GoalListSerializer(queryset, many=True)

    return render(request, 'goals.html',
                  {
                      'goal': serializer_class.data,
                  }
                  )


def history(request):
    """Renders the create history page."""
    assert isinstance(request, HttpRequest)
    queryset = History.objects.all()
    serializer_class = HistorySerializer(queryset, many=True)

    return render(request, 'history.html',
                  {
                      'history': serializer_class.data,
                  }
                  )

def vission_mission(request):
    """Renders the create history page."""
    assert isinstance(request, HttpRequest)
    queryset = VisionMissionValue.objects.all()
    serializer_class = VisionMissionValueSerializer(queryset, many=True)

    return render(request, 'vission-mission.html',
                  {
                      'data': serializer_class.data,
                  }
                  )
        


def partener_network(request):
    """Renders the create history page."""
    assert isinstance(request, HttpRequest)
    queryset = PartenerNetwork.objects.all()
    serializer_class = PartenerNetworkSerializer(queryset, many=True)

    return render(request, 'parteners-networks.html',
                  {
                      'data': serializer_class.data,
                  }
                  )
def internal_system(request):
    """Renders the create history page."""
    assert isinstance(request, HttpRequest)
    queryset = InternalSystem.objects.all()
    serializer_class = InternalSystemSerializer(queryset, many=True)

    return render(request, 'internal-system.html',
                  {
                      'data': serializer_class.data,
                  }
                  )

def where_we_work(request):
    """Renders the create history page."""
    assert isinstance(request, HttpRequest)
    queryset = InternalSystem.objects.all()
    serializer_class = InternalSystemSerializer(queryset, many=True)

    return render(request, 'where-we-work.html',
                  {
                      'data': serializer_class.data,
                  }
                  )

def core_list(request):
    core_list = Core.objects.all()
    assert isinstance(request, HttpRequest)
    queryset = Core.objects.all()
    serializer_class = CoreSerializer(queryset, many=True)


    paginator = Paginator(core_list, 10000000000000000)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if core_list:
        context = {'core': page_obj, 
        # 'myfilter': myfilter,
                   'data': serializer_class.data}  # template name

    else:
        context = {'message': "There are no core available at the moment."}
    return render(request, 'core.html', context)


def core_detail(request, id):
    core_detail = Core.objects.get(id=id)
    print(core_detail)
    assert isinstance(request, HttpRequest)

    context = {'core': core_detail}
    return render(request, 'core-details.html', context)