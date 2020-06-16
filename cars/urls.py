from django.conf.urls import url, include
from .views import all_cars, custom_classic_only, luxury_only, supersport_only

urlpatterns = [
    url(r'^$', all_cars, name='cars'),
    url(r'^custom_classic/$', custom_classic_only, name='custom_classic_only'),
    url(r'^luxury/$', luxury_only, name='luxury_only'),
    url(r'^supersport/$', supersport_only, name='supersport_only'),

]
