# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Obfn(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, beam_id: int=None, beam_enable: bool=None, x_offset_angle: int=None, y_offset_angle: int=None, width: int=None):  # noqa: E501
        """Obfn - a model defined in Swagger

        :param beam_id: The beam_id of this Obfn.  # noqa: E501
        :type beam_id: int
        :param beam_enable: The beam_enable of this Obfn.  # noqa: E501
        :type beam_enable: bool
        :param x_offset_angle: The x_offset_angle of this Obfn.  # noqa: E501
        :type x_offset_angle: int
        :param y_offset_angle: The y_offset_angle of this Obfn.  # noqa: E501
        :type y_offset_angle: int
        :param width: The width of this Obfn.  # noqa: E501
        :type width: int
        """
        self.swagger_types = {
            'beam_id': int,
            'beam_enable': bool,
            'x_offset_angle': int,
            'y_offset_angle': int,
            'width': int
        }

        self.attribute_map = {
            'beam_id': 'beam-id',
            'beam_enable': 'beam-enable',
            'x_offset_angle': 'x-offset-angle',
            'y_offset_angle': 'y-offset-angle',
            'width': 'width'
        }

        self._beam_id = beam_id
        self._beam_enable = beam_enable
        self._x_offset_angle = x_offset_angle
        self._y_offset_angle = y_offset_angle
        self._width = width

    @classmethod
    def from_dict(cls, dikt) -> 'Obfn':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The obfn of this Obfn.  # noqa: E501
        :rtype: Obfn
        """
        return util.deserialize_model(dikt, cls)

    @property
    def beam_id(self) -> int:
        """Gets the beam_id of this Obfn.


        :return: The beam_id of this Obfn.
        :rtype: int
        """
        return self._beam_id

    @beam_id.setter
    def beam_id(self, beam_id: int):
        """Sets the beam_id of this Obfn.


        :param beam_id: The beam_id of this Obfn.
        :type beam_id: int
        """

        self._beam_id = beam_id

    @property
    def beam_enable(self) -> bool:
        """Gets the beam_enable of this Obfn.


        :return: The beam_enable of this Obfn.
        :rtype: bool
        """
        return self._beam_enable

    @beam_enable.setter
    def beam_enable(self, beam_enable: bool):
        """Sets the beam_enable of this Obfn.


        :param beam_enable: The beam_enable of this Obfn.
        :type beam_enable: bool
        """

        self._beam_enable = beam_enable

    @property
    def x_offset_angle(self) -> int:
        """Gets the x_offset_angle of this Obfn.


        :return: The x_offset_angle of this Obfn.
        :rtype: int
        """
        return self._x_offset_angle

    @x_offset_angle.setter
    def x_offset_angle(self, x_offset_angle: int):
        """Sets the x_offset_angle of this Obfn.


        :param x_offset_angle: The x_offset_angle of this Obfn.
        :type x_offset_angle: int
        """

        self._x_offset_angle = x_offset_angle

    @property
    def y_offset_angle(self) -> int:
        """Gets the y_offset_angle of this Obfn.


        :return: The y_offset_angle of this Obfn.
        :rtype: int
        """
        return self._y_offset_angle

    @y_offset_angle.setter
    def y_offset_angle(self, y_offset_angle: int):
        """Sets the y_offset_angle of this Obfn.


        :param y_offset_angle: The y_offset_angle of this Obfn.
        :type y_offset_angle: int
        """

        self._y_offset_angle = y_offset_angle

    @property
    def width(self) -> int:
        """Gets the width of this Obfn.


        :return: The width of this Obfn.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width: int):
        """Sets the width of this Obfn.


        :param width: The width of this Obfn.
        :type width: int
        """

        self._width = width