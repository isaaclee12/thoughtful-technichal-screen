import constants

def sort(width, height, length, mass):
    """
    Sort packages into stacks based on their dimensions and mass.

    Args:
        width (float): the width of the package
        height (float): the height of the package
        length (float): the length of the package
        mass (float): the mass of the package

    NOTE: I've assumed that the measurements are floats
    Units are centimeters for the dimensions and kilogram for the mass.

    Returns:
        str: The name of the stack where the package should go.
    """
    # DO NOT USE A TERNARY OPERATOR IN THE CODE
    # TODO: Data validation.

    bulky = False
    heavy = False

    # - A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³
    volume = width * height * length
    volume_is_bulky = volume >= constants.MAX_VOLUME

    # or when one of its dimensions is greater or equal to 150 cm.
    # if any of these measures are >= 150... then one of the dimensions IS over the max
    dimensions_are_bulky = any(x >= constants.MAX_ANY_DIMENSION for x in [width, height, length])

    if volume_is_bulky or dimensions_are_bulky:
        bulky = True

    # - A package is **heavy** when its mass is greater or equal to 20 kg.
    if mass >= 20:
        heavy = True

    # Debug prints
    print("\n\nPARAMS:", "width:", width, "height:", height, "length:", length, "mass:", mass)
    print("volume:", volume)
    print("volume_is_bulky:", volume_is_bulky)
    print("dimensions_are_bulky:", dimensions_are_bulky)
    print("bulky:", bulky)
    print("heavy:", heavy)

    # You must dispatch the packages in the following stacks:
    # - **STANDARD**: standard packages (those that are not bulky or heavy) can be handled normally.
    if not bulky and not heavy:
        return constants.STANDARD

    # - **SPECIAL**: packages that are either heavy or bulky can't be handled automatically.
    if (heavy or bulky) and (heavy != bulky):  # Use != to calculate XOR of these two
        return constants.SPECIAL

    # - **REJECTED**: packages that are **both** heavy and bulky are rejected.
    if heavy and bulky:
        return constants.REJECTED
