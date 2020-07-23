from django.conf.urls import url
from .views import all_cars, custom_classic_only, luxury_only, supersport_only, car_register, car_detail, edit_car, del_car, add_ons

urlpatterns = [
    url(r'^$', all_cars, name='all_cars'),
    url(r'^custom_classic/$', custom_classic_only, name='custom_classic_only'),
    url(r'^luxury/$', luxury_only, name='luxury_only'),
    url(r'^supersport/$', supersport_only, name='supersport_only'),
    url(r'^rent_my_car/$', car_register, name='car_register'),
    url(r'^car_details/(?P<car_id>\d+)', car_detail, name='car_detail'),
    url(r'^edit_car/(?P<car_id>\d+)', edit_car, name='edit_car'),
    url(r'^delete_car/(?P<car_id>\d+)', del_car, name='delete_car'),
    url(r'^add_ons/(?P<item_type>[\w-]+)/', add_ons, name='add_ons'),
]
