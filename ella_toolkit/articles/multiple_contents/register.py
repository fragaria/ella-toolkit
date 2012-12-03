from django.conf import settings

__author__ = 'xaralis'


try:
    from ella_newman.widget_extensions import rich_text_extensions

    rich_text_extensions.register(
        settings.STATIC_URL + 'multiple_contents/markdown_pagebreak.js',
        type='js'
    )
    rich_text_extensions.register(
        settings.STATIC_URL + 'multiple_contents/markdown_pagebreak.css',
        type='css'
    )
except ImportError:
    pass
