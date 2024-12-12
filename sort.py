"""
The sort function
"""
import constants

def sort(width, height, length, mass):
    """
    Sort packages into stacks based on their dimensions and mass.
    Units are centimeters for the dimensions and kilogram for the mass.
    NOTE: This version is optimized for readability

    Args:
        width (int): the width of the package
        height (int): the height of the package
        length (int): the length of the package
        mass (int): the mass of the package

    NOTE: I've assumed that the measurements are ints as to include data validation.
    If that causes your unit tests then please let me know.

    Returns:
        str: The name of the stack where the package should go.
    """
    # Ensure all params are ints
    if any(not isinstance(x, int) for x in [width, height, length, mass]):
        return constants.INTEGER_ERROR_MESSAGE

    # Ensure all params are > 0
    if any(x <= 0 for x in [width, height, length, mass]):
        return constants.ZERO_OR_NEGATIVE_ERROR_MESSAGE

    # Initialize booleans
    bulky = False
    heavy = False

    #A package is bulky if its volume (Width x Height x Length) is >= 1,000,000 cm³...
    volume = width * height * length
    volume_is_bulky = volume >= constants.MAX_VOLUME

    # ...or when one of its dimensions is greater or equal to 150 cm.
    dimensions_are_bulky = any(x >= constants.MAX_ANY_DIMENSION for x in [width, height, length])

    if volume_is_bulky or dimensions_are_bulky:
        bulky = True

    # A package is heavy when its mass is greater or equal to 20 kg.
    if mass >= 20:
        heavy = True

    # STANDARD: not bulky or heavy.
    if not bulky and not heavy:
        return constants.STANDARD

    # SPECIAL: either heavy or bulky.
    if heavy != bulky:  # Use != to calculate XOR of these two booleans
        return constants.SPECIAL

    # REJECTED: both heavy and bulky.
    if heavy and bulky:
        return constants.REJECTED
