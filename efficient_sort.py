"""
An efficient version of the sort function
"""
import constants


def sort(width, height, length, mass):
    """
    Sort packages into stacks based on their dimensions and mass.
    Units are centimeters for the dimensions and kilogram for the mass.
    NOTE: This version is optimized for minimal lines of code + runtime

    Args:
        width (int): the width of the package
        height (int): the height of the package
        length (int): the length of the package
        mass (int): the mass of the package

    NOTE: I've assumed that the measurements are ints as to include data validation. =
    If that causes your unit tests then please let me know.

    Returns:
        str: The name of the stack where the package should go.
    """
    if any(not isinstance(x, int) for x in [width, height, length, mass]):
        return constants.INTEGER_ERROR_MESSAGE
    if any(x <= 0 for x in [width, height, length, mass]):
        return constants.ZERO_OR_NEGATIVE_ERROR_MESSAGE

    bulky = ((width * height * length >= constants.MAX_VOLUME)
            or any(x >= constants.MAX_ANY_DIMENSION for x in [width, height, length]))
    heavy = mass >= 20

    if not bulky and not heavy:
        return constants.STANDARD
    if heavy and bulky:
        return constants.REJECTED
    return constants.SPECIAL
