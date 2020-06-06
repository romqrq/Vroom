from django.conf.urls import url, include
from .views import index_view


urlpatterns = [
    url(r'^$', index_view, name='index'),
]
