from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def get_setting(setting):
    """ Get the specified django setting, or it's default value """
    defaults = {
        # The context to use for rendering fields
        'TEMPLATE_FIELD_CONTEXT': {},
        # When this is False, don't do any TemplateField rendering
        'TEMPLATE_FIELD_RENDER': True
    }
    try:
        return getattr(settings, setting, defaults[setting])
    except KeyError:
        msg = "{0} is not specified in your settings".format(setting)
        raise ImproperlyConfigured(msg)
