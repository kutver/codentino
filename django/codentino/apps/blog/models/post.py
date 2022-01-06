from django.db import models
from codentino import settings
from martor.models import MartorField

class Post(models.Model):
    
    PUBLISHED_STATUS = (
        (1, 'Published'),
        (0, 'Draft')
    )

    title = models.CharField(max_length=100, blank=False)
    slug = models.SlugField(max_length=100, unique=True, blank=False)
    description = models.CharField(max_length=300, blank=False)
    post = MartorField()
    tags = models.ManyToManyField("tag.Tag", related_name="posts")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, blank=False)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    published = models.PositiveSmallIntegerField(choices=PUBLISHED_STATUS)

    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):
        # TODO: At this point of developement no urls determined for posts yet.
        # This function is required for Django's sitemap framework to function,
        # However, after determining the urls and views, it's better to update
        # below code.
        return f"/blog/{self.slug}/"
