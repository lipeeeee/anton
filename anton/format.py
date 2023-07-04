"""Format Module that takes care of formatting a string

Helper module with multiple functions aimed to format a given
string
"""

import re


def remove_excessive_spaces(target: str) -> str:
    """Removes excessive spaces from `target`

    Warning: processes parameterized str
    """
    return re.sub(" +", " ", target)


def remove_newline_chars(target: str) -> str:
    """Remove '\n' chars from `target`"""
    target = re.sub("\n", "", target)
    return target
