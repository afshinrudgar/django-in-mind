from django.conf.urls import url

from . import views

urlpatterns = [
  # home page (index)
  url(r'^$', views.home, name='home'),
  # place/uri
  url(r'^place/(?P<uri>[\w\-]+)/$', views.place, name='place'),
  # user/username
  url(r'^user/(?P<username>[\w\.\_\-]+)/$', views.user, name='user')
]