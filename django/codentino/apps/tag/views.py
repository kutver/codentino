from codentino.apps.blog.models.post import Post
from django.views import generic

from .models import Tag


class TagListView(generic.ListView):
    model = Tag
    template_name = 'tag/index.html'
    context_object_name = 'tags'

class TagView(generic.DetailView):
    model = Tag
    template_name = 'tag/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(published='1', tags=self.object).order_by('-updated_at')
        return context
