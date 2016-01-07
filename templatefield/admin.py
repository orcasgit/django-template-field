from django.contrib import admin


class UnrenderedAdmin(admin.ModelAdmin):
    """ Make sure template fields aren't rendered in the Django admin. """

    def get_queryset(self, request):
        """ Remove ``show_rendered`` from the context, if it's there. """
        qs = super(UnrenderedAdmin, self).get_queryset(request)
        if 'show_rendered' in qs.query.context:
            del qs.query.context['show_rendered']
        return qs
