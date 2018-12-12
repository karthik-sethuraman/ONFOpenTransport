# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_topology_risk_characteristic import TapiTopologyRiskCharacteristic  # noqa: F401,E501
from tapi_server import util


class TapiTopologyRiskParameterPac(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, risk_characteristic=None):  # noqa: E501
        """TapiTopologyRiskParameterPac - a model defined in OpenAPI

        :param risk_characteristic: The risk_characteristic of this TapiTopologyRiskParameterPac.  # noqa: E501
        :type risk_characteristic: List[TapiTopologyRiskCharacteristic]
        """
        self.openapi_types = {
            'risk_characteristic': List[TapiTopologyRiskCharacteristic]
        }

        self.attribute_map = {
            'risk_characteristic': 'risk-characteristic'
        }

        self._risk_characteristic = risk_characteristic

    @classmethod
    def from_dict(cls, dikt) -> 'TapiTopologyRiskParameterPac':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.topology.RiskParameterPac of this TapiTopologyRiskParameterPac.  # noqa: E501
        :rtype: TapiTopologyRiskParameterPac
        """
        return util.deserialize_model(dikt, cls)

    @property
    def risk_characteristic(self):
        """Gets the risk_characteristic of this TapiTopologyRiskParameterPac.

        A list of risk characteristics for consideration in an analysis of shared risk. Each element of the list represents a specific risk consideration.  # noqa: E501

        :return: The risk_characteristic of this TapiTopologyRiskParameterPac.
        :rtype: List[TapiTopologyRiskCharacteristic]
        """
        return self._risk_characteristic

    @risk_characteristic.setter
    def risk_characteristic(self, risk_characteristic):
        """Sets the risk_characteristic of this TapiTopologyRiskParameterPac.

        A list of risk characteristics for consideration in an analysis of shared risk. Each element of the list represents a specific risk consideration.  # noqa: E501

        :param risk_characteristic: The risk_characteristic of this TapiTopologyRiskParameterPac.
        :type risk_characteristic: List[TapiTopologyRiskCharacteristic]
        """

        self._risk_characteristic = risk_characteristic