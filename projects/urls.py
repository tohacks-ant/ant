"""ant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls.py/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls.py import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls.py'))
"""
from django.urls import path, re_path
from .views import project_detail, project_list, index

urlpatterns = [
    path('', index, name='index'),
    re_path(r'^project/$', project_list, name='project_list'),
    re_path(r'^project/detail(?P<id>\d+)/$', project_detail, name='project_detail'),
]
