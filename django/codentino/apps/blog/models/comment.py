from django.db import models
from codentino import settings
from mptt.models import MPTTModel, TreeForeignKey

class Comment(MPTTModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, blank=False)
    published_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    parent = TreeForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1_000, blank=False)

    class MPTTMeta:
        order_insertion_by = ['published_at']

    def __str__(self) -> str:
        return f'Comment by {self.author} to {self.post}'
