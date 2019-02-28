from django.conf.urls import url
from recipes import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^suggestion/$', views.suggestion, name='suggestion'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^addrecipe/$', views.addrecipe, name='addrecipe'),
]
