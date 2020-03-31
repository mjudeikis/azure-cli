# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from azure.cli.command_modules.test._client_factory import cf_test


def load_command_table(self, _):

    # TODO: Add command type here
    # test_sdk = CliCommandType(
    #    operations_tmpl='<PATH>.operations#.{}',
    #    client_factory=cf_test)


    with self.command_group('test') as g:
        g.custom_command('create', 'create_test')
        # g.command('delete', 'delete')
        g.custom_command('list', 'list_test')
        # g.show_command('show', 'get')
        # g.generic_update_command('update', setter_name='update', custom_func_name='update_test')


    with self.command_group('test', is_preview=True):
        pass

