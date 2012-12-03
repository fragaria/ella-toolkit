function handle_pagebreak(evt, toolbar) {
    toolbar.selection_handler.replace_selection("\n<!--PB-->\n");
    toolbar.trigger_delayed_preview();
}

toolbarButtonRegister.addButton(gettext('Page break'), 'pagebreak', handle_pagebreak);
