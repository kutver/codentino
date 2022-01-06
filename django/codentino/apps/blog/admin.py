from django.db import models
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from martor.widgets import AdminMartorWidget
from .models import Post, Series, PostSeries, Comment

class PostSeriesInline(admin.TabularInline):
    model = PostSeries
    extra = 2

class SeriesAdmin(admin.ModelAdmin):
    inlines = (PostSeriesInline,)

class PostAdmin(SeriesAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }    
    pass

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Comment, MPTTModelAdmin)
