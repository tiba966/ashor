from email.message import EmailMessage
from django.shortcuts import redirect, render
from django.http import HttpResponse
from rest_framework import generics, permissions
from .serializers import WhatWeAreDoingSerializer, ThemesSerializer, ProjectSerializer, ThemeBackgroundImageSerializer
from django.http import HttpRequest
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.core.paginator import Paginator
from django.utils.translation import get_language, activate
from what_we_are_doing.models import WhatWeAreDoing, Themes, Project, ThemeBackgroundImage
from django.core.mail import send_mail,  EmailMessage
from mediapage.models import MediaDetail
from django.shortcuts import get_object_or_404, render
from .filters import ThemesDetailFilter, ProjectDetailFilter


renderer_classes = (JSONRenderer, TemplateHTMLRenderer,)
template_name = "applicantsList.html"


def translate(language):
    cur_language = get_language()
    try:
        activate(language)
    finally:
        activate(cur_language)


def what_we_are_doing(request):
    """Renders the create what_we_are_doing page."""
    assert isinstance(request, HttpRequest)
    queryset = WhatWeAreDoing.objects.all()
    serializer_class = WhatWeAreDoingSerializer(queryset, many=True)
    media = MediaDetail.objects.all()

    # Show many contacts per page for stories
    paginator_media = Paginator(media, 10000000000000000)
    page_number_media = request.GET.get('page')
    page_obj_media = paginator_media.get_page(page_number_media)

    return render(request, 'what-we-are-doing.html',
                  {
                      'data': serializer_class.data,
        'media' : page_obj_media
                  }
                  )

# def themes(request):
#     """Renders the create themes page."""
#     themes = Themes.objects.all()

#     # filters
#     myfilter = ThemesDetailFilter(request.GET, queryset=themes)
     
#     context = {
#         'themes': themes,
#         'myfilter': myfilter,
#     }  # template name

#     return render(request, 'themes.html', context)


from django.shortcuts import render

def themes(request):
    """Renders the create themes page."""
    themes = Themes.objects.all()
    themes_bg = ThemeBackgroundImage.objects.all()
    # filters
    myfilter = ThemesDetailFilter(request.GET, queryset=themes)
    media = MediaDetail.objects.all()

    # Show many contacts per page for stories
    paginator_media = Paginator(media, 10000000000000000)
    page_number_media = request.GET.get('page')
    page_obj_media = paginator_media.get_page(page_number_media)

    context = {
        'themes': themes,
        'myfilter': myfilter,
        'themes_bg': themes_bg,
        'media' : page_obj_media
    }  # template name

    return render(request, 'themes.html', context)


# def themes_details(request, id):
#     """Renders the create themes page."""
 
#     themes = Themes.objects.get(id=id)

#     context = {'item': themes}
#     return render(request, 'themes-details.html', context)

def theme_detail(request, theme_id):
    theme = get_object_or_404(Themes, pk=theme_id)
    context = {'theme': theme}
    return render(request, 'themes-details.html', context)

def project(request):
    """Renders the create what_we_are_doing page."""
    assert isinstance(request, HttpRequest)
 
    order = request.GET.get("order", None)
    if order == "popularity":
        project = Project.objects.order_by("-views")
    elif order == "latest":
        project = Project.objects.all().order_by("-date")
    else:
        project = Project.objects.all()
    serializer_class = ProjectDetailFilter(request.GET, queryset=project).qs

    media = MediaDetail.objects.all()

    # Show many contacts per page for stories
    paginator_media = Paginator(media, 10000000000000000)
    page_number_media = request.GET.get('page')
    page_obj_media = paginator_media.get_page(page_number_media)

    return render(request, 'projects.html',
        {
            'data': serializer_class,
        'media' : page_obj_media
        }
        )
