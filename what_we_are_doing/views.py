from email.message import EmailMessage
from django.shortcuts import redirect, render
from django.http import HttpResponse
from rest_framework import generics, permissions
from .serializers import WhatWeAreDoingSerializer, ThemesSerializer, ProjectSerializer
from django.http import HttpRequest
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.core.paginator import Paginator
from django.utils.translation import get_language, activate
from what_we_are_doing.models import WhatWeAreDoing, Themes, Project
from django.core.mail import send_mail,  EmailMessage
from django.shortcuts import get_object_or_404, render

from .filters import ThemesDetailFilter


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

    return render(request, 'what-we-are-doing.html',
                  {
                      'data': serializer_class.data,
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

    # filters
    myfilter = ThemesDetailFilter(request.GET, queryset=themes)
     
    context = {
        'themes': themes,
        'myfilter': myfilter,
    }
    
    # Render index.html
    index_html = render(request, 'index.html', context)
    
    # Render themes.html
    themes_html = render(request, 'themes.html', context)

    # Return both HTML pages
    return index_html, themes_html


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
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer(queryset, many=True)

    return render(request, 'projects.html',
        {
            'data': serializer_class.data,
        }
        )
