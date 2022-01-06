from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Tag(MPTTModel):
    slug = models.SlugField(unique=True, blank=False)
    description = models.CharField(max_length=300)
    parent = TreeForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.slug}'