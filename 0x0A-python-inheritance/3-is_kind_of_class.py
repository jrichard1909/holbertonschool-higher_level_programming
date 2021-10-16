#!/usr/bin/python3
"""is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Function that returns True if obj isinstance of.
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
