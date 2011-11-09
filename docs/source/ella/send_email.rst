.. _send_email:

============================
Send email about Publishable
============================

This package offers nicely wrapped custom send email action over Publishable
models. Installation is very easy.

How to install
==============

Simply add ``ella_toolkit.publishable.send_email`` to your ``INSTALLED_APPS`` and make
sure that ``ella_toolkit.publishable.send_email.urls`` is loaded. You can enforce it your ``urls.py` in 
the following fashion::

    from ella.utils.installedapps import call_modules
    call_modules(auto_discover=('urls',))
    
That's really everything you need to do to run the custom application.

Template customization
======================

You would probably want to use a customized template for showing the form or the email. It's
easy to do, just override the template by creating it in these locations:

    * ``/templates/send_email/email.html``
    * ``/templates/send_email/form.html``
