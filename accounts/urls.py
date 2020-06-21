from django.conf.urls import url, include
from . import urls_reset
from .views import register, profile, visit_profile, logout, login

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'visit_profile/(?P<userid>\d+)', visit_profile, name='visit_profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(urls_reset)),
]
