from django.shortcuts import render
from django.views import generic
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponseForbidden
from django.urls import reverse
from ..models import Post
from ..forms import CommentForm

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(published='1').order_by('-updated_at')

class PostView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'
    queryset = Post.objects.filter(published='1')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

class PostCommentFormView(SingleObjectMixin, generic.FormView):
    model = Post
    form_class = CommentForm
    template_name = 'blog/detail.html'

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.post = self.object
        comment.parent = form.cleaned_data['parent']
        comment.save()
        return super().form_valid(form)     

    def get_success_url(self):
        return reverse('blog:post', kwargs={'slug': self.object.slug})

class PostWithCommentView(generic.View):

    def get(self, request, *args, **kwargs):
        view = PostView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostCommentFormView.as_view()
        return view(request, *args, **kwargs)        