from django.conf.urls import url
from recipes import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
	url(r'^faq/$', views.faq, name='faq'),
	url(r'^recipe/(?P<recipe_name_slug>[\w\-]+)/$', views.viewrecipe, name='viewrecipe'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^suggestion/$', views.suggestion, name='suggestion'),
    url(r'^contact/$', views.contact, name='contact'),
	url(r'^trending/$', views.trending, name='trending'),
    url(r'^categories/$', views.categories, name='categories'),
    url(r'^categories/(?P<cat_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^addrecipe/$', views.addrecipe, name='addrecipe'),
	url(r'^profile/(?P<username>[\w\-]+)/$', views.userprofile, name='userprofile'),

]
