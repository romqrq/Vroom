from django.conf.urls import url, include
from .views import index_view, about_view, faqs_view, contact_view


urlpatterns = [
    url(r'^about/$', about_view, name='about'),
    url(r'^FAQs/$', faqs_view, name='faqs'),
    url(r'^contact/$', contact_view, name='contact'),
]
