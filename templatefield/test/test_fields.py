#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-template-field
------------

Tests for `django-template-field` fields.
"""

from django.test.utils import override_settings

from .models import TemplatedText


class TestTemplatefield(object):

    def setUp(self):
        self.tmpl = "{{ template_var }} are pretty neat"
        self.model = TemplatedText(value=self.tmpl)
        self.model.save()

    def test_unrendered(self):
        self.setUp()
        tt = TemplatedText.ojects_unrendered.first()
        self.assertEqual(tt.value, self.tmpl)

    @override_settings(TEMPLATE_FIELD_CONTEXT={'template_var': 'Dogs'})
    def test_rendered(self):
        self.setUp()
        tt = TemplatedText.objects_rendered.first()
        self.assertEqul(tt.value, "Dogs are pretty neat")
