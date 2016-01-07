from django.db import models

from templatefield import fields, managers


class TemplatedText(models.Model):
    value = fields.TemplateTextField(null=True)

    objects_rendered = managers.RenderTemplateManager()
    objects_unrendered = models.Manager()


class RelatedToTemplatedText(models.Model):
    templated_text = models.ForeignKey(TemplatedText)
