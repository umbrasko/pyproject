import os


class Example(object):
    """
    This class description
    Example
    -------
    >>> from pyproject.src.example import Example
    >>> obj = Example()
    """
    def __init__(self):
        self.unit = ""

    def set_unit(self, unit):
        """
        Set unit
        Parameters:
            unit : str
                Unit.
        Example
        -------
        >>> from pyproject.src.example import Example
        >>> obj = Example()
        >>> obj.set_unit('per sample')
        >>> print (obj.unit)
        per sample
        """
        if unit:
            self.unit = unit
