'''
Created on 17.10.2011

@author: xaralis
'''
from django.http import HttpResponse
from ella.core.cache.utils import get_cached_object_or_404
from ella.core.models.publishable import Placement, HitCount

def record_hit(request, placement_id):
    p = get_cached_object_or_404(Placement, pk=placement_id)
    HitCount.objects.hit(p)
    return HttpResponse(status=204)