from django.conf.urls import url, include
from . import urls_reset
from .views import register, profile, visit_profile, logout, login, edit_user_view, del_user

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^edit_profile/(?P<user_id>\d+)', edit_user_view, name='edit_user'),
    url(r'^delete_user/(?P<user_id>\d+)', del_user, name='delete_user'),
    url(r'^visit_profile/(?P<user_id>\d+)', visit_profile,
        name='visit_profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password_reset/', include(urls_reset)),
]
