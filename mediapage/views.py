from django.shortcuts import render
from django.db.models import F

from .models import MediaDetail, MediaBackgroundImage
from .serializers import MediaDetailSerializer, MediaBackgroundImageSerializer
from django.http import HttpRequest
from .filters import MediaDetailFilter
# from .form import StoryDetailForm
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

def media_filter(request):

    order = request.GET.get("order", None)
    if order == "popularity":
        media = MediaDetail.objects.order_by("-views")
    elif order == "latest":
        media = MediaDetail.objects.all().order_by("-date")
    else:
        media = MediaDetail.objects.all()
        
    media = MediaDetailFilter(request.GET, queryset=media).qs
  
    

    if media:
        context = {
            "media": media,
        }  # template name

    else:
        context = {"message": "There are no media available at the moment."}
    return render(request, "media_filter.html", context)

def media_list(request):

    media = MediaDetail.objects.all().order_by("-date")
    myfilter = MediaDetailFilter(request.GET, queryset=media)
    media = myfilter.qs
    media_bg = MediaBackgroundImage.objects.all()

    # Show many contacts per page.
    paginator = Paginator(media, 100000000000000000000)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    print("hello")

    if media:
        context = {
            "media": page_obj,
            "myfilter": myfilter,
            'media_bg':media_bg
        }  # template name

    else:
        context = {"message": "There are no media available at the moment."}
    return render(request, "media.html", context)


def media_detail(request, id):
    media = get_object_or_404(MediaDetail, pk=id)

    media = MediaDetail.objects.filter(id=id).last()
    media.views = F("views") + 1
    media.save()
    media.refresh_from_db()
    medias = MediaDetail.objects.all()

    # Show many contacts per page for stories
    paginator_media = Paginator(medias, 10000000000000000)
    page_number_media = request.GET.get('page')
    page_obj_media = paginator_media.get_page(page_number_media)

    context = {"media": media,  'num_visits': media.views, 'medias': page_obj_media}
    return render(request, "media-details.html", context)



def clear(request):
    return HttpResponse("")



