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


class UpgradeRecommendedElasticPoolProperties(Model):
    """Represents the properties of a Azure SQL Recommended Elastic Pool being
    upgraded.

    :param name: The name of the Azure SQL Recommended Elastic Pool being
     upgraded.
    :type name: str
    :param edition: The target edition for the Azure SQL Recommended Elastic
     Pool being upgraded. Possible values include: 'Basic', 'Standard',
     'Premium'
    :type edition: str or :class:`TargetElasticPoolEditions
     <azure.mgmt.sql.models.TargetElasticPoolEditions>`
    :param dtu: The DTU guarantee for the Azure SQL Recommended Elastic Pool
     being upgraded.
    :type dtu: int
    :param storage_mb: The storage limit in MB for the Azure SQL Recommended
     Elastic Pool being upgraded.
    :type storage_mb: int
    :param database_dtu_min: The DTU guarantee for database for the Azure SQL
     Recommended Elastic Pool being upgraded.
    :type database_dtu_min: int
    :param database_dtu_max: The DTU cap for database for the Azure SQL
     Recommended Elastic Pool being upgraded.
    :type database_dtu_max: int
    :param database_collection: The list of database names to be put in the
     Azure SQL Recommended Elastic Pool being upgraded.
    :type database_collection: list of str
    :param include_all_databases: Gets or sets whether all databases to be
     put in the Azure SQL Recommended Elastic Pool being upgraded.
    :type include_all_databases: bool
    """ 

    _validation = {
        'name': {'required': True},
        'edition': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'edition': {'key': 'Edition', 'type': 'TargetElasticPoolEditions'},
        'dtu': {'key': 'Dtu', 'type': 'int'},
        'storage_mb': {'key': 'StorageMb', 'type': 'int'},
        'database_dtu_min': {'key': 'DatabaseDtuMin', 'type': 'int'},
        'database_dtu_max': {'key': 'DatabaseDtuMax', 'type': 'int'},
        'database_collection': {'key': 'DatabaseCollection', 'type': '[str]'},
        'include_all_databases': {'key': 'IncludeAllDatabases', 'type': 'bool'},
    }

    def __init__(self, name, edition, dtu=None, storage_mb=None, database_dtu_min=None, database_dtu_max=None, database_collection=None, include_all_databases=None):
        self.name = name
        self.edition = edition
        self.dtu = dtu
        self.storage_mb = storage_mb
        self.database_dtu_min = database_dtu_min
        self.database_dtu_max = database_dtu_max
        self.database_collection = database_collection
        self.include_all_databases = include_all_databases
