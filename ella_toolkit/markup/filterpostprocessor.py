from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module
from django.utils.encoding import smart_str

from djangomarkup import processors

MARKUP_FILTER_POST_PROCESSOR_BASE = getattr(settings, 'MARKUP_FILTER_POST_PROCESSOR_BASE', 'markdown')
MARKUP_FILTER_CLASSES = ()

class MarkupFilterPostProcessor(object):
    def __init__(self):
        self.processor = getattr(processors, MARKUP_FILTER_POST_PROCESSOR_BASE)
        
    def __call__(self, src, **kwargs):
        ret = self.processor(src, **kwargs)
        
        for import_path in settings.MARKUP_FILTER_CLASSES:
            module, attr = import_path.rsplit('.', 1)
            try:
                mod = import_module(module)
            except ImportError, e:
                raise ImproperlyConfigured('Error importing module %s: "%s"' %
                                           (module, e))
            try:
                f = getattr(mod, attr)
            except AttributeError:
                raise ImproperlyConfigured('Module "%s" does not define a "%s" '
                                           'class.' % (module, attr))
                 
            ret = f(smart_str(ret))
        return ret

post_processor = MarkupFilterPostProcessor()
