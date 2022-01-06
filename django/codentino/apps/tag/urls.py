from django.urls import path
from . import views


urlpatterns = [
    path('', views.TagListView.as_view(), name='index'),
    path('<slug:slug>/', views.TagView.as_view(), name='tag'),
]
