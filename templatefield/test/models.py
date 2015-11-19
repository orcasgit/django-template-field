from django.db import models

from templatefield import fields, managers


class TemplatedText(models.Model):
    value = fields.TemplateTextField()

    objects_rendered = managers.RenderTemplateManager()
    objects_unrendered = models.Manager()
