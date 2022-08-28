# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class PetAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None):  # noqa: E501
        """PetAllOf - a model defined in OpenAPI

        :param id: The id of this PetAllOf.  # noqa: E501
        :type id: int
        """
        self.openapi_types = {
            'id': int
        }

        self.attribute_map = {
            'id': 'id'
        }

        self._id = id

    @classmethod
    def from_dict(cls, dikt) -> 'PetAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Pet_allOf of this PetAllOf.  # noqa: E501
        :rtype: PetAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this PetAllOf.


        :return: The id of this PetAllOf.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PetAllOf.


        :param id: The id of this PetAllOf.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id
