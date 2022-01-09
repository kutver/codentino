from django.views import generic
from .models import Tag

class TagListView(generic.ListView):
    model = Tag
    template_name = 'tag/index.html'
    context_object_name = 'tags'

class TagView(generic.DetailView):
    model = Tag
    template_name = 'tag/detail.html'

    def get_queryset(self):
        return Tag.objects.filter(posts__published=1).order_by('-posts__updated_at')
    