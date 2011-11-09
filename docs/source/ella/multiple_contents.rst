.. _multiple_contents:


=========================
Multiple article contents
=========================

There are situations when you want to have one Article content split to several
pages. Reasons for this are mostly **pageviews**.

``ella_toolkit.articles.multiple_contents`` solves this issue by using special mark
in the place you want your page splitted.

Usage
======

First, add ``ella_toolkit.articles.multiple_contents`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'ella.core',
        'ella.articles',
        ...
        'ella_toolkit.articles.multiple_contents',
        ...
    )
    
It is important that ``ella_toolkit.articles.multiple_contents`` is listed **after**
the ``ella.articles``.

Second, include the app in your URL patterns::

    patterns = urlpatterns('',
        ...
        url('^', include('ella_toolkit.articles.multiple_contents.urls'),
        ...
    )

After this, we are almost ready, we just need to alter our templates.

Page split mark
===============

When you want to split your page into several pages, you have to put
a split mark on that place. The split mark is defined as::

    <!--PB-->


New template context
====================

``ella_toolkit.articles.multiple_contents`` adds a lot of additional context to your
templates.

``content``
    Current content to show.
    
``content_list``
    List of all contents available for article.
    
``content_count``
    Total number of all contents.
    
``next_content_index``
    1-based index of next content, None if this is the last content or no
    content is available.

``prev_content_index``
    1-based index of previous content, None if this is the first content or no
    content is available.
    
``has_next_content``
    True if there is another content, False otherwise.
    
``has_prev_content``
    True if there is previous content, False otherwise.
    
``has_some_content``
    True if there is some content available, False otherwise.
    
New article model methods
=========================

This app also adds three new ``Article`` model methods. The extension of ``Article``
is done by a little bit of Python magic, so be sure to list ``multiple_contents``
**after** ``ella.articles`` in ``INSTALLED_APPS``.

.. autofunction:: ella_toolkit.articles.multiple_contents.models.get_contents

.. autofunction:: ella_toolkit.articles.multiple_contents.models.get_content_count

.. autofunction:: ella_toolkit.articles.multiple_contents.models.get_content

Template example
================

One simple example of usage in template is offered here::

    {% block main_content %}
        {% comment %}IF PRINT IS REQUESTED, RENDER EVERYTHING{% endcomment %}
        {% ifequal request.GET.print "1" %}
            {% for con in content_list %}{% render con %}{% endfor %}
        {% else %}
            {% render content %}
        {% endifequal %}
        
        {% ifnotequal request.GET.print "1" %}
            {% ifnotequal content_count 1 %}
                <div class="pagination">      
                 <p>
                {% for p in content_list %}
                    <a href="{% ifequal forloop.counter 1 %}{{ object.get_absolute_url }}{% else %}{% custom_url object article_page forloop.counter %}{% endifequal %}" title="Strana {{ forloop.counter }}" {% ifequal p content %}class="active"{% endifequal %}>{{ forloop.counter }}</a>
                {% endfor %}
                </p>
                
                {% if has_prev_content %}
                    <div class='strankovaniLeft'>
                        <a href="{% ifequal prev_content_index 1 %}{{ object.get_absolute_url }}{% else %}{% custom_url object article_page prev_content_index %}{% endifequal %}">předchozí &laquo;</a>
                    </div>
                {% endif %}
                
                {% if has_next_content %}
                  <div class='strankovaniRight'>
                      <a href="{% ifequal next_content_index 1 %}{{ object.get_absolute_url }}{% else %}{% custom_url object article_page next_content_index %}{% endifequal %}">&raquo; další</a>
                  </div>
                {% endif %}
                </div>
            {% endifnotequal %}
        {% endifnotequal %}
    {% endblock %}
    
Note use of ``{% custom_url %}`` templatetag from ella artillery. ``ella_toolkit.articles.multiple_contents`` adds a **custom URL** called **article_page**.
