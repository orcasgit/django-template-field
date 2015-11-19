from django.db import models
from django.template import Context, Template
from . import settings


class TemplateTextField(models.TextField):

    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return None

        if not context.get('show_rendered'):
            # `show_rendered` flag is unset, return the templeate
            return value

        # Return the rendered template
        template = Template(value)
        context = Context(settings.TEMPLATE_FIELD_CONTEXT)
        return template.render(context)
