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


class ElasticPoolDtuCapability(Model):
    """The Elastic Pool DTU capability.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar limit: The maximum size of the database (see 'unit' for the units).
    :vartype limit: long
    :ivar max_database_count: The maximum number of databases supported.
    :vartype max_database_count: long
    :ivar status: The status of the capability. Possible values include:
     'Visible', 'Available', 'Default', 'Disabled'
    :vartype status: str or ~azure.mgmt.sql.models.CapabilityStatus
    :ivar supported_max_sizes: The list of supported max sizes.
    :vartype supported_max_sizes:
     list[~azure.mgmt.sql.models.MaxSizeCapability]
    :ivar included_max_size: The included (free) max size for this service
     level objective.
    :vartype included_max_size: ~azure.mgmt.sql.models.MaxSizeCapability
    :ivar supported_per_database_max_sizes: The list of supported max database
     sizes.
    :vartype supported_per_database_max_sizes:
     list[~azure.mgmt.sql.models.MaxSizeCapability]
    :ivar supported_per_database_max_dtus: The list of supported max database
     DTUs.
    :vartype supported_per_database_max_dtus:
     list[~azure.mgmt.sql.models.ElasticPoolPerDatabaseMaxDtuCapability]
    """

    _validation = {
        'limit': {'readonly': True},
        'max_database_count': {'readonly': True},
        'status': {'readonly': True},
        'supported_max_sizes': {'readonly': True},
        'included_max_size': {'readonly': True},
        'supported_per_database_max_sizes': {'readonly': True},
        'supported_per_database_max_dtus': {'readonly': True},
    }

    _attribute_map = {
        'limit': {'key': 'limit', 'type': 'long'},
        'max_database_count': {'key': 'maxDatabaseCount', 'type': 'long'},
        'status': {'key': 'status', 'type': 'CapabilityStatus'},
        'supported_max_sizes': {'key': 'supportedMaxSizes', 'type': '[MaxSizeCapability]'},
        'included_max_size': {'key': 'includedMaxSize', 'type': 'MaxSizeCapability'},
        'supported_per_database_max_sizes': {'key': 'supportedPerDatabaseMaxSizes', 'type': '[MaxSizeCapability]'},
        'supported_per_database_max_dtus': {'key': 'supportedPerDatabaseMaxDtus', 'type': '[ElasticPoolPerDatabaseMaxDtuCapability]'},
    }

    def __init__(self):
        super(ElasticPoolDtuCapability, self).__init__()
        self.limit = None
        self.max_database_count = None
        self.status = None
        self.supported_max_sizes = None
        self.included_max_size = None
        self.supported_per_database_max_sizes = None
        self.supported_per_database_max_dtus = None