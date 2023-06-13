# coding: utf-8



from pprint import pformat
from ..utils import to_dict


class HtmlView(object):
    def __init__(self, inline=None, width=None, height=None):

        self._inline = inline
        self._width = width
        self._height = height


    @property
    def inline(self):
        return self._inline

    @inline.setter
    def inline(self, inline):

        self._inline = inline

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):

        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):

        self._height = height

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        return to_dict(self.__dict__)

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
