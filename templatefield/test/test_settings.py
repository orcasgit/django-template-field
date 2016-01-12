#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_settings
-------------

Tests for `django-template-field` settings
"""
import json
import pytest
import sys

from django.core.exceptions import ImproperlyConfigured
from django.core.management import call_command
from django.test.utils import override_settings

from ..settings import get_setting
from .models import TemplatedText


pytestmark = pytest.mark.django_db


class TestSettings(object):
    def setUp(self):
        self.tmpl = "{{ template_var }} are pretty neat"
        self.model = TemplatedText(value=self.tmpl)
        self.model.save()

    @override_settings(TEMPLATE_FIELD_CONTEXT={'test_var': 'val'})
    def test_get_setting(self):
        assert get_setting('TEMPLATE_FIELD_CONTEXT') == {'test_var': 'val'}
        assert get_setting('TEMPLATE_FIELD_RENDER') == True
        pytest.raises(ImproperlyConfigured, get_setting, 'FAKE_SETTING')

    def test_render_true(self, capsys):
        self.setUp()
        call_command('dumpdata', 'test.templatedtext')
        out, _ = capsys.readouterr()
        fixture = json.loads(out)

        assert len(fixture) == 1
        assert fixture[0]['fields']['value'] == 'Dogs are pretty neat'

    def test_render_false(self, capsys):
        with override_settings(TEMPLATE_FIELD_RENDER=False):
            self.setUp()
            call_command('dumpdata', 'test.templatedtext')
            out, _ = capsys.readouterr()
            fixture = json.loads(out)
            fixture_value = fixture[0]['fields']['value']

            assert len(fixture) == 1
            assert fixture_value == '{{ template_var }} are pretty neat'
