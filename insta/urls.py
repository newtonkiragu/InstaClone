from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^newprofile/(?P<profile_id>\d+)/$',views.profile,name = 'profile'),
    url(r'^showprofile/(\d+)',views.display_profile,name = 'showprofile'),
    url(r'^image/$', views.add_image, name='upload_image'),


]