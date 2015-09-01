from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^$', 'twitmap.views.home', name='home'),
    url(r'^login/$', 'twitmap.views.login', name='login'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),

]