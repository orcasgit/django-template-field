from django.db import models
from django.template import Context, Template
from .settings import get_setting


class TemplateTextField(models.TextField):

    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return None

        should_render = get_setting('TEMPLATE_FIELD_RENDER')
        if not context.get('show_rendered') or not should_render:
            # `show_rendered` flag is unset, return the templeate
            return value

        # Return the rendered template
        template = Template(value)
        context_dict = {}
        context_dict.update(get_setting('TEMPLATE_FIELD_CONTEXT'))
        context_dict.update(context.get('tmpl_context', {}))
        return template.render(Context(context_dict))
