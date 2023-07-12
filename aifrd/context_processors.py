from mediapage.models import Category
from what_we_are_doing.models import Category as ProjectCategory
def index(request):
    return {
        'categories': Category.objects.all(),
                'project_categories': ProjectCategory.objects.all(),

        }
