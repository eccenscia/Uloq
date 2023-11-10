# coding: utf-8

"""
    Uloq Requestor Service

    Requestor Endpoints  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from Eccenscia.Services.Models.configuration import Configuration


class ApplicationActivationResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'application_identity': 'str',
        'response': 'str',
        'active': 'bool'
    }

    attribute_map = {
        'application_identity': 'ApplicationIdentity',
        'response': 'Response',
        'active': 'Active'
    }

    def __init__(self, application_identity=None, response=None, active=None, local_vars_configuration=None):  # noqa: E501
        """ApplicationActivationResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._application_identity = None
        self._response = None
        self._active = None
        self.discriminator = None

        if application_identity is not None:
            self.application_identity = application_identity
        if response is not None:
            self.response = response
        if active is not None:
            self.active = active

    @property
    def application_identity(self):
        """Gets the application_identity of this ApplicationActivationResponse.  # noqa: E501

        Application public identity - generated  # noqa: E501

        :return: The application_identity of this ApplicationActivationResponse.  # noqa: E501
        :rtype: str
        """
        return self._application_identity

    @application_identity.setter
    def application_identity(self, application_identity):
        """Sets the application_identity of this ApplicationActivationResponse.

        Application public identity - generated  # noqa: E501

        :param application_identity: The application_identity of this ApplicationActivationResponse.  # noqa: E501
        :type: str
        """

        self._application_identity = application_identity

    @property
    def response(self):
        """Gets the response of this ApplicationActivationResponse.  # noqa: E501

        deactivation message  # noqa: E501

        :return: The response of this ApplicationActivationResponse.  # noqa: E501
        :rtype: str
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this ApplicationActivationResponse.

        deactivation message  # noqa: E501

        :param response: The response of this ApplicationActivationResponse.  # noqa: E501
        :type: str
        """

        self._response = response

    @property
    def active(self):
        """Gets the active of this ApplicationActivationResponse.  # noqa: E501

        activation state  # noqa: E501

        :return: The active of this ApplicationActivationResponse.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this ApplicationActivationResponse.

        activation state  # noqa: E501

        :param active: The active of this ApplicationActivationResponse.  # noqa: E501
        :type: bool
        """

        self._active = active

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApplicationActivationResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplicationActivationResponse):
            return True

        return self.to_dict() != other.to_dict()
