# -*- coding: utf-8; -*-
#
# This file is part of Superdesk.
#
# Copyright 2013, 2014, 2015 Sourcefabric z.u. and contributors.
#
# For the full copyright and license information, please see the
# AUTHORS and LICENSE files distributed with this source code, or
# at https://www.sourcefabric.org/superdesk/license

from superdesk.tests import TestCase
from unittest import mock


class SuperdeskValidatorTest(TestCase):
    """Base class for the SuperdeskValidator class tests."""

    def _get_target_class(self):
        """Return the class under test.

        Make the test fail immediately if the class cannot be imported.
        """
        try:
            from superdesk.validator import SuperdeskValidator
        except ImportError:
            self.fail("Could not import class under test (SuperdeskValidator)")
        else:
            return SuperdeskValidator


@mock.patch('superdesk.validator.superdesk')
class ValidateIuniqueMethodTestCase(SuperdeskValidatorTest):
    """Tests for the _validate_iunique() method."""

    def setUp(self):
        super().setUp()
        klass = self._get_target_class()
        self.validator = klass(schema={})

    def test_does_not_raise_error_on_inputs_containing_special_regex_chars(
        self, fake_superdesk
    ):
        field = 'field_name'
        value = 'foo(bar++^$$^'  # an invalid regex pattern

        try:
            self.validator._validate_iunique(True, field, value)
        except Exception as ex:
            self.fail("Error unexpectedly raised: {}".format(ex))


@mock.patch('superdesk.validator.superdesk')
class ValidateIuniquePerParentMethodTestCase(SuperdeskValidatorTest):
    """Tests for the _validate_iunique_per_parent() method."""

    def setUp(self):
        super().setUp()
        klass = self._get_target_class()
        self.validator = klass(schema={})
        self.validator.document = {}

    def test_does_not_raise_error_on_inputs_containing_special_regex_chars(
        self, fake_superdesk
    ):
        parent_field = 'parent_field_name'
        field = 'field_name'
        value = 'foo(bar++^$$^'  # an invalid regex pattern

        try:
            self.validator._validate_iunique_per_parent(
                parent_field, field, value)
        except Exception as ex:
            self.fail("Error unexpectedly raised: {}".format(ex))