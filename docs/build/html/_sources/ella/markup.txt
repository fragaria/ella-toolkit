.. _markup:

==================================
Utilities for markup customization
==================================

Specifing filters to run on save of markup content
==================================================

You can replace usage of filter in rendering part of your page by pre-filtering
the content after the field has been saved by using our :py:class:`MarkupFilterPostProcessor`. 
This can save some performance because the filtering is done only once.

.. py:class:: MarkupFilterPostProcessor

To use it, you must do the following:

    #. Create a database record in ``djangomarkup_textprocessor`` table like this::
    
        INSERT INTO `djangomarkup_textprocessor` (`function`, `name`, `processor_options`) VALUES ('ella_toolkit.markup.filterpostprocessor.post_processor', 'post_processor', '');

    #. In your Django settings, be sure to list ``DEFAULT_MARKUP = 'post_processor'``.
    #. List all filter classes you want to run on save, e.g.::
    
        MARKUP_FILTER_CLASSES = (
            'myapp.templatetags.filter1',
            'myapp.templatetags.filter2',
        )
        
       Ordering is important, filters are applied in the order they are listed.
       
Optionally, you can select which **TextProcessor** class is used as base (by
default it is markdown) by setting the ``MARKUP_FILTER_POST_PROCESSOR_BASE = 'textile/../..'``.
