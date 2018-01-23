from django.conf.urls import url
from . import views

urlpatterns=[
    url('^home$/',views.welcome,name = 'welcome'),
    url(r'^$',views.all_images,name='allImages')
]
