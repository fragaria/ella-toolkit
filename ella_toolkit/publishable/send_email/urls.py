from django.conf.urls.defaults import url, patterns
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

from ella.core.custom_urls import resolver

urlpatterns = patterns('ella_toolkit.publishable.send_email.views',
    # send information about article to e-mail
    url(r'^%s/$' % slugify(_('send by email')), 'send_by_email', name='send_by_email'),
    url(r'^%s/%s/$' % (slugify(_('send by email')), slugify(_('done'))), 'send_by_email_success', name='send_by_email_success'),
)

resolver.register(urlpatterns)
