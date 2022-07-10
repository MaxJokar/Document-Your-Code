"""
We can document our functions, classes, methods , etc
are deprecated with the help of integrated Sphinx directives:
"""


from deprecated.sphinx import deprecated
from deprecated.sphinx import versionadded
from deprecated.sphinx import versionchanged


@versionadded(version="1.0", reason="This function is new")
def function_one():
    """This is the function one"""


@versionchanged(version="1.0", reason="This function is modified")
def function_two():
    """This is the function two"""


@deprecated(version="1.0", reason="This function will be removed soon")
def function_three():
    """This is the function three"""
