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


class QRCodeRequest(object):
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
        'request_type': 'str',
        'category': 'str',
        'action_title': 'str',
        'action_message': 'str',
        'metadata': 'str',
        'public_key': 'str'
    }

    attribute_map = {
        'request_type': 'RequestType',
        'category': 'Category',
        'action_title': 'ActionTitle',
        'action_message': 'ActionMessage',
        'metadata': 'Metadata',
        'public_key': 'PublicKey'
    }

    def __init__(self, request_type=None, category=None, action_title=None, action_message=None, metadata=None, public_key=None, local_vars_configuration=None):  # noqa: E501
        """QRCodeRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._request_type = None
        self._category = None
        self._action_title = None
        self._action_message = None
        self._metadata = None
        self._public_key = None
        self.discriminator = None

        if request_type is not None:
            self.request_type = request_type
        if category is not None:
            self.category = category
        if action_title is not None:
            self.action_title = action_title
        if action_message is not None:
            self.action_message = action_message
        if metadata is not None:
            self.metadata = metadata
        if public_key is not None:
            self.public_key = public_key

    @property
    def request_type(self):
        """Gets the request_type of this QRCodeRequest.  # noqa: E501


        :return: The request_type of this QRCodeRequest.  # noqa: E501
        :rtype: str
        """
        return self._request_type

    @request_type.setter
    def request_type(self, request_type):
        """Sets the request_type of this QRCodeRequest.


        :param request_type: The request_type of this QRCodeRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Sign", "KeyExchange"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and request_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `request_type` ({0}), must be one of {1}"  # noqa: E501
                .format(request_type, allowed_values)
            )

        self._request_type = request_type

    @property
    def category(self):
        """Gets the category of this QRCodeRequest.  # noqa: E501

        The Category in which to display this request  # noqa: E501

        :return: The category of this QRCodeRequest.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this QRCodeRequest.

        The Category in which to display this request  # noqa: E501

        :param category: The category of this QRCodeRequest.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def action_title(self):
        """Gets the action_title of this QRCodeRequest.  # noqa: E501

        Title of the approval request  # noqa: E501

        :return: The action_title of this QRCodeRequest.  # noqa: E501
        :rtype: str
        """
        return self._action_title

    @action_title.setter
    def action_title(self, action_title):
        """Sets the action_title of this QRCodeRequest.

        Title of the approval request  # noqa: E501

        :param action_title: The action_title of this QRCodeRequest.  # noqa: E501
        :type: str
        """

        self._action_title = action_title

    @property
    def action_message(self):
        """Gets the action_message of this QRCodeRequest.  # noqa: E501

        Short description of the approval  # noqa: E501

        :return: The action_message of this QRCodeRequest.  # noqa: E501
        :rtype: str
        """
        return self._action_message

    @action_message.setter
    def action_message(self, action_message):
        """Sets the action_message of this QRCodeRequest.

        Short description of the approval  # noqa: E501

        :param action_message: The action_message of this QRCodeRequest.  # noqa: E501
        :type: str
        """

        self._action_message = action_message

    @property
    def metadata(self):
        """Gets the metadata of this QRCodeRequest.  # noqa: E501

        Additional data related to the approval.  # noqa: E501

        :return: The metadata of this QRCodeRequest.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this QRCodeRequest.

        Additional data related to the approval.  # noqa: E501

        :param metadata: The metadata of this QRCodeRequest.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def public_key(self):
        """Gets the public_key of this QRCodeRequest.  # noqa: E501


        :return: The public_key of this QRCodeRequest.  # noqa: E501
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this QRCodeRequest.


        :param public_key: The public_key of this QRCodeRequest.  # noqa: E501
        :type: str
        """

        self._public_key = public_key

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
        if not isinstance(other, QRCodeRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QRCodeRequest):
            return True

        return self.to_dict() != other.to_dict()
