# Copyright (c) Microsoft Corporation.
# Licensed under the Apache License 2.0.

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import ScenarioTest, ResourceGroupPreparer

class AroScenarioTests(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_aro_create')
    @AllowLargeResponse
    def test_aro_create(self, resource_group):
        self.kwargs.update({
            'name': 'aro',
            "subscription": "225e02bc-43d0-43d1-a01a-17e584a4ef69",
            "master_subnet": "/subscriptions/225e02bc-43d0-43d1-a01a-17e584a4ef69/resourceGroups/v4-eastus/providers/Microsoft.Network/virtualNetworks/dev-vnet/subnets/dev-masters",
            "worker_subnet": "/subscriptions/225e02bc-43d0-43d1-a01a-17e584a4ef69/resourceGroups/v4-eastus/providers/Microsoft.Network/virtualNetworks/dev-vnet/subnets/dev-workers",
        })

        self.cmd('aro create -g {rg} -n {name} --master-subnet {master_subnet} --worker-subnet {worker_subnet} --tags foo=doo', checks=[
            self.check('tags.foo', 'doo'),
            self.check('name', '{name}'),
            self.check('properties.masterProfile.subnetId','{master_subnet}'),
            self.check('properties.workersProfile[0].subnetId', '{worker_subnet}')
        ])
