"""django_test URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from dashboard import views as dashboard_views
from users import views as users_views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^login/', auth_views.login, name='login'),
    url(r'^logout/$', users_views.logout, name='logout'),
    url(r'^signup/', users_views.signup, name='signup'),
    url(r'^dashboard/', dashboard_views.IndexView.as_view(), name='dashboard'),
    url(r'^form/', dashboard_views.MyFormView.as_view(), name='form'),
    url(r'^list/$', dashboard_views.Patient_list.as_view(), name='list'),
]
