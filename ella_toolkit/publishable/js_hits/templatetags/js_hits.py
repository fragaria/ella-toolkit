'''
Created on 17.10.2011

@author: xaralis
'''
import random, time

from django import template

register = template.Library()

@register.inclusion_tag('js_hits/hitcounts.html')
def js_hitcount(placement):
    return {'placement': placement, 'ts': '%s%s' % (time.time(), random.randrange(0, 10000))}
