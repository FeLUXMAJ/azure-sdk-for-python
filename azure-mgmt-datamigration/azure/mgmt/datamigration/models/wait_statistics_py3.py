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


class WaitStatistics(Model):
    """Wait statistics gathered during query batch execution.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar wait_type: Type of the Wait
    :vartype wait_type: str
    :ivar wait_time_ms: Total wait time in millisecond(s). Default value: 0 .
    :vartype wait_time_ms: float
    :ivar wait_count: Total no. of waits
    :vartype wait_count: long
    """

    _validation = {
        'wait_type': {'readonly': True},
        'wait_time_ms': {'readonly': True},
        'wait_count': {'readonly': True},
    }

    _attribute_map = {
        'wait_type': {'key': 'waitType', 'type': 'str'},
        'wait_time_ms': {'key': 'waitTimeMs', 'type': 'float'},
        'wait_count': {'key': 'waitCount', 'type': 'long'},
    }

    def __init__(self, **kwargs) -> None:
        super(WaitStatistics, self).__init__(**kwargs)
        self.wait_type = None
        self.wait_time_ms = None
        self.wait_count = None