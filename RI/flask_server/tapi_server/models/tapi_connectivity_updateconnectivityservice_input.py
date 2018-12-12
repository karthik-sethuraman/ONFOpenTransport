# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_connectivity_connectivity_constraint import TapiConnectivityConnectivityConstraint  # noqa: F401,E501
from tapi_server.models.tapi_connectivity_connectivityservice_end_point import TapiConnectivityConnectivityserviceEndPoint  # noqa: F401,E501
from tapi_server.models.tapi_connectivity_resilience_constraint import TapiConnectivityResilienceConstraint  # noqa: F401,E501
from tapi_server.models.tapi_path_computation_routing_constraint import TapiPathComputationRoutingConstraint  # noqa: F401,E501
from tapi_server.models.tapi_path_computation_topology_constraint import TapiPathComputationTopologyConstraint  # noqa: F401,E501
from tapi_server import util


class TapiConnectivityUpdateconnectivityserviceInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, service_id_or_name=None, topology_constraint=None, end_point=None, resilience_constraint=None, routing_constraint=None, state=None, connectivity_constraint=None):  # noqa: E501
        """TapiConnectivityUpdateconnectivityserviceInput - a model defined in OpenAPI

        :param service_id_or_name: The service_id_or_name of this TapiConnectivityUpdateconnectivityserviceInput.  # noqa: E501
        :type service_id_or_name: str
        :param topology_constraint: The topology_constraint of this TapiConnectivityUpdateconnectivityserviceInput.  # noqa: E501
        :type topology_constraint: TapiPathComputationTopologyConstraint
        :param end_point: The end_point of this TapiConnectivityUpdateconnectivityserviceInput.  # noqa: E501
        :type end_point: List[TapiConnectivityConnectivityserviceEndPoint]
        :param resilience_constraint: The resilience_constraint of this TapiConnectivityUpdateconnectivityserviceInput.  # noqa: E501
        :type resilience_constraint: TapiConnectivityResilienceConstraint
        :param routing_constraint: The routing_constraint of this TapiConnectivityUpdateconnectivityserviceInput.  # noqa: E501
        :type routing_constraint: TapiPathComputationRoutingConstraint
        :param state: The state of this TapiConnectivityUpdateconnectivityserviceInput.  # noqa: E501
        :type state: str
        :param connectivity_constraint: The connectivity_constraint of this TapiConnectivityUpdateconnectivityserviceInput.  # noqa: E501
        :type connectivity_constraint: TapiConnectivityConnectivityConstraint
        """
        self.openapi_types = {
            'service_id_or_name': str,
            'topology_constraint': TapiPathComputationTopologyConstraint,
            'end_point': List[TapiConnectivityConnectivityserviceEndPoint],
            'resilience_constraint': TapiConnectivityResilienceConstraint,
            'routing_constraint': TapiPathComputationRoutingConstraint,
            'state': str,
            'connectivity_constraint': TapiConnectivityConnectivityConstraint
        }

        self.attribute_map = {
            'service_id_or_name': 'service-id-or-name',
            'topology_constraint': 'topology-constraint',
            'end_point': 'end-point',
            'resilience_constraint': 'resilience-constraint',
            'routing_constraint': 'routing-constraint',
            'state': 'state',
            'connectivity_constraint': 'connectivity-constraint'
        }

        self._service_id_or_name = service_id_or_name
        self._topology_constraint = topology_constraint
        self._end_point = end_point
        self._resilience_constraint = resilience_constraint
        self._routing_constraint = routing_constraint
        self._state = state
        self._connectivity_constraint = connectivity_constraint

    @classmethod
    def from_dict(cls, dikt) -> 'TapiConnectivityUpdateconnectivityserviceInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.connectivity.updateconnectivityservice.Input of this TapiConnectivityUpdateconnectivityserviceInput.  # noqa: E501
        :rtype: TapiConnectivityUpdateconnectivityserviceInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def service_id_or_name(self):
        """Gets the service_id_or_name of this TapiConnectivityUpdateconnectivityserviceInput.

        none  # noqa: E501

        :return: The service_id_or_name of this TapiConnectivityUpdateconnectivityserviceInput.
        :rtype: str
        """
        return self._service_id_or_name

    @service_id_or_name.setter
    def service_id_or_name(self, service_id_or_name):
        """Sets the service_id_or_name of this TapiConnectivityUpdateconnectivityserviceInput.

        none  # noqa: E501

        :param service_id_or_name: The service_id_or_name of this TapiConnectivityUpdateconnectivityserviceInput.
        :type service_id_or_name: str
        """

        self._service_id_or_name = service_id_or_name

    @property
    def topology_constraint(self):
        """Gets the topology_constraint of this TapiConnectivityUpdateconnectivityserviceInput.


        :return: The topology_constraint of this TapiConnectivityUpdateconnectivityserviceInput.
        :rtype: TapiPathComputationTopologyConstraint
        """
        return self._topology_constraint

    @topology_constraint.setter
    def topology_constraint(self, topology_constraint):
        """Sets the topology_constraint of this TapiConnectivityUpdateconnectivityserviceInput.


        :param topology_constraint: The topology_constraint of this TapiConnectivityUpdateconnectivityserviceInput.
        :type topology_constraint: TapiPathComputationTopologyConstraint
        """

        self._topology_constraint = topology_constraint

    @property
    def end_point(self):
        """Gets the end_point of this TapiConnectivityUpdateconnectivityserviceInput.

        none  # noqa: E501

        :return: The end_point of this TapiConnectivityUpdateconnectivityserviceInput.
        :rtype: List[TapiConnectivityConnectivityserviceEndPoint]
        """
        return self._end_point

    @end_point.setter
    def end_point(self, end_point):
        """Sets the end_point of this TapiConnectivityUpdateconnectivityserviceInput.

        none  # noqa: E501

        :param end_point: The end_point of this TapiConnectivityUpdateconnectivityserviceInput.
        :type end_point: List[TapiConnectivityConnectivityserviceEndPoint]
        """

        self._end_point = end_point

    @property
    def resilience_constraint(self):
        """Gets the resilience_constraint of this TapiConnectivityUpdateconnectivityserviceInput.


        :return: The resilience_constraint of this TapiConnectivityUpdateconnectivityserviceInput.
        :rtype: TapiConnectivityResilienceConstraint
        """
        return self._resilience_constraint

    @resilience_constraint.setter
    def resilience_constraint(self, resilience_constraint):
        """Sets the resilience_constraint of this TapiConnectivityUpdateconnectivityserviceInput.


        :param resilience_constraint: The resilience_constraint of this TapiConnectivityUpdateconnectivityserviceInput.
        :type resilience_constraint: TapiConnectivityResilienceConstraint
        """

        self._resilience_constraint = resilience_constraint

    @property
    def routing_constraint(self):
        """Gets the routing_constraint of this TapiConnectivityUpdateconnectivityserviceInput.


        :return: The routing_constraint of this TapiConnectivityUpdateconnectivityserviceInput.
        :rtype: TapiPathComputationRoutingConstraint
        """
        return self._routing_constraint

    @routing_constraint.setter
    def routing_constraint(self, routing_constraint):
        """Sets the routing_constraint of this TapiConnectivityUpdateconnectivityserviceInput.


        :param routing_constraint: The routing_constraint of this TapiConnectivityUpdateconnectivityserviceInput.
        :type routing_constraint: TapiPathComputationRoutingConstraint
        """

        self._routing_constraint = routing_constraint

    @property
    def state(self):
        """Gets the state of this TapiConnectivityUpdateconnectivityserviceInput.

        none  # noqa: E501

        :return: The state of this TapiConnectivityUpdateconnectivityserviceInput.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TapiConnectivityUpdateconnectivityserviceInput.

        none  # noqa: E501

        :param state: The state of this TapiConnectivityUpdateconnectivityserviceInput.
        :type state: str
        """

        self._state = state

    @property
    def connectivity_constraint(self):
        """Gets the connectivity_constraint of this TapiConnectivityUpdateconnectivityserviceInput.


        :return: The connectivity_constraint of this TapiConnectivityUpdateconnectivityserviceInput.
        :rtype: TapiConnectivityConnectivityConstraint
        """
        return self._connectivity_constraint

    @connectivity_constraint.setter
    def connectivity_constraint(self, connectivity_constraint):
        """Sets the connectivity_constraint of this TapiConnectivityUpdateconnectivityserviceInput.


        :param connectivity_constraint: The connectivity_constraint of this TapiConnectivityUpdateconnectivityserviceInput.
        :type connectivity_constraint: TapiConnectivityConnectivityConstraint
        """

        self._connectivity_constraint = connectivity_constraint