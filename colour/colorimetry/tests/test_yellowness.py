# !/usr/bin/env python
"""Define the unit tests for the :mod:`colour.colorimetry.yellowness` module."""

import numpy as np
import unittest
from itertools import product

from colour.colorimetry import (
    yellowness_ASTMD1925,
    yellowness_ASTME313_alternative,
    yellowness_ASTME313,
)
from colour.colorimetry.yellowness import YELLOWNESS_COEFFICIENTS_ASTME313
from colour.colorimetry.yellowness import yellowness
from colour.utilities import domain_range_scale, ignore_numpy_errors

__author__ = "Colour Developers"
__copyright__ = "Copyright 2013 Colour Developers"
__license__ = "BSD-3-Clause - https://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-developers@colour-science.org"
__status__ = "Production"

__all__ = [
    "TestYellownessASTMD1925",
    "TestYellownessASTM313Alternative",
    "TestYellownessASTM313",
    "TestYellowness",
]


class TestYellownessASTMD1925(unittest.TestCase):
    """
    Define :func:`colour.colorimetry.yellowness.yellowness_ASTMD1925`
    definition unit tests methods.
    """

    def test_yellowness_ASTMD1925(self):
        """
        Test :func:`colour.colorimetry.yellowness.yellowness_ASTMD1925`
        definition.
        """

        self.assertAlmostEqual(
            yellowness_ASTMD1925(
                np.array([95.00000000, 100.00000000, 105.00000000])
            ),
            10.299999999999997,
            places=7,
        )

        self.assertAlmostEqual(
            yellowness_ASTMD1925(
                np.array([105.00000000, 100.00000000, 95.00000000])
            ),
            33.700000000000003,
            places=7,
        )

        self.assertAlmostEqual(
            yellowness_ASTMD1925(
                np.array([100.00000000, 100.00000000, 100.00000000])
            ),
            22.0,
            places=7,
        )

    def test_n_dimensional_yellowness_ASTMD1925(self):
        """
        Test :func:`colour.colorimetry.yellowness.yellowness_ASTMD1925`
        definition n_dimensional arrays support.
        """

        XYZ = np.array([95.00000000, 100.00000000, 105.00000000])
        YI = yellowness_ASTMD1925(XYZ)

        XYZ = np.tile(XYZ, (6, 1))
        YI = np.tile(YI, 6)
        np.testing.assert_array_almost_equal(
            yellowness_ASTMD1925(XYZ), YI, decimal=7
        )

        XYZ = np.reshape(XYZ, (2, 3, 3))
        YI = np.reshape(YI, (2, 3))
        np.testing.assert_array_almost_equal(
            yellowness_ASTMD1925(XYZ), YI, decimal=7
        )

    def test_domain_range_scale_yellowness_ASTMD1925(self):
        """
        Test :func:`colour.colorimetry.yellowness.yellowness_ASTMD1925`
        definition domain and range scale support.
        """

        XYZ = np.array([95.00000000, 100.00000000, 105.00000000])
        YI = 10.299999999999997

        d_r = (("reference", 1), ("1", 0.01), ("100", 1))
        for scale, factor in d_r:
            with domain_range_scale(scale):
                np.testing.assert_array_almost_equal(
                    yellowness_ASTMD1925(XYZ * factor), YI * factor, decimal=7
                )

    @ignore_numpy_errors
    def test_nan_yellowness_ASTMD1925(self):
        """
        Test :func:`colour.colorimetry.yellowness.yellowness_ASTMD1925`
        definition nan support.
        """

        cases = [-1.0, 0.0, 1.0, -np.inf, np.inf, np.nan]
        cases = np.array(list(set(product(cases, repeat=3))))
        yellowness_ASTMD1925(cases)


class TestYellownessASTM313Alternative(unittest.TestCase):
    """
    Define :func:`colour.colorimetry.yellowness.\
yellowness_ASTME313_alternative` definition unit tests methods.
    """

    def test_yellowness_ASTME313_alternative(self):
        """
        Test :func:`colour.colorimetry.yellowness.\
yellowness_ASTME313_alternative` definition.
        """

        self.assertAlmostEqual(
            yellowness_ASTME313_alternative(
                np.array([95.00000000, 100.00000000, 105.00000000])
            ),
            11.065000000000003,
            places=7,
        )

        self.assertAlmostEqual(
            yellowness_ASTME313_alternative(
                np.array([105.00000000, 100.00000000, 95.00000000])
            ),
            19.534999999999989,
            places=7,
        )

        self.assertAlmostEqual(
            yellowness_ASTME313_alternative(
                np.array([100.00000000, 100.00000000, 100.00000000])
            ),
            15.300000000000002,
            places=7,
        )

    def test_n_dimensional_yellowness_ASTME313_alternative(self):
        """
        Test :func:`colour.colorimetry.yellowness.\
yellowness_ASTME313_alternative` definition n_dimensional arrays support.
        """

        XYZ = np.array([95.00000000, 100.00000000, 105.00000000])
        YI = yellowness_ASTME313_alternative(XYZ)

        XYZ = np.tile(XYZ, (6, 1))
        YI = np.tile(YI, 6)
        np.testing.assert_array_almost_equal(
            yellowness_ASTME313_alternative(XYZ), YI, decimal=7
        )

        XYZ = np.reshape(XYZ, (2, 3, 3))
        YI = np.reshape(YI, (2, 3))
        np.testing.assert_array_almost_equal(
            yellowness_ASTME313_alternative(XYZ), YI, decimal=7
        )

    def test_domain_range_scale_yellowness_ASTME313_alternative(self):
        """
        Test :func:`colour.colorimetry.yellowness.\
yellowness_ASTME313_alternative` definition domain and range scale support.
        """

        XYZ = np.array([95.00000000, 100.00000000, 105.00000000])
        YI = 11.065000000000003

        d_r = (("reference", 1), ("1", 0.01), ("100", 1))
        for scale, factor in d_r:
            with domain_range_scale(scale):
                np.testing.assert_array_almost_equal(
                    yellowness_ASTME313_alternative(XYZ * factor),
                    YI * factor,
                    decimal=7,
                )

    @ignore_numpy_errors
    def test_nan_yellowness_ASTME313_alternative(self):
        """
        Test :func:`colour.colorimetry.yellowness.\
yellowness_ASTME313_alternative` definition nan support.
        """

        cases = [-1.0, 0.0, 1.0, -np.inf, np.inf, np.nan]
        cases = np.array(list(set(product(cases, repeat=3))))
        yellowness_ASTME313_alternative(cases)


class TestYellownessASTM313(unittest.TestCase):
    """
    Define :func:`colour.colorimetry.yellowness.yellowness_ASTME313`
    definition unit tests methods.
    """

    def test_yellowness_ASTME313(self):
        """
        Test :func:`colour.colorimetry.yellowness.yellowness_ASTME313`
        definition.
        """

        self.assertAlmostEqual(
            yellowness_ASTME313(
                np.array([95.00000000, 100.00000000, 105.00000000])
            ),
            4.340000000000003,
            places=7,
        )

        self.assertAlmostEqual(
            yellowness_ASTME313(
                np.array([105.00000000, 100.00000000, 95.00000000])
            ),
            28.660000000000011,
            places=7,
        )

        self.assertAlmostEqual(
            yellowness_ASTME313(
                np.array([100.00000000, 100.00000000, 100.00000000])
            ),
            16.500000000000000,
            places=7,
        )

        self.assertAlmostEqual(
            yellowness_ASTME313(
                np.array([95.00000000, 100.00000000, 105.00000000]),
                YELLOWNESS_COEFFICIENTS_ASTME313[
                    "CIE 1931 2 Degree Standard Observer"
                ]["C"],
            ),
            10.089500000000001,
            places=7,
        )

    def test_n_dimensional_yellowness_ASTME313(self):
        """
        Test :func:`colour.colorimetry.yellowness.yellowness_ASTME313`
        definition n_dimensional arrays support.
        """

        XYZ = np.array([95.00000000, 100.00000000, 105.00000000])
        YI = yellowness_ASTME313(XYZ)

        XYZ = np.tile(XYZ, (6, 1))
        YI = np.tile(YI, 6)
        np.testing.assert_array_almost_equal(
            yellowness_ASTME313(XYZ), YI, decimal=7
        )

        XYZ = np.reshape(XYZ, (2, 3, 3))
        YI = np.reshape(YI, (2, 3))
        np.testing.assert_array_almost_equal(
            yellowness_ASTME313(XYZ), YI, decimal=7
        )

    def test_domain_range_scale_yellowness_ASTME313(self):
        """
        Test :func:`colour.colorimetry.yellowness.yellowness_ASTME313`
        definition domain and range scale support.
        """

        XYZ = np.array([95.00000000, 100.00000000, 105.00000000])
        YI = 4.340000000000003

        d_r = (("reference", 1), ("1", 0.01), ("100", 1))
        for scale, factor in d_r:
            with domain_range_scale(scale):
                np.testing.assert_array_almost_equal(
                    yellowness_ASTME313(XYZ * factor), YI * factor, decimal=7
                )

    @ignore_numpy_errors
    def test_nan_yellowness_ASTME313(self):
        """
        Test :func:`colour.colorimetry.yellowness.yellowness_ASTME313`
        definition nan support.
        """

        cases = [-1.0, 0.0, 1.0, -np.inf, np.inf, np.nan]
        cases = np.array(list(set(product(cases, repeat=3))))
        yellowness_ASTME313(cases)


class TestYellowness(unittest.TestCase):
    """
    Define :func:`colour.colorimetry.yellowness.yellowness` definition unit
    tests methods.
    """

    def test_domain_range_scale_yellowness(self):
        """
        Test :func:`colour.colorimetry.yellowness.yellowness` definition
        domain and range scale support.
        """

        XYZ = np.array([95.00000000, 100.00000000, 105.00000000])

        m = ("ASTM D1925", "ASTM E313")
        v = [yellowness(XYZ, method) for method in m]

        d_r = (("reference", 1), ("1", 0.01), ("100", 1))
        for method, value in zip(m, v):
            for scale, factor in d_r:
                with domain_range_scale(scale):
                    np.testing.assert_array_almost_equal(
                        yellowness(XYZ * factor, method),
                        value * factor,
                        decimal=7,
                    )


if __name__ == "__main__":
    unittest.main()
