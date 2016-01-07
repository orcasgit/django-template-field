#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_admin
------------

Tests for `django-template-field` admin classes.
"""
import pytest

from django.contrib.admin.sites import AdminSite
from mock import MagicMock

from .models import RelatedToTemplatedText, TemplatedText
from ..admin import UnrenderedAdmin


class TestUnrenderedAdmin(object):
    def test_get_queryset(self):
        # Check the resulting context in both models
        for model in [RelatedToTemplatedText, TemplatedText]:
            admin = UnrenderedAdmin(model, AdminSite())
            qs = admin.get_queryset(MagicMock())
            assert qs.query.context == {}
