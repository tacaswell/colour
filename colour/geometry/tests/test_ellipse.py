# !/usr/bin/env python
"""Define the unit tests for the :mod:`colour.geometry.ellipse` module."""

import numpy as np
import unittest

from colour.geometry import (
    ellipse_coefficients_general_form,
    ellipse_coefficients_canonical_form,
    point_at_angle_on_ellipse,
    ellipse_fitting_Halir1998,
)

__author__ = "Colour Developers"
__copyright__ = "Copyright 2013 Colour Developers"
__license__ = "BSD-3-Clause - https://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-developers@colour-science.org"
__status__ = "Production"

__all__ = [
    "TestEllipseCoefficientsCanonicalForm",
    "TestEllipseCoefficientsGeneralForm",
    "TestPointAtAngleOnEllipse",
    "TestEllipseFittingHalir1998",
]


class TestEllipseCoefficientsCanonicalForm(unittest.TestCase):
    """
    Define :func:`colour.geometry.ellipse.ellipse_coefficients_canonical_form`
    definition unit tests methods.
    """

    def test_ellipse_coefficients_canonical_form(self):
        """
        Test :func:`colour.geometry.ellipse.\
ellipse_coefficients_canonical_form` definition.
        """

        np.testing.assert_array_almost_equal(
            ellipse_coefficients_canonical_form(
                np.array([2.5, -3.0, 2.5, -1.0, -1.0, -3.5])
            ),
            np.array([0.5, 0.5, 2, 1, 45]),
            decimal=7,
        )

        np.testing.assert_array_almost_equal(
            ellipse_coefficients_canonical_form(
                np.array([1.0, 0.0, 1.0, 0.0, 0.0, -1.0])
            ),
            np.array([0.0, 0.0, 1, 1, 0]),
            decimal=7,
        )


class TestEllipseCoefficientsGeneralForm(unittest.TestCase):
    """
    Define :func:`colour.geometry.ellipse.ellipse_coefficients_general_form`
    definition unit tests methods.
    """

    def test_ellipse_coefficients_general_form(self):
        """
        Test :func:`colour.geometry.ellipse.ellipse_coefficients_general_form`
        definition.
        """

        np.testing.assert_array_almost_equal(
            ellipse_coefficients_general_form(np.array([0.5, 0.5, 2, 1, 45])),
            np.array([2.5, -3.0, 2.5, -1.0, -1.0, -3.5]),
            decimal=7,
        )

        np.testing.assert_array_almost_equal(
            ellipse_coefficients_general_form(np.array([0.0, 0.0, 1, 1, 0])),
            np.array([1.0, 0.0, 1.0, 0.0, 0.0, -1.0]),
            decimal=7,
        )


class TestPointAtAngleOnEllipse(unittest.TestCase):
    """
    Define :func:`colour.geometry.ellipse.point_at_angle_on_ellipse`
    definition unit tests methods.
    """

    def test_point_at_angle_on_ellipse(self):
        """
        Test :func:`colour.geometry.ellipse.point_at_angle_on_ellipse`
        definition.
        """

        np.testing.assert_array_almost_equal(
            point_at_angle_on_ellipse(
                np.array([0, 90, 180, 270]), np.array([0.0, 0.0, 2, 1, 0])
            ),
            np.array([[2, 0], [0, 1], [-2, 0], [0, -1]]),
            decimal=7,
        )

        np.testing.assert_array_almost_equal(
            point_at_angle_on_ellipse(
                np.linspace(0, 360, 10), np.array([0.5, 0.5, 2, 1, 45])
            ),
            np.array(
                [
                    [1.91421356, 1.91421356],
                    [1.12883096, 2.03786992],
                    [0.04921137, 1.44193985],
                    [-0.81947922, 0.40526565],
                    [-1.07077081, -0.58708129],
                    [-0.58708129, -1.07077081],
                    [0.40526565, -0.81947922],
                    [1.44193985, 0.04921137],
                    [2.03786992, 1.12883096],
                    [1.91421356, 1.91421356],
                ]
            ),
            decimal=7,
        )


class TestEllipseFittingHalir1998(unittest.TestCase):
    """
    Define :func:`colour.geometry.ellipse.ellipse_fitting_Halir1998`
    definition unit tests methods.
    """

    def test_ellipse_fitting_Halir1998(self):
        """
        Test :func:`colour.geometry.ellipse.ellipse_fitting_Halir1998`
        definition.
        """

        np.testing.assert_array_almost_equal(
            ellipse_fitting_Halir1998(
                np.array([[2, 0], [0, 1], [-2, 0], [0, -1]])
            ),
            np.array(
                [
                    0.24253563,
                    0.00000000,
                    0.97014250,
                    0.00000000,
                    0.00000000,
                    -0.97014250,
                ]
            ),
            decimal=7,
        )


if __name__ == "__main__":
    unittest.main()
