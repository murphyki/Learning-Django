from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'myapp.views.hello_template', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
