from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('', views.index, name = 'Index'),
    path('notifications', views.notification, name='notifications'),
    path('blog', views.blog, name='blog'),
    path('health', views.health, name='health'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)