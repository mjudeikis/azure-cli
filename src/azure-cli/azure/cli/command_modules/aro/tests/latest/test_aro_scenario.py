# Copyright (c) Microsoft Corporation.
# Licensed under the Apache License 2.0.

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import ResourceGroupPreparer
from azure.cli.testsdk import ScenarioTest


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))

class AroScenarioTest(ScenarioTest):
    @ResourceGroupPreparer(name_prefix='cli_test_aro')
    def test_aro_scenarios(self, resource_group):
        self.kwargs.update({
            'name': 'test1',
            'mastersubnet': '/subscriptions/af848f0a-dbe3-449f-9ccd-6f23ac6ef9f1/resourceGroups/vnet/providers/Microsoft.Network/virtualNetworks/test-vnet/subnets/master"',
            'workersubnet': '/subscriptions/af848f0a-dbe3-449f-9ccd-6f23ac6ef9f1/resourceGroups/vnet/providers/Microsoft.Network/virtualNetworks/test-vnet/subnets/worker"'
        })

        self.cmd('aro create -g {rg} -n {name} --worker-subnet {mastersubnet} --master-subnet {workersubnet} --tags foo=doo',
            checks=[
                self.check('tags.foo', 'doo'),
                self.check('name', '{name}'),
                self.check('properties.masterProfile.subnetId','{mastersubnet}'),
                self.check('properties.workersProfile[0].subnetId', '{workersubnet}')])

        self.cmd('aro update -g {rg} -n {name} --tags foo=boo', checks=[
            self.check('tags.foo', 'boo')
        ])

        count = len(self.cmd('aro list').get_output_in_json())
        self.cmd('aro show -g {rg} -n {name}', checks=[
            self.check('name', '{name}'),
            self.check('resourceGroup', '{rg}'),
            self.check('tags.foo', 'boo')])

        self.cmd('aro delete -g {rg} -n {name}')

        final_count = len(self.cmd('aro list').get_output_in_json())
        self.assertTrue(final_count, count - 1)
