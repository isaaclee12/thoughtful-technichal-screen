# pylint: disable=too-many-arguments, too-many-positional-arguments, missing-function-docstring
"""
Tests for the sort function
"""
from unittest import TestCase
import ddt

from sort import sort
from efficient_sort import sort as efficient_sort
import constants


@ddt.ddt
class SortTestCase(TestCase):
    """
    Test Cases for the sort() function.
    Note that this doesn't cover every theoretical possible case that this function could cover,
    in case that's something that is being looked for.

    Test Case Data Format: (width, height, length, mass)
    """

    @ddt.data(
        (0.5, 0.5, 0.5, 0.5, constants.INTEGER_ERROR_MESSAGE),
        ("potato", 1, 1, 1, constants.INTEGER_ERROR_MESSAGE),
        (0, 1, 1, 1, constants.ZERO_OR_NEGATIVE_ERROR_MESSAGE),
        (-1, 1, 1, 1, constants.ZERO_OR_NEGATIVE_ERROR_MESSAGE),
    )
    @ddt.unpack
    def test_sort_errors(self, width, height, length, mass, expected_error_msg):
        error_msg = sort(width, height, length, mass)
        self.assertEqual(error_msg, expected_error_msg)

    @ddt.data(
        # Should return STANDARD
        (1, 1, 1, 1),

        # Any measure is under 150cm (up to two measures since 149cm^3 > 1,000,000 cm^3)
        (149, 1, 1, 1),
        (1, 149, 1, 1),
        (1, 1, 149, 1),
        (149, 149, 1, 1),
        (149, 1, 149, 1),
        (1, 149, 149, 1),

        # Volume just under 1,000,000 cm^3
        (63, 143, 111, 1),
    )
    @ddt.unpack
    def test_sort_standard(self, width, height, length, mass):
        stack_name = sort(width, height, length, mass)
        self.assertEqual(stack_name, constants.STANDARD)

    @ddt.data(
        # Should return SPECIAL
        # Volume = 150 exactly
        (150, 1, 1, 10),
        (1, 150, 1, 10),
        (1, 1, 150, 10),

        # Individual dimensions ARE HUGE
        (9999, 1, 1, 10),
        (9999, 9999, 9999, 10),

        # Volume = 1 mil cm^3 exactly
        (100, 100, 100, 10),

        # Volume is monstrous
        (1000000, 1000, 10000, 10),

        # Mass = 20kg exactly
        (1, 1, 1, 20),

        # Mass is HEAVY
        (1, 1, 1, 99999999999),
    )
    @ddt.unpack
    def test_sort_special(self, width, height, length, mass):
        stack_name = sort(width, height, length, mass)
        self.assertEqual(stack_name, constants.SPECIAL)

    @ddt.data(
        # Should return REJECTED
        (150, 1, 1, 20),
        (150, 150, 150, 20),
        (1000000, 1, 1, 20),
        (999, 999, 999, 999),
    )
    @ddt.unpack
    def test_sort_rejects(self, width, height, length, mass):
        stack_name = sort(width, height, length, mass)
        self.assertEqual(stack_name, constants.REJECTED)

@ddt.ddt
class EfficientSortTestCase(TestCase):
    """
    Test Cases for the efficient version of the sort() function.
    Note that this doesn't cover every theoretical possible case that this function could cover,
    in case that's something that is being looked for.

    Test Case Data Format: (width, height, length, mass)
    """

    @ddt.data(
        (0.5, 0.5, 0.5, 0.5, constants.INTEGER_ERROR_MESSAGE),
        ("potato", 1, 1, 1, constants.INTEGER_ERROR_MESSAGE),
        (0, 1, 1, 1, constants.ZERO_OR_NEGATIVE_ERROR_MESSAGE),
        (-1, 1, 1, 1, constants.ZERO_OR_NEGATIVE_ERROR_MESSAGE),
    )
    @ddt.unpack
    def test_efficient_sort_errors(self, width, height, length, mass, expected_error_msg):
        error_msg = efficient_sort(width, height, length, mass)
        self.assertEqual(error_msg, expected_error_msg)

    @ddt.data(
        # Should return STANDARD
        (1, 1, 1, 1),

        # Any measure is under 150cm (up to two measures since 149cm^3 > 1,000,000 cm^3)
        (149, 1, 1, 1),
        (1, 149, 1, 1),
        (1, 1, 149, 1),
        (149, 149, 1, 1),
        (149, 1, 149, 1),
        (1, 149, 149, 1),

        # Volume just under 1,000,000 cm^3
        (63, 143, 111, 1),
    )
    @ddt.unpack
    def test_efficient_sort_standard(self, width, height, length, mass):
        stack_name = efficient_sort(width, height, length, mass)
        self.assertEqual(stack_name, constants.STANDARD)

    @ddt.data(
        # Should return SPECIAL
        # Volume = 150 exactly
        (150, 1, 1, 10),
        (1, 150, 1, 10),
        (1, 1, 150, 10),

        # Individual dimensions ARE HUGE
        (9999, 1, 1, 10),
        (9999, 9999, 9999, 10),

        # Volume = 1 mil cm^3 exactly
        (100, 100, 100, 10),

        # Volume is monstrous
        (1000000, 1000, 10000, 10),

        # Mass = 20kg exactly
        (1, 1, 1, 20),

        # Mass is HEAVY
        (1, 1, 1, 99999999999),
    )
    @ddt.unpack
    def test_efficient_sort_special(self, width, height, length, mass):
        stack_name = efficient_sort(width, height, length, mass)
        self.assertEqual(stack_name, constants.SPECIAL)

    @ddt.data(
        # Should return REJECTED
        (150, 1, 1, 20),
        (150, 150, 150, 20),
        (1000000, 1, 1, 20),
        (999, 999, 999, 999),
    )
    @ddt.unpack
    def test_efficient_sort_rejects(self, width, height, length, mass):
        stack_name = efficient_sort(width, height, length, mass)
        self.assertEqual(stack_name, constants.REJECTED)
