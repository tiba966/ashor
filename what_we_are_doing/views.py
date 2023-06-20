from email.message import EmailMessage
from django.shortcuts import redirect, render
from django.http import HttpResponse
from rest_framework import generics, permissions
from .serializers import WhatWeAreDoingSerializer, ThemesSerializer
from django.http import HttpRequest
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.core.paginator import Paginator
from django.utils.translation import get_language, activate
from what_we_are_doing.models import WhatWeAreDoing, Themes
from django.core.mail import send_mail,  EmailMessage

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

def themes(request):
    """Renders the create themes page."""
    themes = Themes.objects.all()

    # filters
    myfilter = ThemesDetailFilter(request.GET, queryset=themes)
    themes = myfilter.qs
     
    # Show many contacts per page.
    paginator = Paginator(themes, 10000000000000000)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if themes:
        context = {'themes': page_obj,
                   'myfilter': myfilter,
                   }  # template name

    else:
        context = {'message': "There are no themes available at the moment."}
    return render(request, 'themes.html', context)


def themes_details(request, id):
    """Renders the create themes page."""
 
    themes = Themes.objects.get(id=id)
    print(themes)
    assert isinstance(request, HttpRequest)

    context = {'themes': themes}
    return render(request, 'themes-details.html', context)
