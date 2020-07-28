from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('home/', views.home, name='tag-home'),
    path('about/', views.about, name='tag-about'),
    path('admin/', admin.site.urls),
    
]
