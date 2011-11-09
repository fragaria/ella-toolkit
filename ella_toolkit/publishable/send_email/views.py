from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.views.generic.simple import direct_to_template

from ella.core.custom_urls import resolver

from forms import SendMailForm
from signals import publishable_email_sent

def send_by_email(request, object_info):
    context = {}
    object = object_info['object']

    if request.method == 'POST':
        form = SendMailForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            subject = u'%s %s' % (settings.EMAIL_SUBJECT_PREFIX, _('link to `%s`') % unicode(object))
            message = render_to_string('send_email/email.html', {
                'sender': cd['sender'], 'message': cd['message'],
                'site': Site.objects.get_current(), 'url': request.build_absolute_uri(object.get_absolute_url())
            })
            recipients = (form.cleaned_data['recipient'],)
            send_mail(subject, message, settings.SERVER_EMAIL, recipients,
                fail_silently=False)
            publishable_email_sent.send(sender=object, subject=subject,
                message=message, recipients=recipients)
            return HttpResponseRedirect(resolver.reverse(object, 'send_by_email_success'))
    else:
        form = SendMailForm()

    context['form'] = form
    context.update(object_info)

    return render_to_response('send_email/form.html', context,
        context_instance=RequestContext(request))

def send_by_email_success(request, object_info):
    ctx = object_info
    ctx.update({'sent': True})
    return direct_to_template(request, template='send_email/form.html',
        extra_context=ctx)
