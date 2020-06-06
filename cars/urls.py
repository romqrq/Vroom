from django.conf.urls import url, include
from .views import all_cars

urlpatterns = [
    url(r'^$', all_cars, name='cars')
]
