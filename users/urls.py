from django.urls import re_path, path
from .views import org_register, stu_register, org_login, stu_login, logout, \
    edit_info_stu, edit_profile_stu, edit_info_org, edit_profile_org, \
    get_project_list, dashboard

app_name="users"

urlpatterns = [
    path('', dashboard, name='register_org'),
    re_path(r'^register_org/$', org_register, name='register_org'),
    re_path(r'^register_stu/$', stu_register, name='register_stu'),
    re_path(r'^login_org/$', org_login, name='login_org'),
    re_path(r'^login_stu/$', stu_login, name='login_stu'),
    re_path(r'^logout/$', logout, name='logout'),
    re_path(r'^edit_info_stu/(?P<id>\d+)/$', edit_info_stu, name='edit_info_stu'),
    re_path(r'^edit_profile_stu/(?P<id>\d+)/$', edit_profile_stu, name='edit_profile_stu'),
    re_path(r'^edit_info_org/(?P<id>\d+)/$', edit_info_org, name='edit_info_org'),
    re_path(r'^edit_profile_org/(?P<id>\d+)/$', edit_profile_org, name='edit_profile_org'),
    # re_path(r'^profile_list/$', profile_list, name='profile_list'),
    re_path(r'^project_list/$', get_project_list, name='project_list'),
]
