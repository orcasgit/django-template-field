from django.conf import settings


TEMPLATE_FIELD_CONTEXT = getattr(settings, 'TEMPLATE_FIELD_CONTEXT', {})
