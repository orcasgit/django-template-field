=============================
django-template-field
=============================

.. image:: https://badge.fury.io/py/django-template-field.png
    :target: https://badge.fury.io/py/django-template-field

.. image:: https://travis-ci.org/orcasgit/django-template-field.png?branch=master
    :target: https://travis-ci.org/orcasgit/django-template-field

A Django template field with a manager to return the rendered template.

Documentation
-------------

The full documentation is at https://django-template-field.readthedocs.org.

Quickstart
----------

Install django-template-field::

    pip install django-template-field

Then use it in a project::

    from django.db import models

    from templatefield import fields, managers


    class TemplatedText(models.Model):
        value = fields.TemplateTextField()

        # Manager that returns rendered templates. This will be the default
        # manager since it is first. Now, when accessed via `Related Models`_
        # this field will also be rendered.
        objects_rendered = managers.RenderTemplateManager()
        # Django's default manager returns unrendered templates.
        objects_unrendered = models.Manager()

Extra context can be added in `settings` like so:

    TEMPLATE_FIELD_CONTEXT = { 'template_var': value }

Context can also be added to querysets like so:

    TemplatedText.objects_rendered.with_context({'template_var2': value2})


Related Models
--------------

If a ``TemplateTextField`` will be accessed from another model through a
``ForeignKey`` relationship, Django will use the default manager to render the
``TemplateTextField``. For example, if we define this additional model:

    class RelatedToTemplatedText(models.Model):
        templated_text = models.ForeignKey(TemplatedText)

We can expect to see fields accessed via ``templated_text`` rendered properly.

Admin
-----

Using ``RenderTemplateManager`` as the default has the unfortunate side effect
of rendering your fields in the Django admin, so we have provided a class from
which you can inherit to solve that problem. Ex:

    from templatefield import admin

    class TemplatedTextAdmin(admin.UnrenderedAdmin):
        ...

Running Tests
--------------


    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements/test.txt
    (myenv) $ python runtests.py
