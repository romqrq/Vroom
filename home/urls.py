from django.conf.urls import url, include
from .views import index_view, about_view


urlpatterns = [
    url(r'^$', index_view, name='index'),
    url(r'^about/$', about_view, name='about_page'),
]
