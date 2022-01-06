from django.contrib import admin
from .models import Tag
from mptt.admin import MPTTModelAdmin

# Register your models here.
admin.site.register(Tag, MPTTModelAdmin)