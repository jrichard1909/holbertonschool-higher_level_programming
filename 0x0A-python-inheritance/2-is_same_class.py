#!/usr/bin/python3
"""is_same_class
"""


def is_same_class(obj, a_class):
    """Returns True if obj is same instance, else False
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
