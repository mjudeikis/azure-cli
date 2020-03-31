# Copyright (c) Microsoft Corporation.
# Licensed under the Apache License 2.0.

import os
import unittest
import mock

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import ResourceGroupPreparer
from azure.cli.testsdk import ScenarioTest
from azure.cli.core.mock import DummyCli

TEST_SUBSCRIPTION = 'af848f0a-dbe3-449f-9ccd-6f23ac6ef9f1'

class AroMockCommandsTests(unittest.TestCase):

    @mock.patch('azure.cli.core.commands.client_factory.get_subscription_id', autospec=True)
    def test_get_subscription_id(self, mock_cli_ctx):
        mock_cli_ctx = self._setup_cmd()
        mock_cli_ctx.data['subscription_id'] = TEST_SUBSCRIPTION
        return mock_cli_ctx.data['subscription_id']


    def _setup_cmd(self):
        cmd = mock.MagicMock()
        cmd.cli_ctx = DummyCli()
        mock_sku = mock.MagicMock()
        mock_sku.classic.value = 'Classic'
        mock_sku.basic.value = 'Basic'
        mock_sku.standard.value = 'Standard'
        mock_sku.premium.value = 'Premium'
        cmd.get_models.return_value = mock_sku
        return cmd
