# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class NodeRemoveParameter(Model):
    """Options for removing compute nodes from a pool.

    All required parameters must be populated in order to send to Azure.

    :param node_list: Required. A list containing the IDs of the compute nodes
     to be removed from the specified pool.
    :type node_list: list[str]
    :param resize_timeout: The timeout for removal of compute nodes to the
     pool. The default value is 15 minutes. The minimum value is 5 minutes. If
     you specify a value less than 5 minutes, the Batch service returns an
     error; if you are calling the REST API directly, the HTTP status code is
     400 (Bad Request).
    :type resize_timeout: timedelta
    :param node_deallocation_option: Determines what to do with a node and its
     running task(s) after it has been selected for deallocation. The default
     value is requeue. Possible values include: 'requeue', 'terminate',
     'taskCompletion', 'retainedData'
    :type node_deallocation_option: str or
     ~azure.batch.models.ComputeNodeDeallocationOption
    """

    _validation = {
        'node_list': {'required': True, 'max_items': 100},
    }

    _attribute_map = {
        'node_list': {'key': 'nodeList', 'type': '[str]'},
        'resize_timeout': {'key': 'resizeTimeout', 'type': 'duration'},
        'node_deallocation_option': {'key': 'nodeDeallocationOption', 'type': 'ComputeNodeDeallocationOption'},
    }

    def __init__(self, *, node_list, resize_timeout=None, node_deallocation_option=None, **kwargs) -> None:
        super(NodeRemoveParameter, self).__init__(**kwargs)
        self.node_list = node_list
        self.resize_timeout = resize_timeout
        self.node_deallocation_option = node_deallocation_option