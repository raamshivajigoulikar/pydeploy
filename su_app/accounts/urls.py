from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.contrib.auth.views import (
                                 login,
                                 logout,
                                 password_reset,
                                 password_reset_done,
                                 )
#Define accounts.urls
urlpatterns = [
        url(r'^login/$', login, {'template_name': 'accounts/login.html'},
                                                            name='login'),
        url(r'^profile/$',views.profile,name='profile'),
        url(r'^logout/$',logout, {'template_name': 'accounts/logout.html'},
                                                            name='logout'),
        url(r'^register/$',views.register,name='register'),
        url(r'^profile/edit/$',views.profile_edit,name='profile_edit'),
        url(r'^change-password/$',views.change_password,name='change_password'),
        url(r'^reset-password/$',password_reset,name='PasswordResetView.as_view()'),
        url(r'^reset-password/done/$',password_reset_done,name='PasswordResetDoneView.as_view()'),
         ]


# url(r'^password_reset/$',password_reset,
#      {
#       'template_name': 'accounts/passwordreset/password_reset_form.html',
#       'email_template_name': 'accounts/passwordreset/password_reset_email.html',
#       'subject_template_name': 'accounts/passwordreset/password_reset_subject.txt',
#       'post_reset_redirect': 'accounts:password_reset_done'
#      },
#   name='password_reset'),
#
#     url(r'^password_reset_done/$',password_reset_done,
#      { 'template_name': 'accounts/passwordreset/password_reset_done.html'},
#      name='password_reset_done'),
