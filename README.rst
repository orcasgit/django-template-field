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

        # Manger that returns rendered templates.
        objects_rendered = managers.RenderTemplateManager()
        # Django's default manager returns unrendered templates.
        objects_unrendered = models.Manager()

Extra context can be added in `settings` like so:

    TEMPLATE_FIELD_CONTEXT = { 'template_var': value }


Running Tests
--------------


    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements-test.txt
    (myenv) $ python runtests.py

