from django.conf.urls import url
from recipes import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
