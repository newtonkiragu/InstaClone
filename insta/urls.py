from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^user/', views.profile, name='profile'),

]