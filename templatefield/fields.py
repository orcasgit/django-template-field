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
        context_dict = {}
        context_dict.update(settings.TEMPLATE_FIELD_CONTEXT)
        context_dict.update(context.get('tmpl_context', {}))
        return template.render(Context(context_dict))
