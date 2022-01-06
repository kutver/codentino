from django.db import models

class Series(models.Model):
    title = models.CharField(max_length=100, blank=False)
    slug = models.SlugField(max_length=100, unique=True, blank=False)
    posts = models.ManyToManyField('blog.Post', through='PostSeries', related_name='series_posts')
    tags = models.ManyToManyField("tag.Tag", related_name="series_tags")

    def __str__(self) -> str:
        return self.title

class PostSeries(models.Model):
    series = models.ForeignKey('blog.Series', on_delete=models.CASCADE)
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField(blank=False)

    class Meta:
        ordering = ('order',)
    
    def __str__(self) -> str:
        return f'{self.series} / {self.order}. {self.post}'
