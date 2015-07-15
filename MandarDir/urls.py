"""MandarDir URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from mandardb import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    #create a address
    url(r'^address/$', views.AddressCreate.as_view()),

    url(r'^address/all/$', views.AddressGet.as_view()),

    url(r'^address/(?P<address_id>[0-9]+)$', views.AddressCreate.as_view()),

    url(r'^person/$', views.PersonCreate.as_view()),

    url(r'^person/(?P<person_id>[0-9]+)$', views.PersonCreate.as_view()),

    url(r'^person/all/$', views.PersonGet.as_view()),

    url(r'^feed/$', views.FeedCreate.as_view()),

    url(r'^feed/(?P<feed_id>[0-9]+)$', views.FeedCreate.as_view()),

    url(r'^feed/all/$', views.FeedGet.as_view()),

    url(r'^image/$', views.ImageUpload.as_view()),

    url(r'^image/(?P<image_id>[0-9]+)$', views.ImageUpload.as_view()),

]
