#!/usr/bin/python3
"""MyList
"""


class MyList(list):
    """
        inherits
    """

    def print_sorted(self):
        """Prints sorted list
        """

        print(sorted(self))
