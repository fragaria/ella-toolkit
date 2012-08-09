'''
Created on 17.10.2011

@author: xaralis
'''
from django.http import HttpResponse

from ella.core.cache.utils import get_cached_object_or_404
from ella.core.models.publishable import Publishable

from ella_hits.models import HitCount


def record_hit(request, publishable_id):
    p = get_cached_object_or_404(Publishable, pk=publishable_id)
    HitCount.objects.hit(p)
    return HttpResponse(status=204)
