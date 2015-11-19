from django.db import models


class RenderTemplateManager(models.Manager):
    def get_queryset(self):
        qs = super(RenderTemplateManager, self).get_queryset()
        qs.query.add_context('show_rendered', True)
        return qs
