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



print("=================================================================")
function_one()
function_two()
function_three()  # warns

help(function_one)
help(function_two)
help(function_three)




#  OutPut:
# $ python hello_sphinx.py

# hello_sphinx.py:23: DeprecationWarning: Call to deprecated function (or staticmethod) function_three.
# (This function will be removed soon) -- Deprecated since version 1.0.
#   function_three()  # warns

# Help on function function_one in module __main__:

# function_one()
#     This is the function one

#     .. versionadded:: 1.0
#        This function is new

# Help on function function_two in module __main__:

# function_two()
#     This is the function two

#     .. versionchanged:: 1.0
#        This function is modified

# Help on function function_three in module __main__:

# function_three()
#     This is the function three

#     .. deprecated:: 1.0
#        This function will be removed soon
