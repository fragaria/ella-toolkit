'''
Created on 17.10.2011

@author: xaralis
'''
import random
import time

from django import template

register = template.Library()


@register.inclusion_tag('js_hits/hitcounts.html')
def js_hitcount(publishable):
    return {'publishable': publishable,
            'ts': '%s%s' % (time.time(), random.randrange(0, 10000))}
