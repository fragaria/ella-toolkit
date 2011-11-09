'''
Created on 17.10.2011

@author: xaralis
'''
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('ella_toolkit.publishable.js_hits.views',
    url('^hit/(?P<placement_id>\d+)/$', 'record_hit', name='js_hits_record'),
)
