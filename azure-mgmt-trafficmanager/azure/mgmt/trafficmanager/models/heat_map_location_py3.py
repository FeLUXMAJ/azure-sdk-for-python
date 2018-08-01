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


class HeatMapLocation(Model):
    """Class which represents locations of traffic sources and percentage.

    :param location: Location of heatmap traffic sources.
    :type location: str
    :param percentage: Percentage of traffic from a specific location.
    :type percentage: float
    """

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'percentage': {'key': 'percentage', 'type': 'float'},
    }

    def __init__(self, *, location: str=None, percentage: float=None, **kwargs) -> None:
        super(HeatMapLocation, self).__init__(**kwargs)
        self.location = location
        self.percentage = percentage
