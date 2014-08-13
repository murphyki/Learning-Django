from django.conf.urls import patterns, include, url

from myapp.views import HelloTemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^hello_simple$', 'myapp.views.hello_simple', name='home'),
    url(r'^hello_template$', 'myapp.views.hello_template', name='home'),
    url(r'^hello_template_simple$', 'myapp.views.hello_template_simple', name='home'),
    url(r'^hello_template_class$', HelloTemplateView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
