from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<slug:slug>/', views.PostWithCommentView.as_view(), name='post'),
]
