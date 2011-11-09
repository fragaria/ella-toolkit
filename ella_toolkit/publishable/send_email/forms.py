from django import forms
from django.utils.translation import ugettext_lazy as _

class SendMailForm(forms.Form):
	recipient = forms.EmailField(label=_('Recipient'), required=True)
	sender = forms.EmailField(label=_('Sender'), required=True)
	message = forms.CharField(required=False, max_length=255, widget=forms.Textarea, label=_('Your message'))
