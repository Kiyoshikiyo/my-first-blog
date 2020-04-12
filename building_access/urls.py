from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='tag-home'),
    path('about/', views.about, name='tag-about'),
]
