from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import *
from django.contrib import admin
import dbindexer

from arescaler.views import *

handler500 = 'djangotoolbox.errorviews.server_error'

# django admin
admin.autodiscover()

# search for dbindexes.py in all INSTALLED_APPS and load them
dbindexer.autodiscover()

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}),
    ('^admin/', include(admin.site.urls)),
    ('^main/', 'arescaler.views.main'),
    ('^do_rescale/', 'arescaler.views.do_rescale'),
    ('^rescale/', RescaleView.as_view()),
)

urlpatterns += staticfiles_urlpatterns()
