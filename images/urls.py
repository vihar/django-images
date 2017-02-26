from django.conf.urls import url
from django.conf.urls.static import static

from .views import post_list
from django.conf import settings
urlpatterns = [
    url(r'^$', post_list, name='list'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
