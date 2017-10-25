from django.conf.urls import url

from member.views import member_profile

urlpatterns = [
    url(r'^profile/(?P<member_pk>\d+)/$', member_profile,  name='member_profile'),
]