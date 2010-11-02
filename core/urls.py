from django.conf.urls.defaults import *

urlpatterns = patterns('core.views',
    (r'^$', 'list_conferences'),
    (r'^new', 'new_conference'),
)
