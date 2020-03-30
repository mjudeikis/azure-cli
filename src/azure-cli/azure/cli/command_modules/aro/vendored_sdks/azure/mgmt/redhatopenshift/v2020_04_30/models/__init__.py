# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

try:
    from ._models_py3 import APIServerProfile
    from ._models_py3 import AzureEntityResource
    from ._models_py3 import CloudError, CloudErrorException
    from ._models_py3 import CloudErrorBody
    from ._models_py3 import ClusterProfile
    from ._models_py3 import ConsoleProfile
    from ._models_py3 import Display
    from ._models_py3 import IngressProfile
    from ._models_py3 import MasterProfile
    from ._models_py3 import NetworkProfile
    from ._models_py3 import OpenShiftCluster
    from ._models_py3 import OpenShiftClusterCredentials
    from ._models_py3 import OpenShiftClusterUpdate
    from ._models_py3 import Operation
    from ._models_py3 import ProxyResource
    from ._models_py3 import Resource
    from ._models_py3 import ServicePrincipalProfile
    from ._models_py3 import TrackedResource
    from ._models_py3 import WorkerProfile
except (SyntaxError, ImportError):
    from ._models import APIServerProfile
    from ._models import AzureEntityResource
    from ._models import CloudError, CloudErrorException
    from ._models import CloudErrorBody
    from ._models import ClusterProfile
    from ._models import ConsoleProfile
    from ._models import Display
    from ._models import IngressProfile
    from ._models import MasterProfile
    from ._models import NetworkProfile
    from ._models import OpenShiftCluster
    from ._models import OpenShiftClusterCredentials
    from ._models import OpenShiftClusterUpdate
    from ._models import Operation
    from ._models import ProxyResource
    from ._models import Resource
    from ._models import ServicePrincipalProfile
    from ._models import TrackedResource
    from ._models import WorkerProfile
from ._paged_models import OpenShiftClusterPaged
from ._paged_models import OperationPaged

__all__ = [
    'APIServerProfile',
    'AzureEntityResource',
    'CloudError', 'CloudErrorException',
    'CloudErrorBody',
    'ClusterProfile',
    'ConsoleProfile',
    'Display',
    'IngressProfile',
    'MasterProfile',
    'NetworkProfile',
    'OpenShiftCluster',
    'OpenShiftClusterCredentials',
    'OpenShiftClusterUpdate',
    'Operation',
    'ProxyResource',
    'Resource',
    'ServicePrincipalProfile',
    'TrackedResource',
    'WorkerProfile',
    'OperationPaged',
    'OpenShiftClusterPaged',
]
