from django.conf.urls import include, url
from django.contrib import admin
from accounts import views as acc_views

# urlpatterns = [
    # Examples:
    # url(r'^$', 'su_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
#     url(r'^$','views.home',name='home'),
#     url(r'^admin/', include(admin.site.urls)),
# ]


urlpatterns = [
        url(r'^$',acc_views.home_view,name='home_view'),
        url(r'^admin/',include(admin.site.urls)),
        url(r'^accounts/', include('accounts.urls', namespace='accounts')),
]
